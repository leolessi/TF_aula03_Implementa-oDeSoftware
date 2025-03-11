from flask import Flask, jsonify, request

app = Flask(__name__)

# Dados de exemplo (em produção, usaríamos um banco de dados)
alunos = [
    {"id": 1, "nome": "Aluno A", "curso": "Direito"},
    {"id": 2, "nome": "Aluno B", "curso": "ADS"},
]


@app.route("/alunos", methods=["GET"])
def obter_aluno():
    return jsonify(alunos)


@app.route("/alunos/", methods=["GET"])
def obter_aluno(aluno_id):
    aluno = next((p for p in alunos if p["id"] == aluno_id), None)
    if aluno:
        return jsonify(aluno)
    return jsonify({"erro": "Aluno não encontrado"}), 404


if __name__ == "__main__":
    app.run(debug=True)
