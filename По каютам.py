from flask import Flask, render_template

app = Flask("MyApp")


@app.route("/distribution")
def rooms():
    lst_to_form = ['Ридли Скотт',
                   'Энди Уир',
                   'Марк Уотни',
                   'Венката Капур',
                   'Тедди Сандерс',
                   'Шон Бин'
                   ]
    return render_template('rooms.html', lst=lst_to_form)


app.run(host='127.0.0.1', port=8080, debug=True)
