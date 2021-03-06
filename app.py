import os

from flask import Flask, render_template

app = Flask(__name__)


data = {}


@app.route('/<currency>')
def home(currency):
    import stocker
    for i in range(5):
        s = stocker.predict.tomorrow(currency.upper())
        label = f'{s[2]}/{currency.upper()}'
        if label in data and len(data[label]['values']) != 5:
            data[label]['values'].append(float(s[0]))
            data[label]['errors'].append(float(s[1]))
        else:
            data[label] = {'values': [s[0]], 'errors': [s[1]]}
    res = []
    for index, values in data.items():
        res.append({
            'label': index,
            'min': f'{min(values["values"])} ({min(values["errors"])})',
            'avg': f'{round(sum(values["values"]) / len(values["values"]), 2)} ({round(sum(values["errors"]) / len(values["errors"]), 2)})',
            'max': f'{max(values["values"])} ({max(values["errors"])})'
        })
    return render_template('index.html', data=res)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
