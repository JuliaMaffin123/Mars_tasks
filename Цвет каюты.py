from flask import Flask, render_template

app = Flask("MyApp")


@app.route("/table/<m_or_f>/<int:age>")
def rooms(m_or_f, age):
    return render_template('color.html', m_or_f=m_or_f, age=age)


app.run(host='127.0.0.1', port=8080, debug=True)
