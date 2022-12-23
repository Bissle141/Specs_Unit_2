from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/menu-{cupcake}")
def menu_single():
    return render_template("menu_single.html")

@app.route("/order")
def order():
    return render_template("order.html")

if __name__ == "__main__":
    app.run(debug = True, port = 8000, host = "localhost")