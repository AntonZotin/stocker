# Copyright 2019 Google, LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START app]
import logging

from flask import Flask, render_template

app = Flask(__name__)

# Global list to store messages, tokens, etc. received by this instance.
MESSAGES = []
TOKENS = []
CLAIMS = []


@app.route('/')
def hello():
    return 'hello'
    # try:
    #     import stocker
    #     s = stocker.predict.tomorrow('AAPL')
    #     res = f'Result for {s[2]} {s[0]}'
    #     return res
    # except Exception as e:
    #     return str(e)
# # [START index]
# @app.route('/', methods=['GET'])
# def index():
#     return render_template('index.html', messages=MESSAGES, tokens=TOKENS,
#                            claims=CLAIMS)
# # [END index]


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END app]
