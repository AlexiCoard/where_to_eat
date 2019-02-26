# coding: utf-8

import csv
import datetime
import os
from argparse import ArgumentParser
from random import randint


class Restaurant:
    """
        A simple class to represent a restaurant
    """

    def __init__(self, r_id, name, comment):
        self.id = r_id
        self.name = name
        self.comment = comment


NUMBER_OF_VISITED_RESTAURANTS_TO_KEEP = 5
HISTORY_FILE = 'history.csv'
RESTAURANT_FILE = 'restaurants.csv'


def find_last_visited_restaurants(number_of_restaurant_to_keep):
    """Find the last visited restaurant ids

    :param number_of_restaurant_to_keep: [int] you cannot return to the last x restaurants
    :return:
        List[int] The restaurants ids
    """

    exists = os.path.exists(HISTORY_FILE)
    if not exists:
        open(HISTORY_FILE, 'x')

    with open(HISTORY_FILE, 'r+') as visited_restaurants:
        full_history = visited_restaurants.readlines()
        last_five_restaurants = full_history[-number_of_restaurant_to_keep:]
        restaurant_ids = []
        for restaurant in last_five_restaurants:
            restaurant_ids.append(int(restaurant.split(';')[1]))
        return restaurant_ids


def find_one_restaurant(restaurants, black_listed_ids):
    """Find one restaurant which is not in the blacklist

    :param restaurants: List[Restaurant] Available restaurant list
    :param black_listed_ids: List[int] a blacklist id
    :return: Restaurant
    """
    restaurant_found = False
    loops = 0
    while not restaurant_found:
        if loops > 100:
            raise Exception('Cannot find a suitable restaurant, try to lower the limit')

        index = randint(0, len(restaurants) - 1)
        candidate = restaurants[index]

        if candidate.id not in black_listed_ids:
            with open('history.csv', 'a+', newline='') as history:
                entry = csv.writer(history, delimiter=';')
                today = datetime.date.today()
                entry.writerow([
                    today.strftime('%d-%m'),
                    candidate.id,
                    candidate.name
                ])
            return candidate

        loops += 1


def load_available_restaurants(restaurant_file):
    exists = os.path.exists(restaurant_file)
    if not exists:
        raise Exception('Restaurant file not found')

    with open(restaurant_file, 'r') as file:
        found_restaurants = []
        has_header = csv.Sniffer().has_header(file.read())
        # Reset cursor
        file.seek(0)
        reader = csv.reader(file)
        if has_header:
            next(reader)
        for row in reader:
            elements = row[0].split(';')
            found_restaurants.append(Restaurant(elements[0], elements[1], elements[2]))

        return found_restaurants


"""
    MAIN
"""

parser = ArgumentParser()
parser.add_argument("-l", "--limit", default=NUMBER_OF_VISITED_RESTAURANTS_TO_KEEP,
                    help="Remove the X last visited restaurants")

parser.add_argument("-f", "--file", default=RESTAURANT_FILE,
                    help="Remove the X last visited restaurants")
args = parser.parse_args()

already_visited_restaurants = find_last_visited_restaurants(int(args.limit))

the_choosen_one = find_one_restaurant(load_available_restaurants(args.file), already_visited_restaurants)

print("On va manger {}. {}".format(the_choosen_one.name, the_choosen_one.comment))
