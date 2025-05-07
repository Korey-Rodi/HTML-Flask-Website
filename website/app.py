from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route("/")
def Welcome():
    return render_template("index.html")

@app.route('/signup', methods=["GET", "POST"])
def SignUp():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        data = open("UserLog.txt", "w")
        data.write("username: " + username + "password: " + password)
        return redirect(url_for("ThankYou"))
    
    return render_template('SignUpPage.html')

@app.route("/thankyou")
def ThankYou():
    return render_template("ThankYouPage.html")

if __name__ == "__main__":
    app.run(debug=True)