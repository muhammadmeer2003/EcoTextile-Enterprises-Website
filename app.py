from flask import Flask, render_template

app = Flask(__name__)

app.config["SECRET_KEY"] = "EcoTextile_Website_Secret_Key_2026"

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return "About EcoTextile - Coming Soon"


@app.route("/features")
def features():
    return "Features - Coming Soon"


@app.route("/tutorials")
def tutorials():
    return "Tutorials - Coming Soon"


@app.route("/documentation")
def documentation():
    return "Documentation - Coming Soon"


@app.route("/support")
def support():
    return "Support Center - Coming Soon"


@app.route("/contact")
def contact():
    return "Contact - Coming Soon"


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5050,
        debug=True
    )