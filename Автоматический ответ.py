from flask import Flask, url_for, request, render_template

app = Flask("MyApp")


@app.route('/auto_answer', methods=['POST', 'GET'])
@app.route('/answer', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return render_template('form.html')
    elif request.method == 'POST':
        rec_dict = {
            'title': 'Анкета',
            'surname': request.form['surname'],
            'name': request.form['name'],
            'education': request.form['class'],
            'profession': request.form.getlist('professions'),
            'sex': request.form['sex'],
            'motivation': request.form['about'],
            'ready': request.form.get('accept'),
        }
        # print(request.form['surname'])
        # print(request.form['name'])
        # print(request.form['email'])
        # print(request.form['class'])
        # print(request.form.getlist('professions'))
        # print(request.form['sex'])
        # print(request.form['about'])
        # f = request.files['file']
        # print(f.read())
        # print(request.form.get('accept'))
        return render_template('auto_answer.html',
                               title=rec_dict['title'],
                               surname=rec_dict['surname'],
                               name=rec_dict['name'],
                               education=rec_dict['education'],
                               profession=rec_dict['profession'],
                               sex=rec_dict['sex'],
                               motivation=rec_dict['motivation'],
                               ready=rec_dict['ready'])


app.run(host='127.0.0.1', port=8080, debug=True)
