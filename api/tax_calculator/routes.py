from flask import jsonify, render_template, redirect
from app import app
from . import controllers


@app.route('/tax-calculator/')
def tax_calculator_instructions():
    return jsonify({
        'tax_brackets': controllers.get_reliable_brackets()
    })


@app.route('/tax-calculator/tax-year')
def default_brackets():
    return redirect('/')


@app.route('/tax-calculator/tax-year/<tax_year>')
def tax_year_brackets(tax_year):
    return jsonify({
        'tax_brackets': controllers.get_unreliable_brackets(tax_year)
    })
