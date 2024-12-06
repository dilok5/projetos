import mysql.connector

try:
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="gtr3253",
        db="aula"
    )

    cursor = conexao.cursor()

    with open("base.csv", "r") as dados_csv:
        inserir = "INSERT INTO cadastros(id, nome, cidade, uf, email, valor) VALUES (%s, %s, %s, %s, %s, %s)"
        qtd = 0

        for linha in dados_csv:
            coluna = linha.strip().split(";")  # Remove espaços em branco ao redor e divide
            if coluna[0].upper() == "ID":
                continue

            try:
                valores = [int(coluna[0]), coluna[1], coluna[2], coluna[3], coluna[4], float(coluna[5])]
                cursor.execute(inserir, valores)
                qtd += 1
            except ValueError as e:
                print(f"Erro ao processar a linha: {linha.strip()} - {e}")

    conexao.commit()
    print(f"Quantidade total de registros = {qtd}")

except mysql.connector.Error as e:
    print(f"Erro de conexão ou execução no banco de dados: {e}")
finally:
    if 'conexao' in locals() and conexao.is_connected():
        conexao.close()
