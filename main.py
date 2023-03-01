from flask import Flask
from flask import render_template, redirect
from wtforms import StringField, PasswordField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "yandexlyceum_secret_key"
data = {}
app.config["UPLOAD_FOLDER"] = "static/images/"


class LoginForm(FlaskForm):
    id_user = StringField("id астронавта", validators=[DataRequired()])
    password = PasswordField("Пароль астронавта", validators=[DataRequired()])
    id_cap = StringField("id капитана", validators=[DataRequired()])
    token = PasswordField("Токен капитана", validators=[DataRequired()])
    submit = SubmitField("Доступ")


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


@app.route("/answer")
@app.route("/auto_answer")
def answer():
    title = "Анкета пролетария"
    surname = "Иванов"
    name = "Иван"
    education = "среднее професиональное"
    profession = "токарь"
    sex = "м"
    motivation = "Хочу делать табуретки на Марсе"
    ready = "Да"
    d = {"Заголовок": title, "Фамилия": surname, "Имя": name, "Образование": education,
         "Профессия": profession, "Пол": sex, "Мотивация": motivation, "Готовы остаться на Марсе?": ready}
    return render_template("ex4.html", d=d)


@app.route("/login", methods=["GET", "POST"])
def login():
    global data
    form = LoginForm()
    if form.validate_on_submit():
        data = {form.id_user.label: form.id_user.data, form.password.label: form.password.data,
                form.id_cap.label: form.id_cap.data, form.token.label: form.token.data}
        return redirect("/success")
    return render_template("ex5.html", title="Авторизация", form=form)


@app.route("/success")
def ok_page():
    return render_template("ex51.html", data=data, k=len(data))


@app.route('/distribution')
def places():
    pas = ["Ридли Скотт", "Энди Уир", "Марк Уотни", "Венката Капур", "Тедди Сандерс", "Шон Бин"]
    return render_template('ex6.html', pas=pas)


@app.route('/table/<gender>/<int:age>')
def table(gender, age):
    return render_template('ex7.html', gender=gender, age=age)


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
