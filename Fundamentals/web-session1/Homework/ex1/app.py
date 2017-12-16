from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Body Mass Index</h1>"

@app.route('/bmiwithoutrender/<weight>/<height>')
def bmiwithoutrender(weight, height):
    w = float(weight)
    h = float(height)
    bmi = w/(h**2)
    if bmi < 16:
        result = 'Severely underweight.'
    elif 16 <= bmi < 18.5:
        result = 'Underweight.'
    elif 18.5 <= bmi < 25:
        result = 'Normal.'
    elif 25 <= bmi < 30:
        result = 'Overweight.'
    else:
        result = 'Obese.'
    return '<p>Your weight:</p>' + str(w) + '<p>Your height:</p>' + str(h) + '<p>Your BMI:</p>' + str(bmi) + '<p>Result:</p>' + result

@app.route('/bmiwithrender/<weight>/<height>')
def bmiwithrender(weight, height):
    w = float(weight)
    h = float(height)
    bmi = w/(h**2)
    return render_template('bmi.html', w = w, h = h, bmi = bmi)

if __name__ == '__main__':
  app.run(debug=True)
