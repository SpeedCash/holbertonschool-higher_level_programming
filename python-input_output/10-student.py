#!/usr/bin/python3
"""
Module 10-student.
Définit une classe Étudiant et une méthode pour récupérer une représentation
dictionnaire de l'instance Étudiant.
"""


class Student:
    """
    Définit un étudiant par ses attributs `first_name`, `last_name` et `age`.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialise une nouvelle instance de la classe Student.

        Paramètres:
            first_name (str): Le prénom de l'étudiant.
            last_name (str): Le nom de famille de l'étudiant.
            age (int): L'âge de l'étudiant.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Récupère une représentation dictionnaire de l'instance Student.

        Paramètres:
            attrs (list): Liste des attributs à inclure dans le dictionnaire.

        Retourne:
            Un dictionnaire représentant les attributs de l'instance.
        """
        if attrs is not None and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__
