from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)

@app.route("/")
def pagina_inicial():
    return "DevOps Hands On - Turma 7ASO Grupo 8"

if __name__ == '__main__':
    app.run()