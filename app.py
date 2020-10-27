import random
import time
from flask import Flask, jsonify, render_template
from flask_cors import CORS

from api.error_handlers import format_error
from api.tax_calculator import (
    get_tax_brackets
)

app = Flask(__name__)
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


def naptime():
    sleep_time = random.randint(0, 5)
    time.sleep(sleep_time)


@app.route('/tax-calculator/brackets')
def default_brackets():
    tax_brackets = get_tax_brackets()

    return jsonify({'tax_brackets': tax_brackets})


@app.route('/tax-calculator/brackets/<tax_year>')
def tax_year_brackets(tax_year):

    naptime()

    # be evil
    roulette = random.randint(1, 3)
    print(f'Database roulette {roulette}')
    if roulette == 3:
        raise Exception("Database not found!")

    tax_brackets = get_tax_brackets(tax_year)

    return jsonify({'tax_brackets': tax_brackets})