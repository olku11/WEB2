from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
@app.route("/index/<title>")
def index(title=""):
    return render_template("base.html", title=title)


@app.route("/training/<prof>")
def training(prof):
    pro = prof
    if "строитель" in pro:
        pro = "строитель"
    elif "инженер" in pro:
        pro = "инженер"
    return render_template("ex2.html", prof=pro)


@app.route("/list_prof/<list>")
def list_prof(list):
    pr = "Инженер, пилот, строитель, биолог, врач, климатолог, специалист по радиоционной защите, геолог, метеоролог," \
         "оператор марсохода, штурман, астролог".split(", ")
    return render_template("ex3.html", list=list, user_list=pr)


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
