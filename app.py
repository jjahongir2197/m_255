from flask import Flask, render_template, request, redirect

app = Flask(__name__)

users = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        users.append(name)
        return redirect("/")

    return render_template("crud.html", users=users)

@app.route("/delete/<name>")
def delete(name):
    users.remove(name)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
