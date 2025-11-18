import pandas as pd
import numpy as np
from pathlib import Path

def read_matches_from_file(path):
    """
    Lê o arquivo cujo formato de cada linha é:
      <date> , <home> , <home_goals - away_goals> , <away>
    Retorna DataFrame com colunas: date, home, away, home_goals, away_goals, total_goals
    """


    output_dir = Path("leagues")
    # Resolve o caminho absoluto (útil para debug)
    path = str(path)  # garante str se vier Path
    output_path = (output_dir / path).resolve()
    temp_path = output_path.with_suffix(output_path.suffix + ".tmp")  # leagues/arquivo.txt.tmp
    patcha = "leagues/" + path
    rows = []
    with open(patcha, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            # dividir por ' , ' (com espaços como no seu exemplo)
            parts = [p.strip() for p in line.split(" , ")]
            if len(parts) != 4:
                # tenta dividir por vírgula genérica caso o arquivo tenha outro espaçamento
                parts = [p.strip() for p in line.split(",")]
            if len(parts) != 4:
                # pula linha inválida (ou trate como erro)
                print("Linha ignorada (formato inesperado):", line)
                continue
            date_raw, home, score, away = parts
            # parse score "0 - 3"
            try:
                left, right = [s.strip() for s in score.split("-")]
                home_goals = int(left)
                away_goals = int(right)
            except Exception as e:
                print("Erro ao parsear score:", score, "->", e)
                continue
            rows.append({
                "date_raw": date_raw,
                "home": home,
                "away": away,
                "home_goals": home_goals,
                "away_goals": away_goals,
                "total_goals": home_goals + away_goals
            })
    
    return pd.DataFrame(rows)
    


def compute_team_stats(df):
    """
    Recebe DataFrame com colunas home, away, home_goals, away_goals, total_goals.
    Retorna DataFrame agregado por time com as métricas pedidas.
    """
    # Estatísticas quando time é mandante
    home_grp = df.groupby("home").agg(
        home_matches = ("home_goals", "count"),
        home_goals = ("home_goals", "sum"),
        home_conceded = ("away_goals", "sum"),
        home_over_1_5 = ("total_goals", lambda s: (s > 1.5).sum()),
        home_over_2_5 = ("total_goals", lambda s: (s > 2.5).sum()),
    ).rename_axis("team").reset_index()

    # Estatísticas quando time é visitante
    away_grp = df.groupby("away").agg(
        away_matches = ("away_goals", "count"),
        away_goals = ("away_goals", "sum"),
        away_conceded = ("home_goals", "sum"),
        away_over_1_5 = ("total_goals", lambda s: (s > 1.5).sum()),
        away_over_2_5 = ("total_goals", lambda s: (s > 2.5).sum()),
    ).rename_axis("team").reset_index()

    # unir ambos (outer join para incluir times que só apareceram como mandante ou visitante)
    merged = pd.merge(home_grp, away_grp, on="team", how="outer").fillna(0)

    # converter para tipos inteiros onde faz sentido
    int_cols = ["home_matches","home_goals","home_conceded","home_over_1_5","home_over_2_5",
                "away_matches","away_goals","away_conceded","away_over_1_5","away_over_2_5"]
    for c in int_cols:
        merged[c] = merged[c].astype(int)

    # métricas derivadas: médias e percentuais (trata divisão por zero)
    merged["home_avg_goals"] = np.where(
        merged["home_matches"]>0,
        merged["home_goals"] / merged["home_matches"],
        0.0
    )
    merged["away_avg_goals"] = np.where(
        merged["away_matches"]>0,
        merged["away_goals"] / merged["away_matches"],
        0.0
    )

    merged["home_pct_over_1_5"] = np.where(
        merged["home_matches"]>0,
        merged["home_over_1_5"] / merged["home_matches"] * 100,
        0.0
    )
    merged["away_pct_over_1_5"] = np.where(
        merged["away_matches"]>0,
        merged["away_over_1_5"] / merged["away_matches"] * 100,
        0.0
    )

    merged["home_pct_over_2_5"] = np.where(
        merged["home_matches"]>0,
        merged["home_over_2_5"] / merged["home_matches"] * 100,
        0.0
    )
    merged["away_pct_over_2_5"] = np.where(
        merged["away_matches"]>0,
        merged["away_over_2_5"] / merged["away_matches"] * 100,
        0.0
    )

    # ordena por nome do time (opcional)
    merged = merged.sort_values("team").reset_index(drop=True)
    return merged

def analyze_file(path_to_file):
    df = read_matches_from_file(path_to_file)
    stats = compute_team_stats(df)
    return df, stats