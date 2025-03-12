from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return '<a href="/photos">Photos</a>'

@app.route("/photos")
def photos():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)