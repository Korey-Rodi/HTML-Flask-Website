from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route("/")
def weclome():
    return render_template("WelcomePage.html")




if __name__ == "__main__":
    app.run(debug=True)