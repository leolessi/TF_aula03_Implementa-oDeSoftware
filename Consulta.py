from flask import Flask, jsonify, request
import mysql.connector

app = Flask("alunos")


def connect_to_db():
    try:
        connection = mysql.connector.connect(
            database="alunos", user="faat", password="faat", host="localhost", port=3306
        )
        return connection
    except mysql.connector.Error as error:
        print(f"Erro ao conectar ao banco de dados: {error}")
        return None


@app.route("/alunos", methods=["GET"])
def obter_alunos():
    connection = connect_to_db()
    if connection is None:
        return jsonify({"erro": "Falha ao conectar ao banco de dados"}), 500

    try:
        cursor = connection.cursor()
        query = "SELECT id, nome, idade, curso FROM alunos"
        cursor.execute(query)
        rows = cursor.fetchall()

        alunos = [
            {"id": row[0], "nome": row[1], "idade": row[2], "curso": row[3]}
            for row in rows
        ]
        return jsonify(alunos)
    except mysql.connector.Error as error:
        print(f"Erro ao obter alunos: {error}")
        return jsonify({"erro": "Falha ao obter dados"}), 500
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()


@app.route("/alunos/<int:aluno_id>", methods=["GET"])
def obter_aluno(aluno_id):
    connection = connect_to_db()
    if connection is None:
        return jsonify({"erro": "Falha ao conectar ao banco de dados"}), 500

    try:
        cursor = connection.cursor()
        query = "SELECT id, nome, idade, curso FROM alunos WHERE id = %s"
        cursor.execute(query, (aluno_id,))
        row = cursor.fetchone()

        if row is None:
            return jsonify({"erro": "Aluno não encontrado"}), 404

        aluno = {"id": row[0], "nome": row[1], "idade": row[2], "curso": row[3]}
        return jsonify(aluno)
    except mysql.connector.Error as error:
        print(f"Erro ao obter aluno: {error}")
        return jsonify({"erro": "Falha ao obter dados"}), 500
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()


if __name__ == "__main__":
    app.run(debug=True)
