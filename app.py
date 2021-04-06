import random
import time
from flask import Flask, jsonify, render_template
from flask_cors import CORS

from api.error_handlers import format_error
from api.tax_calculator.controllers import (
    get_tax_brackets
)


app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

CORS(app)

@app.errorhandler(404)
def not_found_handler(e):
    return jsonify({
        'errors': format_error(
            'That url was not found',
            code='NOT_FOUND'
        )
    }), 404


@app.errorhandler(Exception)
def exception_handler(e):
    return jsonify({
        'errors': format_error(str(e), code='INTERNAL_SERVER_ERROR')
    }), 500


@app.route('/')
def instructions():
    return render_template('instructions.html')


from api.tax_calculator.routes import *
from api.autonomous_car.routes import *
