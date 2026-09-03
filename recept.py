from ingredient import Ingredient


class Recept:
    def __init__(self, naam, omschrijving):
        self.__naam = naam
        self.__omschrijving = omschrijving
        self.__ingredient_list = []
        self.__stappen_list = []

    def voeg_ingredient_toe(self, ingredient: Ingredient):
        self.__ingredient_list.append(ingredient)

    def get_ingredienten(self):
        return self.__ingredient_list

    def get_naam(self):
        return self.__naam

    def voeg_stap_toe(self, stap):
        self.__stappen_list.append(stap)

    def __str__(self):
        return f"{self.__naam} ({self.__omschrijving})"