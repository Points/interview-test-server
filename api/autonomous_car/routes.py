from flask import render_template
from app import app


@app.route('/autonomous-car/')
def car_instructions():
    return render_template('autonomous-car.html')
