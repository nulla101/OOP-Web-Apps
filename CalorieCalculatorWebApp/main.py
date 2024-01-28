from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from calorie import Calorie
from temperature import Temperature

# Instantiation of the Flask class
app = Flask(__name__)


class HomePage(MethodView):
    """Class to create webpage instances whenever a user
    visits that webpage.
    """

    def get(self):
        # Return the HTML template to the user.
        return render_template('index.html')


class FormPage(MethodView):

    def get(self):
        calories_form = CalorieForm()

        return render_template('form_page.html',
                               calories=calories_form)

    def post(self):
        calories_form = CalorieForm(request.form)

        temperature = Temperature(country=calories_form.country.data,
                                  city=calories_form.city.data).get()

        calorie = Calorie(weight=calories_form.weight.data,
                          height=calories_form.height.data,
                          age=calories_form.age.data,
                          temperature=temperature)

        calories = calorie.calculate()

        return render_template('form_page.html',
                               calories=calories_form,
                               calorie=calories,
                               result=True)


class CalorieForm(Form):

    weight = StringField("Weight: ")
    height = StringField("Height: ")
    age = StringField("Age: ")
    country = StringField("Country: ")
    city = StringField("City: ")

    button = SubmitField("Calculate")


app.add_url_rule('/',
                 view_func=HomePage.as_view('home_page'))
app.add_url_rule('/form_page',
                 view_func=FormPage.as_view('form_page'))

app.run()
