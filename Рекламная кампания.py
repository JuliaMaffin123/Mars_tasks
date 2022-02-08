from flask import Flask

app = Flask("MyApp")


@app.route('/')
def mission_name():
    return '<h1>Миссия Колонизация Марса</h1>'


@app.route('/index')
def mission_deviz():
    return '<h1>И на Марсе будут яблони цвести!</h1>'


@app.route('/promotion')
def show_promotion():
    return f'<h1>Человечество вырастает из детства.</h1><br>'\
           f'<h1>Человечеству мала одна планета.</h1><br>'\
           f'<h1>Мы сделаем обитаемыми безжизненные пока планеты.</h1><br>'\
           f'<h1>И начнем с Марса!</h1><br>'\
           f'<h1>Присоединяйся!</h1>'


app.run(host='127.0.0.1', port=8080, debug=True)
