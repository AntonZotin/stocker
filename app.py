import _thread
import os
import time

from flask import Flask, render_template

import stocker

app = Flask(__name__)

data = {}


@app.route('/')
def home():
    return str(stocker.predict.tomorrow('AAPL'))
    res = []
    for date, values in data.items():
        res.append({
            'date': date,
            'min': f'{min(values["values"])} ({min(values["errors"])})',
            'avg': f'{round(sum(values["values"]) / len(values["values"]), 2)} ({round(sum(values["errors"]) / len(values["errors"]), 2)})',
            'max': f'{max(values["values"])} ({max(values["errors"])})'
        })
    return render_template('index.html', data=res)


def get_data():
    s = stocker.predict.tomorrow('AAPL')
    if s[2] in data:
        data[s[2]]['values'].append(s[0])
        data[s[2]]['errors'].append(s[1])
    else:
        data[s[2]] = {'values': [s[0]], 'errors': [s[1]]}
    time.sleep(3600)


if __name__ == '__main__':
    # _thread.start_new_thread(get_data, ())
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
