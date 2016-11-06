from flask import Flask, render_template
from Medellin import Medellin

app = Flask(__name__)

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index(user=None):
	return render_template("index.html")

@app.route("/medellin")
@app.route("/Medellin")
def medellin():
	return render_template("medellin.html")

@app.route("/medellinLocs", methods=['POST'])
def medellinLocs():
	city = Medellin()
	return city.getDolar()

@app.route("/medellinTrm", methods=['POST'])
def medellinTrm():
	city = Medellin()
	return city.getTrm()

if __name__ == '__main__':
	app.run(debug=True)