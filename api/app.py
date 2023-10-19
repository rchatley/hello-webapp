from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


def process_query(query):
    if "name" in query:
        return "Rob"
    else:
        return "unknown"


@app.route("/query")
def query():
    return process_query(request.args.get('q', default="", type=str))


@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_age = request.form.get("age")
    return render_template("hello.html", name=input_name, age=input_age)
