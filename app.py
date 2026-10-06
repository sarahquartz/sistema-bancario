from flask import (Flask, render_template, request, redirect, url_for)
from banco import Banco

banco = Banco()
banco.carregar()

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/contas")
def contas():
    return render_template("contas.html",
                           contas = banco.listar_contas())

@app.route("/nova_conta", methods=["GET","POST"])
def nova_conta():

    if request.method == "POST":

        titular = request.form["titular"]
        banco.criar_conta(titular)
        banco.salvar()

        return redirect(url_for("contas"))

    return render_template("nova_conta.html")

@app.route("/conta/<int:id_conta>", methods =["GET", "POST"])
def conta(id_conta):
    conta = banco.buscar_conta(id_conta)

    if conta is None:
        return "Conta não encontrada"

    return render_template("conta.html", conta = conta)

app.run(debug=True)