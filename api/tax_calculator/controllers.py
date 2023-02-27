import random
from api.utils import naptime
from .tax_brackets import get_tax_brackets


def get_reliable_brackets():
    return get_tax_brackets()


def get_unreliable_brackets(tax_year):
    naptime()

    # be evil
    roulette = random.randint(1, 4)
    print(f'Database roulette {roulette}')
    if roulette == 3:
        raise Exception("Database not found!")

    return get_tax_brackets(tax_year)
    