
import csv
import os
import re
from typing import Dict, List, Tuple



SCORE_PATTERN = re.compile(r"^\s*(\d+)\s*-\s*(\d+)\s*$")
TIME_PATTERN = re.compile(r"^\s*\d{1,2}:\d{2}\s*$")


def is_played_match(match):
    return bool(' - ' in match)


def is_future_match(value: str) -> bool:
    return bool(TIME_PATTERN.match(str(value)))


def parse_score(score: str) -> Tuple[int, int]:
    match = SCORE_PATTERN.match(str(score))
    if not match:
        raise ValueError(f"Placar inválido: {score}")
    return int(match.group(1)), int(match.group(2))


def safe_div(numerator: float, denominator: float) -> float:
    return numerator / denominator if denominator else 0.0


def pct(part: int, total: int) -> float:
    return safe_div(part * 100.0, total)


def round2(value: float) -> float:
    return round(value + 1e-12, 2)


def create_team_stats() -> Dict[str, Dict[str, float]]:
    return {}




def ensure_team(team_stats: Dict[str, Dict[str, float]], team: str) -> Dict[str, float]:
    if team not in team_stats:
        team_stats[team] = {
            "home_games": 0,
            "away_games": 0,
            "home_goals_for": 0,
            "away_goals_for": 0,
            "home_goals_against": 0,
            "away_goals_against": 0,
            "home_over_1_5": 0,
            "away_over_1_5": 0,
            "home_over_2_5": 0,
            "away_over_2_5": 0,
            "home_under_2_5": 0,
            "away_under_2_5": 0,
        }
    return team_stats[team]


