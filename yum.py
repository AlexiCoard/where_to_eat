# coding: utf-8

import csv
import datetime
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


def find_last_visited_restaurants(number_of_restaurant_to_keep):
    """Find the last visited restaurant ids

    :param number_of_restaurant_to_keep: [int] you cannot return to the last x restaurants
    :return:
        List[int] The restaurants ids
    """
    with open(HISTORY_FILE, 'r+') as visited_restaurants:
        full_history = visited_restaurants.readlines()
        last_five_restaurants = full_history[-number_of_restaurant_to_keep:]
        restaurant_ids = []
        for restaurant in last_five_restaurants:
            restaurant_ids.append(int(restaurant.split(';')[1]))
        return restaurant_ids


def find_one_restaurant(black_listed_ids):
    """Find one restaurant which is not in the blacklist

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


restaurants = [
    Restaurant(1, "Take N Eat", "La petite tarte au chocolat"),
    Restaurant(2, "Take Away", "Le fameux burger vagintarien"),
    Restaurant(3, "Noii", "On prononce Nouye ou Noye"),
    Restaurant(4, "Pad Thai", "Si la serveuse comprend la commande"),
    Restaurant(5, "Sushi", "Sans aucun sushi.... Philosophie !!!! Hakuna Matata"),
    Restaurant(6, "Petit Japon", "La valeur sûre"),
    Restaurant(7, "Chinois", "Je nem pas ça"),
    Restaurant(8, "Pizza", "Nique la pizza Hawaïenne"),
    Restaurant(9, "Subway", "Les petits cookies Macadamia"),
    Restaurant(10, "Burger King", "Ils ont la même agence de pub que nous, c'est des copains"),
    Restaurant(11, "Voyou", "Sauce Dallas"),
    Restaurant(12, "Five Guys", "LES FRITES"),
    Restaurant(13, "Joffre", "Un ptit plat du jour"),
    Restaurant(14, "Schindler ou Paul", "Un p'tit sandwich"),
    Restaurant(15, "Made in France", "Désespoir"),
    Restaurant(16, "Biscotto", "C'est loin St Epvre"),
    Restaurant(17, "Rice and Curry", "Rip ton slibard ce soir"),
]

"""
    MAIN
"""

parser = ArgumentParser()
parser.add_argument("-l", "--limit", default=NUMBER_OF_VISITED_RESTAURANTS_TO_KEEP,
                    help="Remove the X last visited restaurants")
args = parser.parse_args()

print('Looping over {} restaurants...'.format(len(restaurants)))

already_visited_restaurants = find_last_visited_restaurants(int(args.limit))

the_choosen_one = find_one_restaurant(already_visited_restaurants)

print("On va manger {}. {}".format(the_choosen_one.name, the_choosen_one.comment))
