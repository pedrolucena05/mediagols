import pandas as pd
from pathlib import Path
import traceback

def sortCSV ():

    BASE_DIR = Path(__file__).resolve().parent

    input_csv = BASE_DIR.parent / "next_games.csv"
    output_csv = BASE_DIR.parent / "final.csv"

    MESES = {
        "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4,
        "May": 5, "Jun": 6, "Jul": 7, "Aug": 8,
        "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
    }

    df = pd.read_csv(input_csv)

    def converter_data(valor):
        # Exemplo: "Mon 4 May"

        try:

            partes = valor.split()

            if not partes[0].isdigit():
                
                dia = int(partes[1])
                mes = MESES[partes[2]]
        
            else:
                
                dia = int(partes[0])
                mes = MESES[partes[1]]

            return mes, dia
        
        except Exception as erro:

            print(f"Erro: {erro}")
            print(valor)
            print(partes)
            traceback.print_exc()


    df[["mes_ordem", "dia_ordem"]] = df["Date"].apply(
        lambda x: pd.Series(converter_data(x))
    )

    df = df.sort_values(by=["mes_ordem", "dia_ordem"])

    df = df.drop(columns=["mes_ordem", "dia_ordem"])

    df.to_csv(output_csv, index=False, encoding="utf-8")


