import pprint
from flask import Flask, render_template, url_for, redirect

from cupcakes import get_cupcakes, find_cupcake, add_cupcake_dictionary, get_total, del_cupcake, minus_from_quan, add_to_quan

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/menu")
def menu():
    return render_template("menu.html", cupcakes = get_cupcakes("CSVs\menu.csv"))

@app.route("/menu/<name>")
def menu_single(name):
    cupcake = find_cupcake("CSVs/menu.csv", name)
    
    if cupcake:
        sprinkles = cupcake['sprinkles'].strip("[]''")
        sprinkles = sprinkles.split("', '")
        
        return render_template("menu_single.html", cupcake=cupcake, sprinkles = sprinkles)
    else:
        return "Sorry cupcake not found."

@app.route("/order_add/<name>")
def add_cupcake(name):
    cupcake = find_cupcake("CSVs/menu.csv", name)
    
    if cupcake: 
        add_cupcake_dictionary("CSVs/order.csv", cupcake=cupcake)
        return redirect(url_for("menu"))
    else: 
        return "Sorry cupcake not found."
    
@app.route("/order_del/<name>")
def delete_cupcake(name):
    del_cupcake("./CSVs/order.csv", name)
    return redirect(url_for("order"))
    
@app.route("/add_quan/<name>")
def add_quantity(name):
    add_to_quan("CSVs/order.csv", name)
    return redirect(url_for("order"))
    
@app.route("/minus_quan/<name>")
def minus_quantity(name):
    minus_from_quan("CSVs/order.csv", name)
    return redirect(url_for("order"))
    

@app.route("/order")
def order():
    return render_template("order.html", order = get_cupcakes("CSVs/order.csv"), total = get_total("CSVs/order.csv"))


if __name__ == "__main__":
    app.run(debug = True, port = 8000, host = "localhost")
    
