from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def films():
    context = {
        "link": "Персонажи Гарри Поттера"
    }
    return render_template("index.html", **context)



@app.route("/person/")
def person():
    context = {
        "link": "Персонажи Гарри Поттера в аккордеоне"
    }
    return render_template("main.html")


if __name__ == "__main__":
    app.run()