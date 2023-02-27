import os
import json
import http
import flask


brackets_dir = os.path.join(os.path.dirname(__file__), 'fixtures')


def _open_config(filename):

    with open(filename) as config_file:
        json_contents = json.load(config_file)
        config_file.close()

    return json_contents


def get_tax_brackets(tax_year='2022'):
    filename = f'tax-brackets--{tax_year}.json'
    file_with_path = os.path.join(brackets_dir, filename)
    try:
        return _open_config(file_with_path)
    except FileNotFoundError:
        flask.abort(http.HTTPStatus.NOT_FOUND)
