import http

from flask import abort
from flask import jsonify
from flask import render_template

from api.autonomous_car import controllers
from api.autonomous_car import autonomous_car
from app import app


@app.route('/autonomous-car/')
def automated_car_instructions():
    return render_template('autonomous-car.html')


@app.route('/autonomous-car/routes/')
def random_automated_car_route():
    return jsonify({
        'car_route': controllers.get_random_car_route()
    })


@app.route('/autonomous-car/routes/<string:status>/')
def get_automated_car_route(status):
    if status.upper() not in autonomous_car.STATUS_LIST:
        abort(http.HTTPStatus.NOT_FOUND)
    return jsonify({
        'car_route': autonomous_car.get_random_car_route_from_status(status)
    })
