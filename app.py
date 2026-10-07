from flask import (Flask, render_template, request, redirect, url_for,session,flash)
from werkzeug.security import check_password_hash, generate_password_hash
from banco import Banco

banco = Banco()
banco.carregar()

app = Flask(__name__)
app.secret_key = "minha-chave-secreta"

@app.route("/", methods=["GET", "POST"])
def inicio():

    #se já estiver logado
    if "conta_id" in session:
        return redirect(url_for("minha_conta"))

    if request.method == "POST":

        usuario = request.form["usuario"]
        senha = request.form["senha"]

        conta = banco.buscar_conta_usuario(usuario)

        #conta não encontrada
        if conta is None:
            flash("Usuario ou senha invalido")
            return render_template("index.html")

        #senha incorreta
        if not check_password_hash(conta.senha_hash, senha):
            flash("Usuario ou senha invalido")
            return render_template("index.html")

        #criar sessão
        session["conta_id"] = conta.id
        session["titular"] = conta.titular

        flash("Loguin realizado com sucesso")

        return redirect(url_for("minha_conta"))

    return render_template("index.html")

@app.route("/contas")
def contas():
    return render_template("contas.html",
                           contas = banco.listar_contas())

@app.route("/nova_conta", methods=["GET","POST"])
def nova_conta():

    if request.method == "POST":

        titular = request.form["titular"]
        usuario = request.form["usuario"]
        senha = request.form["senha"]

        usuario_verificar = banco.buscar_conta_usuario(usuario)

        if usuario_verificar is None:

            senha_hash = generate_password_hash(senha)
            banco.criar_conta(titular, usuario, senha_hash)
            banco.salvar()
        else:
            flash("Nome de usuario já existe")
            return redirect(url_for("inicio"))

        return redirect(url_for("inicio"))

    return render_template("nova_conta.html")

@app.route("/minha_conta", methods =["GET", "POST"])
def minha_conta():

    if "conta_id" not in session:
        return redirect(url_for("inicio"))

    conta = banco.buscar_conta(session["conta_id"])

    if request.method == "POST":

        acao = request.form["acao"]

        try:
            valor = float(request.form["valor"])
            if valor > 0:
                #validar a operação
                if acao == "deposito":
                    conta.depositar(valor)
                    banco.salvar()
                    return redirect(url_for("minha_conta"))
                
                elif acao == "saque":
                    conta.sacar(valor)
                    banco.salvar()
                    return redirect(url_for("minha_conta"))
                elif acao == "transferencia":
                    destino_id = int(request.form["destino"])
                    destino = banco.buscar_conta(destino_id)
                    if destino is not None:
                        conta.transferir(valor, destino)
                        banco.salvar()
                    else:
                        flash("Conta invalida")
            else:
                flash("Entrada Invalida")
        except ValueError:
            flash("Entrada Invalida")

    return render_template("conta.html", conta = conta)

@app.route("/logout")
def logout():
    
    session.clear()

    flash("Você saiu do sistema.")

    return redirect(
    url_for("inicio")
    )

app.run(host = '0.0.0.0', debug=True)