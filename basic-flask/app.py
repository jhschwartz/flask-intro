#!env/bin/python

from flask import Flask

app = Flask(__name__)

@app.route("/hi")
def hi():
	# return hello world here

if __name__ == '__main__':
	app.run()