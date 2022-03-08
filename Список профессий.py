from flask import Flask, render_template

app = Flask(__name__)


@app.route('/list_prof/<ol_ul>')
def training(ol_ul):
    prof_lst = [
        'Инженер-исследователь',
        'Пилот',
        'Строитель',
        'Экзобиолог',
        'Врач',
        'Инженер по терраформированию',
        'Климатолог',
        'Специалист по радиационной защите',
        'Астрогеолог',
        'Гляциолог',
        'Инженер жизнеобеспечения',
        'Метеоролог',
        'Оператор марсохода',
        'Киберинженер',
        'Штурман',
        'Пилот дронов'
    ]
    return render_template('professions.html', ol_ul=ol_ul, prof_lst=prof_lst)


app.run(port=8080, debug=True)
