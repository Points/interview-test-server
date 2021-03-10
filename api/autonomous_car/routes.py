from flask import jsonify
from flask import render_template

from api.autonomous_car import controllers
from app import app


@app.route('/autonomous-car/')
def automated_car_instructions():
    return render_template('autonomous-car.html')


@app.route('/autonomous-car/routes/')
def automated_car_route():
    return jsonify({
        'car_route': controllers.get_reliable_car_route()
    })


@app.route('/autonomous-car/routes/random/')
def random_automated_car_route():
    return jsonify({
        'car_route': controllers.get_unreliable_car_route()
    })
