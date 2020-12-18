from api import utils
from api.tax_calculator import tax_brackets


def get_all_tax_brackets():
    return tax_brackets.get_all_tax_brackets()


def get_reliable_brackets():
    return tax_brackets.get_tax_brackets()


def get_unreliable_brackets(tax_year):
    utils.random_nap_time()
    utils.perform_evil_roulette()  # Be Evil
    return tax_brackets.get_tax_brackets(tax_year)
