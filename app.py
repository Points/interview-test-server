import http

from flask import Flask
from flask_cors import CORS

from api.error_handlers import format_error

app = Flask(__name__)
CORS(app)


@app.route('/')
def instructions():
    return render_template('instructions.html')


@app.errorhandler(http.HTTPStatus.NOT_FOUND)
def not_found_handler(e):
    return jsonify({
        'errors': format_error(
            message='That url was not found.',
            code='NOT_FOUND'
        )
    }), http.HTTPStatus.NOT_FOUND


@app.errorhandler(Exception)
def exception_handler(e):
    return jsonify({
        'errors': format_error(
            message=str(e),
            code='INTERNAL_SERVER_ERROR'
        )
    }), http.HTTPStatus.INTERNAL_SERVER_ERROR


from api.tax_calculator.routes import *
from api.autonomous_car.routes import *
