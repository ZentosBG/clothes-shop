from flask import Flask, render_template, request, flash 
from sql_queries import *
from config import *
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route("/")
def index():
    category_list = get_categorys()
    items = get_ofers()
    return render_template("index.html", category_list = category_list, items = items)

@app.route("/category/<id>")
def category(id):
    items = get_category_items(id)
    category_list = get_categorys()
    category = get_category_name(id)[0].upper()
    return render_template("category.html",category_list=category_list,category=category, items=items)

@app.route("/item/<item_id>")
def item(item_id):
    item = get_item(item_id)
    category_list = get_categorys()
    return render_template("item.html",category_list=category_list, item=item)

@app.route("/order/<item_id>", methods=["POST", "GET"])
def new_order(item_id):
    category_list = get_categorys()
    if request.method == "POST":
        try:
            add_order(item_id, request.form['name'],request.form['phone'],request.form['email'],request.form['city'],request.form['address'],request.form['amount'] )
            flash("Замовлення відправленно", "alert-success")
        except:
            flash("Помилка відправленння замовлення", "alert-danger")
            
    return render_template("order.html",category_list=category_list)

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True  # автоматичне оновлення шаблонів
    app.run(debug=True)