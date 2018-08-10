from flask import Flask

app = Flask(__name__)

@app.route('/')
def test():
	 return "<a href='test'>salam</a>"

@app.route('/')
def salam():
	 return "SALAM"


if __name__ == '__main__':
	app.run(debug=True)