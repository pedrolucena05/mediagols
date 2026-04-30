import re
import csv

MESES = {"Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"}

def formatar_placar_ou_hora(token: str) -> str:
    esquerda, direita = token.split(":")
    if len(esquerda) == 1 and len(direita) == 1:
        return f"{int(esquerda)} - {int(direita)}"
    return token


def parsear_partidas(tokens: list[str]) -> list[dict]:
    registros = []
    i = 0

    while i < len(tokens) and not re.fullmatch(r"\d{1,2}", tokens[i]):
        i += 1

    while i < len(tokens) - 1:
        if not re.fullmatch(r"\d{1,2}", tokens[i]):
            i += 1
            continue

        dia = tokens[i]
        i += 1

        if i >= len(tokens):
            break

        token_mes = tokens[i]
        i += 1

        mes = token_mes[:3]
        if mes not in MESES:
            continue

        mandante_tokens = []
        resto = token_mes[3:]

        if resto:
            mandante_tokens.append(resto)

        while i < len(tokens) and not re.fullmatch(r"\d{1,2}:\d{1,2}", tokens[i]):
            mandante_tokens.append(tokens[i])
            i += 1

        if i >= len(tokens):
            break

        placar_ou_hora = tokens[i]
        i += 1

        visitante_tokens = []
        dia_semana = ""

        while i < len(tokens):
            token = tokens[i]
            visitante_tokens.append(token)
            i += 1

            m = re.search(r"(Mon|Tue|Wed|Thu|Fri|Sat|Sun)$", token)
            if m:
                dia_semana = m.group(1)
                break

        visitante_limpo = []

        for j, token in enumerate(visitante_tokens):
            if j == len(visitante_tokens) - 1:
                token = re.sub(r"(Mon|Tue|Wed|Thu|Fri|Sat|Sun)$", "", token)

            token = re.sub(r"\(.*$", "", token)
            token = re.sub(r"[\+\-]\d.*$", "", token)
            token = token.strip()

            if token:
                visitante_limpo.append(token)

        mandante = " ".join(mandante_tokens).strip()
        visitante = " ".join(visitante_limpo).strip()

        registros.append({
            "Data": f"{dia_semana} {int(dia)} {mes}".strip(),
            "Mandante": mandante,
            "Placar/Hora": formatar_placar_ou_hora(placar_ou_hora),
            "Visitante": visitante,
        })

    return registros


def generateLeagueCSV(tokens: list[str], arquivo_saida: str = "league.csv") -> None:
    partidas = parsear_partidas(tokens)

    with open(arquivo_saida, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["Data", "Mandante", "Placar/Hora", "Visitante"]
        )
        writer.writeheader()
        writer.writerows(partidas)

    print(f"CSV gerado com {len(partidas)} partidas em: {arquivo_saida}")
