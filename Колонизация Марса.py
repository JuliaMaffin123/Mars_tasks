from flask import Flask

app = Flask("MyApp")


@app.route('/')
def mission_name():
    return '<h1>Миссия Колонизация Марса</h1>'


@app.route('/index')
def mission_deviz():
    return '<h1>И на Марсе будут яблони цвести!</h1>'


app.run(host='127.0.0.1', port=8080, debug=True)
