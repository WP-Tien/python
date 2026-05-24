from flask import Flask, render_template

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return render_template(
#         "jinja_intro.html",
#         name="Bob Smith",
#         template_name="Django"
#     )

@app.route("/expressions/")
def hello_world_fancy():
    
    # interpolation
    color = "brown"
    animal_one = "fox"
    animal_two = "dog"
    
    # addition and subtraction
    orange_amount = 10
    apple_amount = 20
    donate_amount = 15
    
    # string concatenation
    first_name = "Caption"
    last_name = "Marvel"
    
    kwargs = {
        "color": color,
        "animal_one": animal_one,
        "animal_two": animal_two,
        "orange_amount": orange_amount,
        "apple_amount": apple_amount,
        "donate_amount": donate_amount,
        "first_name": first_name,
        "last_name": last_name,
    }
    
    return render_template("expressions.html", **kwargs)

class GalileanMoons:
    def __init__(self, first, second, third, fourth):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth

@app.route("/data-structures/")
def render_data_structures():
    
    movies = [
        "Leon the Professional",
        "The Usual Suspects",
        "A Beautiful Mind"
    ]
    
    car = {
        "brand": "Tesla",
        "model": "Roadster",
        "year": "2020",
    }
    
    moons = GalileanMoons('Io', 'Europa', 'Ganymede', 'Callisto')
    
    return render_template("data_structures.html", movies=movies, car=car, moons=moons)

@app.route("/conditionals-basics/")
def render_conditionals():
    company = "else condition"
    return render_template("conditionals_basics.html", company=company)

@app.route("/for-loop/")
def render_loops_for():
    planets = [
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune",
    ]
    return render_template("for_loop.html", planets=planets)

@app.route("/for-loop/conditionals/")
def render_for_loop_conditionals():
    user_os = {
        "Bob Smith": "Windows",
        "Anne Pun": "Macos",
        "Adam Lee": "Linux",
        "Jose Salvatierra": "Windows"
    }
    
    return render_template("loops_and_conditionals.html", user_os=user_os)

@app.route("/variables/")
def render_variables():
    todos=["get milk", "Learn programming"]
    return render_template("variables_using_set.html", todos=todos)

@app.route("/macro/")
def render_macro():
    todos = [
        ("Get milk", False),
        ("Learn programming", True)
    ]
    return render_template("macro.html", todos=todos)

todos = [
    ("Get milk", False),
    ("Learn programming", True)
]

@app.route("/")
def todo():
    return render_template("home.html", todos=todos)

@app.route("/<string:todo>")
def todo_item(todo: str):
    for text, completed in todos:
        if text == todo:
            completed_text = "[x]" if completed else "[]"
            title = f"{completed_text} - Todos"
            return render_template("todo.html", text=text, completed=completed, title=title)
    else:
        return render_template("not-found.html", text=todo, title="Not found")