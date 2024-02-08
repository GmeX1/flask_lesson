from flask import Flask, request, url_for

app = Flask(__name__)


# TODO: поменять содержимое формы

@app.route('/', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        job_list = list(map(
            lambda x: f'<input type="checkbox" class="form-check-input" id="job_{x[0]}" name="jobSelect"'
                      f'value="{x[1].capitalize()}">{x[1].capitalize()}<br/>',
            enumerate(['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
                       'инженер по терраформированию',
                       'климатолог', 'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
                       'инженер жизнеобеспечения',
                       'метеоролог', 'оператор марсохода', 'киберинженер', 'штурман', 'пилот дронов'])
        ))
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" 
                                rel="stylesheet"
                                integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN"
                                crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css"
                                href="{url_for('static', filename='css/style.css')}"/>
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1 class="text-center">Анкета претендента</h1>
                            <h2 class="text-center">На участие в миссии</h2>
                            <div class="modal modal-sheet position-static d-block p-4 py-md-2">
                            <div class="modal-dialog">
                                <div class="modal-content rounded-3 shadow bg-warning-subtle">
                                    <form class="login_form modal-body p-4 text-center" method="post"
                                        enctype="multipart/form-data">
                                        <input class="form-control" id="last_name"
                                        aria-describedby="last_nameHelp" placeholder="Введите имя" name="last_name">
                                        <input class="form-control mb-2" id="name"
                                        aria-describedby="last_nameHelp" placeholder="Введите фамилию" name="last_name">
                                        
                                        <input type="email" class="form-control" id="email"
                                        placeholder="Введите адрес почты" name="email">
                                        <div class="form-group mt-4">
                                            <label for="educationSelect">Какое у Вас образование?</label>
                                            <select class="form-control" id="educationSelect" name="educationSelect">
                                              <option>Начальное</option>
                                              <option>Основное</option>
                                              <option>Среднее общее</option>
                                              <option>Среднее профессиональное</option>
                                              <option>Высшее</option>
                                            </select>
                                         </div>
                                        <div class="form-group form-check mt-4">
                                            <label for="jobSelect">Какие у Вас есть профессии?</label></br>
                                            <div class="text-start mb-4">
                                                {''.join(job_list)}
                                            </div>
                                        </div>
                                        
                                        <div class="form-group mb-4">
                                            <label for="form-check">Укажите пол</label>
                                            <div class="form-check text-start">
                                              <input class="form-check-input" type="radio" name="sex" id="male" 
                                                value="мужской" checked>
                                              <label class="form-check-label" for="male">
                                                Мужской
                                              </label>
                                            </div>
                                            <div class="form-check text-start">
                                              <input class="form-check-input" type="radio" name="sex" id="female" 
                                                value="женский">
                                              <label class="form-check-label" for="female">
                                                Женский
                                              </label>
                                            </div>
                                        </div>
                                        
                                        <div class="form-group mb-4">
                                            <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                            <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                        </div>
                                        <div class="form-group mb-4">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>
                                        <div class="form-group form-check">
                                            <label class="form-check-label" for="acceptStay">
                                                <input type="checkbox" class="form-check-input" id="acceptStay"
                                                name="acceptStay" value="Готов остаться">Готов остаться на Марсе
                                            </label>
                                        </div>
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                    </form>
                                </div>
                            </div>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':  # TODO: сделать серверную часть
        print(request.form.get('last_name'))
        print(request.form.get('name'))
        print(request.form.get('email'))
        print(request.form.get('educationSelect'))
        print(request.form.getlist('jobSelect'))
        print(request.form.get('sex'))
        print(request.form.get('about'))
        print(request.files.get('file'))
        print(request.form.get('acceptStay'))
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
