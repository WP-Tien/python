# https://github.com/tecladocode/web-dev-bootcamp/blob/master/curriculum/section11/lectures/01_jinja_includes/examples/example_1-1/app.py
# pyenv exec python -m venv .venv
# source .venv/bin/activate
# pip install Flask
# pip install python-dotenv

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("main.html", title="My Webpage")