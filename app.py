from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "123hikari"

@app.route("/hikacreation")
def index():
    flash("Tak kenal, maka tak sayang")
    flash("Nama Anda?")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    input_nama = request.form['name_input']
    while input_nama == "":
        request.form['name_input']
    flash("Hello "+str(input_nama)+", terima kasih sudah mengunjungi web Hika Creation.")
    return render_template("index.html")