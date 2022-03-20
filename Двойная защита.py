from flask import Flask, render_template, redirect
from data.loginform import LoginForm

app = Flask("MyApp")
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login1.html', title='Авторизация', form=form)


@app.route('/success')
def success():
    return '<h1>Форма отправлена, вы на главной странице.</h1>'


app.run(host='127.0.0.1', port=8080, debug=True)
