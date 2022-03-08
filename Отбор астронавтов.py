from flask import Flask, url_for, request, render_template

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


@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src={url_for("static", filename="img/mars.jpg")}>
                    <div class="alert alert-secondary" role="alert">
                      Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-success" role="alert">
                      Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-warning" role="alert">
                      И начнем с Марса!
                    </div>
                    <div class="alert alert-info" role="alert">
                      Присоединяйся!
                    </div>
                  </body>
                </html>"""


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return render_template('form.html')
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['class'])
        print(request.form.getlist('professions'))
        print(request.form['sex'])
        print(request.form['about'])
        f = request.files['file']
        print(f.read())
        print(request.form.get('accept'))
        return "Форма отправлена"


app.run(host='127.0.0.1', port=8080, debug=True)
