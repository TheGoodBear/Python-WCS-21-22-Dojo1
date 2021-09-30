"""
    Randomly draw all persons from a list
"""
# coding: utf-8

# imports
import random


# functions
def main():
    """
        Randomly draw all persons from a list
    """

    peoples = [
        "Timothée",
        "Gael",
        "David",
        "Quentin",
        "Théo",
        "Nicolas",
        "Jojo",
        "Jordan",
        "Adrien",
        "Cécilia"]
    number = 1

    while len(peoples) != 0:

        index_random_people = random.randint(0, len(peoples)-1)
        poped_person = peoples.pop(index_random_people)
        start_string = f"{number}ème"
        end_string = f"il reste {len(peoples)} personnes"

        if number == 1:
            start_string = f"{number}er"

        if len(peoples) == 0:
            end_string = "il ne reste plus personne"

        print(f"{start_string} {poped_person} {end_string}")
        number += 1


# code starts here
if __name__ == "__main__":
    main()
