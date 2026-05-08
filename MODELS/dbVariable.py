import psycopg2

conn = psycopg2.connect(
    dbname="dbname",
    user="postgres",
    password="password",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()