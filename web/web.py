from datetime import *
from flask import *
import mlab
from models.images import Image

app = Flask(__name__)
mlab.connect()

@app.route('/')
def hello_world():
    return redirect(url_for("foodblog"))

number_of_visitor = 0

@app.route('/login')
def login():
    current_time_on_server = str(datetime.now())
    global number_of_visitor
    number_of_visitor += 1

    return render_template("login.html", current_time=current_time_on_server, number_of_visitor_1=number_of_visitor)

@app.route('/food')
def food():
    return render_template("food.html", list_food = Image.objects())

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route('/css')
def css():
    return render_template("css_demo.html")

@app.route('/w3css')
def w3css():
    return render_template("w3css.html")

@app.route('/add_image', methods=["GET", "POST"])
def add():
    if(request.method == "GET"):
        return render_template("add_image.html")
    if(request.method == "POST"):
        new_image = Image()
        new_image.src = request.form["source"]
        new_image.title = request.form["title"]
        new_image.description = request.form["description"]
        new_image.save()
        return render_template("add_image.html")

@app.route('/delete_image', methods=["GET", "POST"])
def delete():
    if(request.method == "GET"):
        return render_template("delete_image.html")
    if(request.method == "POST"):
        new_image = Image.objects(title=request.form["title"]).first()
        if new_image is not None:
            new_image.delete()
        return render_template("delete_image.html")

@app.route('/update_image', methods=["GET", "POST"])
def update():
    if (request.method == "GET"):
        return render_template("update_image.html")
    if (request.method == "POST"):
        new_image = Image.objects(title=request.form["title"]).first()
        if new_image is not None:
            new_image.src = request.form["new_source"]
            new_image.description = request.form["new_description"]
            new_image.save()
        return render_template("update_image.html")


@app.route('/foodblog')
def foodblog():
    return render_template("foodblog.html", list_food = Image.objects())

if __name__ == '__main__':
    app.run()