def calculate_team_averages(input_csv, output_csv):
    team_stats: Dict[str, Dict[str, float]] = create_team_stats()

    with open(input_csv, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            score_or_time = str(row["Placar/Hora"]).strip()

            if not is_played_match(score_or_time):
                continue

            home_team = str(row["Mandante"]).strip()
            away_team = str(row["Visitante"]).strip()
            home_goals, away_goals = parse_score(score_or_time)
            total_goals = home_goals + away_goals

            home = ensure_team(team_stats, home_team)
            away = ensure_team(team_stats, away_team)

            home["home_games"] += 1
            home["home_goals_for"] += home_goals
            home["home_goals_against"] += away_goals

            away["away_games"] += 1
            away["away_goals_for"] += away_goals
            away["away_goals_against"] += home_goals

            if total_goals > 1.5:
                home["home_over_1_5"] += 1
                away["away_over_1_5"] += 1

            if total_goals > 2.5:
                home["home_over_2_5"] += 1
                away["away_over_2_5"] += 1

            if total_goals < 2.5:
                home["home_under_2_5"] += 1
                away["away_under_2_5"] += 1

    enriched_stats: Dict[str, Dict[str, float]] = {}

    for team, stats in sorted(team_stats.items()):
        home_games = int(stats["home_games"])
        away_games = int(stats["away_games"])

        enriched_stats[team] = {
            "Team": team,
            "Home Games": home_games,
            "Away Games": away_games,
            "Avg Goals Scored Home": round2(safe_div(stats["home_goals_for"], home_games)),
            "Avg Goals Scored Away": round2(safe_div(stats["away_goals_for"], away_games)),
            "Avg Goals Conceded Home": round2(safe_div(stats["home_goals_against"], home_games)),
            "Avg Goals Conceded Away": round2(safe_div(stats["away_goals_against"], away_games)),
            "Home Over 1.5 %": round2(pct(stats["home_over_1_5"], home_games)),
            "Away Over 1.5 %": round2(pct(stats["away_over_1_5"], away_games)),
            "Home Over 2.5 %": round2(pct(stats["home_over_2_5"], home_games)),
            "Away Over 2.5 %": round2(pct(stats["away_over_2_5"], away_games)),
            "Home Under 2.5 %": round2(pct(stats["home_under_2_5"], home_games)),
            "Away Under 2.5 %": round2(pct(stats["away_under_2_5"], away_games)),
        }

    fieldnames = [
        "Team",
        "Home Games",
        "Away Games",
        "Avg Goals Scored Home",
        "Avg Goals Scored Away",
        "Avg Goals Conceded Home",
        "Avg Goals Conceded Away",
        "Home Over 1.5 %",
        "Away Over 1.5 %",
        "Home Over 2.5 %",
        "Away Over 2.5 %",
        "Home Under 2.5 %",
        "Away Under 2.5 %",
    ]

    with open(output_csv, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for team in sorted(enriched_stats):
            writer.writerow(enriched_stats[team])

    return enriched_stats


def read_team_averages(averages_csv: str) -> Dict[str, Dict[str, float]]:
    data: Dict[str, Dict[str, float]] = {}

    with open(averages_csv, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            team = str(row["Team"]).strip()
            data[team] = {
                key: float(row[key]) if key != "Team" else row[key]
                for key in row
                if key != "Team"
            }

    return data


def compute_global_thresholds(team_data: Dict[str, Dict[str, float]]) -> Dict[str, float]:
    def avg(key: str) -> float:
        values = [stats[key] for stats in team_data.values()]
        return sum(values) / len(values) if values else 0.0

    return {
        "home_attack_high": avg("Avg Goals Scored Home"),
        "away_attack_high": avg("Avg Goals Scored Away"),
        "home_defense_weak": avg("Avg Goals Conceded Home"),
        "away_defense_weak": avg("Avg Goals Conceded Away"),
    }


def build_bonus_flag(home_team: str, away_team: str, team_data: Dict[str, Dict[str, float]], thresholds: Dict[str, float]) -> str:
    home = team_data.get(home_team)
    away = team_data.get(away_team)
    flags: List[str] = []

    if home and away:
        if (
            home["Avg Goals Scored Home"] >= thresholds["home_attack_high"]
            and away["Avg Goals Conceded Away"] >= thresholds["away_defense_weak"]
        ):
            flags.append("HOME_ATTACK_vs_AWAY_WEAK_DEFENSE")

        if (
            away["Avg Goals Scored Away"] >= thresholds["away_attack_high"]
            and home["Avg Goals Conceded Home"] >= thresholds["home_defense_weak"]
        ):
            flags.append("AWAY_ATTACK_vs_HOME_WEAK_DEFENSE")

    return " | ".join(flags) if flags else ""


def predict_total_goals(home_team: str, away_team: str, team_data: Dict[str, Dict[str, float]]) -> Tuple[float, float, float]:
    home = team_data.get(home_team, {})
    away = team_data.get(away_team, {})

    expected_home_goals = (
        home.get("Avg Goals Scored Home", 0.0) +
        away.get("Avg Goals Conceded Away", 0.0)
    ) / 2.0

    expected_away_goals = (
        away.get("Avg Goals Scored Away", 0.0) +
        home.get("Avg Goals Conceded Home", 0.0)
    ) / 2.0

    expected_total = expected_home_goals + expected_away_goals
    return round2(expected_home_goals), round2(expected_away_goals), round2(expected_total)


def generate_next_games(matches_csv: str, averages_csv: str, output_csv: str, league: str = "", country: str = "") -> None:
    team_data = read_team_averages(averages_csv)
    thresholds = compute_global_thresholds(team_data)

    fieldnames = [
        "Date",
        "Home Team",
        "Away Team",
        "Match",
        "Kickoff",
        "Expected Home Goals",
        "Expected Away Goals",
        "Average",
        "Home Avg Goals Scored Home",
        "Away Avg Goals Scored Away",
        "Home Avg Goals Conceded Home",
        "Away Avg Goals Conceded Away",
        "Home Over 1.5 goals",
        "Away Over 1.5 goals",
        "Home Over 2.5 goals",
        "Away Over 2.5 goals",
        "Home Under 2.5 goals",
        "Away Under 2.5 goals",
        "Bonus Flag",
        "League",
        "Country",
    ]

    rows_to_write = []

    with open(matches_csv, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            score_or_time = str(row["Placar/Hora"]).strip()

            if not is_future_match(score_or_time):
                continue

            date_str = str(row["Data"]).strip()
            home_team = str(row["Mandante"]).strip()
            away_team = str(row["Visitante"]).strip()
            kickoff = score_or_time

            exp_home, exp_away, exp_total = predict_total_goals(home_team, away_team, team_data)
            bonus_flag = build_bonus_flag(home_team, away_team, team_data, thresholds)

            home = team_data.get(home_team, {})
            away = team_data.get(away_team, {})

            rows_to_write.append({
                "Date": date_str,
                "Home Team": home_team,
                "Away Team": away_team,
                "Match": f"{home_team} x {away_team}",
                "Kickoff": kickoff,
                "Expected Home Goals": exp_home,
                "Expected Away Goals": exp_away,
                "Average": exp_total,
                "Home Avg Goals Scored Home": round2(home.get("Avg Goals Scored Home", 0.0)),
                "Away Avg Goals Scored Away": round2(away.get("Avg Goals Scored Away", 0.0)),
                "Home Avg Goals Conceded Home": round2(home.get("Avg Goals Conceded Home", 0.0)),
                "Away Avg Goals Conceded Away": round2(away.get("Avg Goals Conceded Away", 0.0)),
                "Home Over 1.5 goals": round2(home.get("Home Over 1.5 %", 0.0)),
                "Away Over 1.5 goals": round2(away.get("Away Over 1.5 %", 0.0)),
                "Home Over 2.5 goals": round2(home.get("Home Over 2.5 %", 0.0)),
                "Away Over 2.5 goals": round2(away.get("Away Over 2.5 %", 0.0)),
                "Home Under 2.5 goals": round2(home.get("Home Under 2.5 %", 0.0)),
                "Away Under 2.5 goals": round2(away.get("Away Under 2.5 %", 0.0)),
                "Bonus Flag": bonus_flag,
                "League": league,
                "Country": country,
            })

    with open(output_csv, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows_to_write)


def processNextMatches(league_csv, output_team_averages_csv, output_next_games_csv, league):
    if not os.path.exists(league_csv):
        raise FileNotFoundError(f"Arquivo não encontrado: {league_csv}")

    calculate_team_averages(league_csv, output_team_averages_csv)
    generate_next_games(league_csv, output_team_averages_csv, output_next_games_csv, league)

    print(f"Arquivo de médias gerado: {output_team_averages_csv}")
    print(f"Arquivo de próximos jogos gerado: {output_next_games_csv}")



