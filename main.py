from flask import Flask, render_template, request, make_response, url_for, redirect


app = Flask(__name__)
app.config["SECRET_KEY"] = "jfjfjf"


@app.route("/")
def home():
    return render_template("test.html")


if __name__ == "__main__":
    app.run("127.0.0.1", 5000, debug=True)
