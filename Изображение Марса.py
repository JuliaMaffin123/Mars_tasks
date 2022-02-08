from flask import Flask, url_for

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


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src={url_for("static", filename="mars.jpg")}>
                    <p>Вот она какая, красная планета.</p>
                  </body>
                </html>"""


app.run(host='127.0.0.1', port=8080, debug=True)
