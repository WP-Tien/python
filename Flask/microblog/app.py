# pyenv exec python -m venv .venv
# source .venv/bin/activate
# pip install flask
# pip install pymongo[srv]

import datetime
from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)
uri = "mongodb+srv://nguyenhuutienit3895:57X4q46WcEgSPNRd@cluster0.xwlvt.mongodb.net/"
client = MongoClient(uri)
app.db = client.microblog

# entries = []
@app.route("/", methods=["GET", "POST"])
def home():

    print([e for e in app.db.entries.find({})])

    if request.method == "POST":
        entry_content = request.form.get("content")
        formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
        # print(entry_content, formatted_date)
        # entries.append((entry_content, formatted_date))

        app.db.entries.insert_one({"content": entry_content, "date": formatted_date})

        entries_with_date = [
            (
                entry["content"],
                entry["date"],
                datetime.datetime.strptime(entry["date"], "%Y-%m-%d").strftime("%b %d")
            )
            # for entry in entries
            for entry in app.db.entries.find({})
        ]



    return render_template("home.html", entries=entries_with_date)