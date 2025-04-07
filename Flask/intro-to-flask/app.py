# pyenv exec python -m venv .venv
# source .venv/bin/activate
# pip install Flask

# export FLASK_APP=app.py
# export FLASK_DEBUG=1
# flask run

from flask import Flask, render_template

app = Flask(__name__)

class GalileanMoons:
    def __init__(self, first, second, third, fourth):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth

@app.route("/")
def hello_world():
    # return "Hello, world!"
    # return render_template("first_page.html")
    return render_template("jinja_intro.html", name="Bob Smith", template_name="Jinja 2")


@app.route("/vincent")
def hello_world_vincent():
    # return """
    # <html>
    # <body>
    # <h1>Greeting!</h1>
    # <p>Hello, World!</p>
    # </body>
    # </html>
    # """
    return render_template("second_page.html")


@app.route("/expressions/")
def expressions():
    #interpolation
    color = "brown"
    animal_one = "fox"
    animal_amount = "dog"

    #addition and subtraction
    orange_amount = 10
    apple_amount = 20
    donate_amount = 15

    #string concatenation
    first_name = "Captain"
    last_name = "Marvel"

    kwargs = {
        "color": color,
        "animal_one": animal_one,
        "animal_amount": animal_amount,
        "orange_amount": orange_amount,
        "apple_amount":  apple_amount,
        "donate_amount": donate_amount,
        "first_name": first_name,
        "last_name": last_name,
    }

    return render_template(
        "expressions.html",
        # color=color,
        # animal_one=animal_one,
        # animal_amount=animal_amount,
        # orange_amount=orange_amount,
        # apple_amount=apple_amount,
        # donate_amount=donate_amount,
        # first_name=first_name,
        # last_name=last_name,
        **kwargs
    )

@app.route("/data-structures/")
def render_data_structures():

    movies = [
        "Leon the professional",
        "The Usual Suspects",
        "A Beautiful Mind"
    ]

    car = {
        "brand": "Tesla",
        "model": "Roadster",
        "year": "2020"
    }

    moons = GalileanMoons("Io", "Europa", "Ganymede", "Callisto")

    kwargs = {
        "movies": movies,
        "car":  car,
        "moons": moons
    }

    return render_template(
        "data_structures.html", 
        # movies=movies, car=car, moons=moons
        **kwargs
    )

@app.route("/conditions-basics/")
def render_conditionals():
    company = "Microsoft"

    return render_template("conditionals_basics.html", company=company)

@app.route("/for-loop")
def render_loops_for():
    planets = [
        'Mercury',
        'Venus',
        'Earth',
        'Mars',
        'Jupiter',
        'Saturn',
        'Uranus',
        'Neptune',
    ]

    return render_template("for_loop.html", planets=planets)

@app.route("/for-loop/conditionals/")
def render_for_loop_conditionals():
    user_os = {
        "Bob Smith": "Windows",
        "Anne Pun": "MacOS",
        "Adam Lee": "Linux",
        "Jose Salvatierra": "Windows"
    }

    return render_template('loops_and_conditionals.html', user_os=user_os)

@app.route("/defining-variables/using-set-keyword/")
def defining_variables_using_set_keyword():
    return render_template('defining_variable.html', todos=["Get milk", "Learn programming"])

@app.route("/macro/")
def macro():
    todos = [
        ("Get milk", False),
        ("Learn programming", True)
    ]

    return render_template('macro.html', todos=todos)