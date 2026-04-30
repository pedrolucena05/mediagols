import psycopg2

conn = psycopg2.connect(
    dbname="bestBet",
    user="postgres",
    password="senha",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS leagues (
    id SERIAL PRIMARY KEY,
    url VARCHAR(80) NOT NULL,
    leagueName VARCHAR(40) NOT NULL
);
""")

conn.commit()

cursor.close()
conn.close()

print("Tabela leagues criada com sucesso!")