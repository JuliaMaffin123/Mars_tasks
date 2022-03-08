from flask import Flask, render_template

app = Flask(__name__)


@app.route('/carousel')
def carousel():
    return render_template('carousel.html')


app.run(port=8080, debug=True)
