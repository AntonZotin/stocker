import os
import logging

from flask import Flask

# Change the format of messages logged to Stackdriver
logging.basicConfig(format='%(message)s', level=logging.INFO)

app = Flask(__name__)


@app.route('/')
def home():
	try:
		import stocker
		return 'hi'
		s = stocker.predict.tomorrow('AAPL')
		res = f'Result for {s[2]} {s[0]}'
		return res
	except Exception as e:
		logging.error(e)
		return str(e)


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
