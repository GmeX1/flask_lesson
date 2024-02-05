from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promote():
    strings = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
               'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    return '</br>'.join(strings)


@app.route('/image_sample')
def image():
    block = f'''<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.png')}" 
                        alt="здесь должна была быть картинка, но не нашлась">
                    <h2>Вот она какая, красная планета.</h2>
                  </body>
                </html>
    '''
    return block


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
