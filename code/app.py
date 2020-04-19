from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://cdn2.thecatapi.com/images/30.gif",
    "https://cdn2.thecatapi.com/images/29.gif",
    "https://cdn2.thecatapi.com/images/28.gif",
    "https://cdn2.thecatapi.com/images/27.gif",
    "https://cdn2.thecatapi.com/images/26.gif",
    "https://cdn2.thecatapi.com/images/25.gif",
    "https://cdn2.thecatapi.com/images/24.gif",
    "https://cdn2.thecatapi.com/images/23.gif",
    "https://cdn2.thecatapi.com/images/22.gif",
    "https://cdn2.thecatapi.com/images/21.gif",
    "https://cdn2.thecatapi.com/images/20.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
