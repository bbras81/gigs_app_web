from flask import Flask, render_template
import db
db.main()
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/clients")
def clients():
    return render_template("clients.html")



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)