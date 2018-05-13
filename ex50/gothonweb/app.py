from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")

def index():
	greeting = "Learn Python 3 The Hard Way"
	return render_template("index.html", hello=greeting)

if __name__ == "__main__":
	app.run()