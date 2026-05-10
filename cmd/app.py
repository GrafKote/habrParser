from flask import Flask, render_template


app = Flask(__name__, template_folder='../templates')

TEXT = '''
Привет это тестовое приложение
для знакомства с фласком
и шаблонизатором Джинджа!
'''

students = [
    {'name': 'Костя', 'age': 25},
    {'name': 'Никита', 'age': 28},
    {'name': 'Дима', 'age': 22},
]


@app.route('/')
def base():
    return render_template("base.html", dis_text=TEXT, students=students)



if __name__ == '__main__':
    app.run()