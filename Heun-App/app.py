from flask import Flask, render_template, request
from heun_method import heun_method

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/examples')
def examples():
    return render_template('example.html')

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():

    result = None
    steps = []

    if request.method == 'POST':

        equation = request.form['equation']
        x0 = float(request.form['x0'])
        y0 = float(request.form['y0'])
        h = float(request.form['h'])
        target = float(request.form['target'])

        result, steps = heun_method(
            equation,
            x0,
            y0,
            h,
            target
        )

    return render_template(
        'calculator.html',
        result=result,
        steps=steps
    )

if __name__ == '__main__':
    app.run(debug=True)