from flask import jsonify
from flask import render_template

from api.autonomous_car import controllers
from app import app


@app.route('/autonomous-car/')
def automated_car_instructions():
    return render_template('autonomous-car.html')


@app.route('/autonomous-car/routes/empty-route/')
def get_empty_car_route():
    return jsonify({
        'route': controllers.get_reliable_car_route('empty-route')
    })


@app.route('/autonomous-car/routes/success-no-obstacles/')
def get_successful_car_route():
    return jsonify({
        'route': controllers.get_reliable_car_route('success-no-obstacles')
    })


@app.route('/autonomous-car/routes/success-with-obstacles/')
def get_successful_car_route_with_obstacles():
    return jsonify({
        'route': controllers.get_reliable_car_route('success-with-obstacles')
    })


@app.route('/autonomous-car/routes/failure-out-of-bounds/')
def get_failure_car_route():
    return jsonify({
        'route': controllers.get_reliable_car_route('failure-out-of-bounds')
    })


@app.route('/autonomous-car/routes/failure-hits-obstacle/')
def get_failure_car_route_with_obstacles():
    return jsonify({
        'route': controllers.get_reliable_car_route('failure-hits-obstacle')
    })


@app.route('/autonomous-car/routes/random/')
def get_random_car_route():
    return jsonify({
        'route': controllers.get_unreliable_car_route()
    })
