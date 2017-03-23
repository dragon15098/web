from flask import *
from datetime import *
app = Flask(__name__)

list_food_1 = [
    {
        "arc" : "http://68.media.tumblr.com/fdce8d90185f8f38a5f36a69b198a271/tumblr_ojqkfv1h7c1qbd81ro1_1280.jpg",
        "title" : "12343 by Đinh Văn Linh",
        "tags" : "#girl xinh#pretty girl#vietnam girl#beautiful girl photo#photography"
    },
    {
        "arc" : "http://68.media.tumblr.com/6707567f4007a0ebb6e342f37692da0b/tumblr_of8kzf8gMp1qbd81ro1_1280.jpg",
        "title" : "lightstudio | 0966726996 by Leo White",
        "tags" : "#girl xinh#pretty girl#vietnam girl#beautiful girl photo#photography"
    },
    {
        "arc" : "http://68.media.tumblr.com/b2546075aa96c52eb287b44da313ac29/tumblr_of8kzbVZmv1qbd81ro1_1280.jpg",
        "title" : "DSC_2180 by mrSun_vn",
        "tags" : "#girl xinh#pretty girl#vietnam girl#beautiful girl photo#photography"
    },
    {
        "arc" : "http://68.media.tumblr.com/7111feb3f9b20cadb1fca92d4aaf62f9/tumblr_of8kz3Im0h1qbd81ro1_1280.jpg",
        "title" : "IMG_7340 by Hải Nguyễn | Tell 0902990341",
        "tags" : "#girl xinh#pretty girl#vietnam girl#beautiful girl photo#photography"
    }
    ]

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
    return render_template("food.html", list_food = list_food_1)

@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route('/css')
def css():
    return render_template("css_demo.html")


@app.route('/w3css')
def w3css():
    return render_template("w3css.html")


@app.route('/foodblog')
def foodblog():
    return render_template("foodblog.html")

if __name__ == '__main__':
    app.run()
