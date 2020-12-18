from api import utils
from api.autonomous_car import autonomous_car


def get_empty_automated_car_route():
    return autonomous_car.get_empty_route()


def get_random_car_route():
    return autonomous_car.get_random_route()


def get_car_route(status):
    utils.random_nap_time()
    utils.perform_evil_roulette()  # Be Evil
    return autonomous_car.get_random_car_route_from_status(status)