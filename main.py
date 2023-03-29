from flask.views import MethodView
from wtforms import Form
from flask import Flask, render_template

app = Flask(__name__)
"""Cоздает новый экземпляр класса Flask, который является основным компонентом приложения Flask.
     Аргумент __name__— это специальная переменная Python, для которой установлено имя текущего модуля,
      что позволяет Flask узнать, где найти ресурсы приложения."""

class HomePage(MethodView):

    def get(self):
        return render_template('index.html')


class BillFormPage(MethodView):

    def get(self):
        return "I am the bill form page!"



class ResultsPage(MethodView):
    pass


class BillForm(Form):
    pass


app.add_url_rule('/', view_func=HomePage.as_view('home.page'))
app.add_url_rule('/bill', view_func=BillFormPage.as_view('bill_form_page'))
app.run()