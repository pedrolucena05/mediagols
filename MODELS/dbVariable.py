import psycopg2

conn = psycopg2.connect(
    dbname="COLOQUE_O_NOME_AQUI",
    user="postgres",
    password="COLOQUE_A_SENHA_AQUI",
    host="host.docker.internal", # host docker
    port="5432"
)

cursor = conn.cursor()