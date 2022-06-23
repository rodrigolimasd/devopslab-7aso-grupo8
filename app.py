from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "DevOps Hands On - Turma 7ASO Grupo 8"

if __name__ == '__main__':
    app.run()