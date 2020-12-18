import os

from api import utils

SUPPORTED_TAX_BRACKET_YEARS = [2019, 2020]

BRACKETS_DIRECTORY = os.path.join(os.path.dirname(__file__), 'fixtures')


def get_all_tax_brackets():
    tax_brackets = {}
    for year in SUPPORTED_TAX_BRACKET_YEARS:
        tax_brackets[str(year)] = get_tax_brackets(year)


def get_tax_brackets(tax_year=2020):
    filename = f'tax-brackets-{tax_year}.json'
    file_with_path = os.path.join(BRACKETS_DIRECTORY, filename)
    try:
        return utils.get_json_contents_from_resource_file(file_with_path)
    except FileNotFoundError:
        raise ValueError(
            f'Tax brackets for the year \'{tax_year}\' were not found.'
        )
