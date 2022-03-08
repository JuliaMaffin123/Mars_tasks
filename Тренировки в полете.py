from flask import Flask, render_template

app = Flask(__name__)


@app.route('/training/<prof>')
def training(prof):
    return render_template('train.html', prof=prof)


app.run(port=8080, debug=True)
