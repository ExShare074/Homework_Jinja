from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def films():
    context = {
        "title": "Все о персонажах Трансформеров",
    }
    return render_template("home.html", **context)



@app.route("/person/")
def person():
    context = {
        "title": "Все о создателях Трансформеров"
    }
    return render_template("about.html", **context)


if __name__ == "__main__":
    app.run()