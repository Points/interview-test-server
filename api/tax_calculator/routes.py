import http

from flask import abort
from flask import jsonify
from flask import render_template

from api.tax_calculator import controllers
from api.tax_calculator import tax_brackets
from app import app


@app.route('/tax-calculator/')
def tax_calculator_instructions():
    return render_template('tax-calculator.html')


@app.route('/tax-calculator/brackets/')
def default_brackets():
    return jsonify({
        'tax_brackets': controllers.get_reliable_brackets()
    })


@app.route('/tax-calculator/brackets/<int:tax_year>/')
def tax_year_brackets(tax_year):
    if tax_year not in tax_brackets.SUPPORTED_TAX_BRACKET_YEARS:
        abort(http.HTTPStatus.NOT_FOUND)
    return jsonify({
        'tax_brackets': controllers.get_unreliable_brackets(tax_year)
    })
