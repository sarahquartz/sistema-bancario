from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "<h1>Sistema Bancário<h1>"

app.run(debug=True)