
from MODELS.dbVariable import conn, cursor



cursor.execute("""
CREATE TABLE IF NOT EXISTS next_matches (
    id SERIAL PRIMARY KEY,
    date VARCHAR(20),
    time VARCHAR(10),
    average FLOAT,
    overTwoHalf FLOAT,
    underOneHalf FLOAT,
    homeTeamGoalsMade FLOAT,
    homeTeamGoalsConceded FLOAT,
    awayTeamGoalsMade FLOAT,
    awayTeamGoalsConceded FLOAT
);
""")

conn.commit()

cursor.close()
conn.close()

print("Tabela next_matches criada com sucesso!")