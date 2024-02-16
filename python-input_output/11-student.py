#!/usr/bin/python3
"""
Module 11-student.
Définit une classe Étudiant et inclut les méthodes pour sérialiser l'instance
en un dictionnaire, et pour désérialiser un dictionnaire pour mettre à jour
les attributs de l'instance.
"""


class Student:
    """
    Définit un étudiant par `first_name`, `last_name` et `age`, et supporte la
    sérialisation et désérialisation de l'instance.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialise une nouvelle instance de la classe Student.

        Paramètres:
            first_name (str): Le prénom de l'étudiant.
            last_name (str): Le nom de l'étudiant.
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

    def reload_from_json(self, json):
        """
        Met à jour les attributs de l'instance Student à partir d'un\
            dictionnaire.

        Paramètres:
            json (dict): Un dictionnaire où les clés correspondent aux noms
            des attributs à mettre à jour, et les valeurs aux nouvelles valeurs
            des attributs.
        """
        for key, value in json.items():
            setattr(self, key, value)
