from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

print(__name__)

@app.route("/")
def home():
    random_number = random.randint(1,10)
    date = datetime.datetime.now()
    year = date.year
    return render_template("index.html",num=random_number, year=year)

@app.route("/guess/<name>")
def guess(name):
    name = name.title()

    params = {
        "name": name,
    }

    response = requests.get(url="https://api.genderize.io/", params=params)
    # response = requests.get(url="https://api.genderize.io?name={name} ##also works without parameters   print(response.status_code)
    response.raise_for_status()
    gender = response.json()['gender']

    response = requests.get(url="https://api.agify.io/", params=params)
    print(response.status_code)
    response.raise_for_status()
    age = response.json()['age']
    return render_template("guess.html",name=name, gender=gender, age=age)

@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/ebecfbcabaa041b3c155"
    response = requests.get(blog_url)
    all_posts = response.json()
    print(all_posts)
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)