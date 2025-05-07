from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route("/")
def Welcome():
    return render_template("index.html")

@app.route('/signup')
def SignUp():
    return render_template('SignUpPage.html')

if __name__ == "__main__":
    app.run(debug=True)