"""Ce module contient le code du serveur de l'api.
Il s'articule principalement en trois parties:
    1. Définition des contrôleurs pour les fonctions.
    2. Définition des routes l'api (endpoints).
    3. Lancement du serveur.
"""

from flask import Flask
from flask_restful import Resource, Api, request, reqparse

from nlp import nlp

app = Flask(__name__)
api = Api(app)

#
# Définition des contrôleurs
#
class FunctionResource(Resource):
    """."""

    def __init__(self):
        self.args = None

    def get(self):
        self.args = request.args
        return self.respond()

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('text', required=True)
        self.args = parser.parse_args()
        return self.respond()


class NbCharacters(FunctionResource):
    def respond(self):
        data = self.args['text']
        return {
            'text': data,
            'output': nlp.nbCharacters(data),
        }


class NbWords(FunctionResource):
    """Contrôleur API pour la fonction `nlp.nbWords`. """

    def respond(self):
        data = self.args['text']
        return {
            'input': data,
            'output': nlp.nbWords(data),
        }


class Occurrences(FunctionResource):
    """Contrôleur API pour la fonction `nlp.occurrences`. """

    def respond(self):
        data = self.args['text']
        return {
            'input': data,
            'output': nlp.occurrences(data),
        }


class ExtractKeyWords(FunctionResource):
    """Contrôleur API pour la fonction `nlp.extractKeywords`. """

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('text', required=True)
        # On ajoute un nouveau paramètre pour le nombre de mots clés.
        parser.add_argument('nb_keywords', type=int, required=True)
        self.args = parser.parse_args()
        return self.respond()

    def respond(self):
        text = self.args['text']
        nb_keywords = self.args['nb_keywords']

        return {
            'input': {'text': text, 'nb_keywords': nb_keywords},
            'output': nlp.extractKeywords(text, nb_keywords=nb_keywords),
        }


#
# Définition des routes de l'api (endpoints)
#

api.add_resource(NbCharacters, '/nb-characters/')
api.add_resource(NbWords, '/nb-words/')
api.add_resource(Occurrences, '/occurrences/')
api.add_resource(ExtractKeyWords, '/extract-keywords/')

#
# Lancement du serveur
#

if __name__ == '__main__':
    app.run(debug=True)