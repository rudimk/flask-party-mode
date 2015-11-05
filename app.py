from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index_view():
	return render_template('index.html')


if __name__ == '__main__':
	app.run(port=8100)