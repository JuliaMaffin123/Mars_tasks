from flask import Flask, render_template

app = Flask("MyApp")


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def show_results(nickname, level, rating):
    return render_template('results.html', nickname=nickname, level=level, rating=rating)


app.run(host='127.0.0.1', port=8080, debug=True)
