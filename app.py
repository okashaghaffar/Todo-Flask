from flask import Flask,render_template
app = Flask(__name__)
@app.route("/")
def HelloWorld():
    return render_template("index.html")

@app.route("/products")
def Products():
    return "This is product page"


if __name__ == "__main__":
    app.run(debug=True, port=8000)