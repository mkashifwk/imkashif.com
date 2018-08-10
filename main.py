from flask import Flask

app = Flask(__name__)

@app.route('/')
def test():
	 return "<a href='test'>salam</a>"


if __name__ == '__main__':
	app.run(debug=True)