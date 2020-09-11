import unittest

from nlp import nlp


class TestNbCharacters(unittest.TestCase):

    def test_with_valid_data(self):
        text = 'wilfried'
        self.assertEqual(nlp.nbCharacters(text), 8)


class TestNbWords(unittest.TestCase):

    def test_simple(self):
        text = 'Tous les hommes sont mortels'
        # ['Tous', 'les', 'hommes', 'sont', 'mortels']
        self.assertEqual(nlp.nbWords(text), 5)

    def test_avec_ponctuation_simple(self):
        text = 'Tous les hommes sont mortels.'
        # ['Tous', 'les', 'hommes', 'sont', 'mortels']
        self.assertEqual(nlp.nbWords(text), 5)

    def test_avec_ponctuation(self):
        text = "Vas-tu à l'hopital?"
        # ['Vas', 'tu', 'à', 'l', 'hopital']
        self.assertEqual(nlp.nbWords(text), 5)


class TestOccurences(unittest.TestCase):

    def test_un(self):
        text = 'Tous les hommes sont mortels'
        expected_output = {
            'tous': 1,
            'les': 1,
            'hommes': 1,
            'sont': 1,
            'mortels': 1,
        }
        self.assertEqual(nlp.occurrences(text), expected_output)

    def test_deux(self):
        text = 'ho ho, la la la la le le le'
        expected_output = {
            'ho': 2,
            'la': 4,
            'le': 3,
        }
        self.assertEqual(nlp.occurrences(text), expected_output)


class TestExtractKeyWords(unittest.TestCase):

    def test_simple(self):
        text = """
        La France est un pays attachant avec de magnifiques monuments et une savoureuse gastronomie. 
        C'est pourquoi parler français lors de ses voyages ou pour nouer des relations professionnelles demeure un vrai plus !
        En France, il y a au total 11 fêtes pendant l’année. Ce sont des jours fériés, c’est-à-dire des jours pendant lesquels on
        ne travaille pas. Certaines fêtes sont civiles et d’autre sont d’origine religieuses. Voici les principales. Le jour de l’An
        correspond au 1 janvier. On le fête avec ses amis ou sa famille, et on souhaite « bonne année ! » à ses proches. Le 14 juillet
        est la fête nationale française. Elle célèbre la prise de la Bastille qui a eu lieu le 14 juillet 1789. Des feux d’artifices 
        et des défilés militaires sont organisés. Le 8 mai est la fête de la Victoire. C’est la commémoration, c’est-à-dire la fête 
        anniversaire, de la fin de la Seconde Guerre mondiale. Le 1er mai correspond à la fête du Travail, et rappelle la lutte des
        ouvriers pour réduire la journée de travail à huit heures. Ce jour-là, on offre traditionnellement du muguet, une petite 
        fleur blanche, à ses proches. Noël a lieu le 25 décembre. C’est une fête chrétienne qui célèbre la naissance de Jésus.
        """""
        expected_output = [
            {'keyword': 'france', 'relevance': 0.06258802836742607},
            {'keyword': 'fête', 'relevance': 0.0709559128934118},
            {'keyword': 'gastronomie', 'relevance': 0.16601451526587843},
            {'keyword': 'pays', 'relevance': 0.1846637908731856}
        ]

        self.assertEqual(nlp.extract_keywords(text, nb_keywords=4), expected_output)
