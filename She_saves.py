from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/calculate', methods=['POST'])
def calculate():
    income = float(request.form['income'])
    expense = float(request.form['expense'])
    savings = income - expense
    if savings > 0:
        message = "✅ Great! You're saving money today!"
    elif savings == 0:
        message = "⚠️ You're breaking even today."
    else:
        message = "❌ You spent more than you earned. Be careful tomorrow!"
    return render_template("result.html", income=income, expense=expense, savings=savings, message=message)

if __name__ == '__main__':
    app.run()
