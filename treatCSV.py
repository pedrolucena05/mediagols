arquivo = "final.csv"

with open(arquivo, "r", encoding="utf-8") as f:
    conteudo = f.read()

conteudo = conteudo.replace(" , ", " ")

with open(arquivo, "w", encoding="utf-8") as f:
    f.write(conteudo)

print("Arquivo atualizado com sucesso!")