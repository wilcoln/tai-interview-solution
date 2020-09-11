import nltk
import yake

# Téléchargement de l'utilitaire de découpage de text
nltk.download('punkt')


def nbCharacters(str) -> int:
    """Renvoie le nombre de caractères de la chaîne de caractères UTF-8
        En python3 toutes les chaines de caractères sont encodées en UTF-8
        (voir https://stackoverflow.com/questions/4182603/how-to-convert-a-string-to-utf-8-in-python),
        Il suffit donc juste de renvoyer la longueur de la chaine passée en argument.
        Args:
            str: La chaine de caractère dont on veut la longueur.
        Returns:
            La longueur de la chaine `str`
    """

    return len(str)


def nbWords(str) -> int:
    """Renvoie le nombre de mots dans une chaine de caractères.
        Args:
            str: La chaine de caractère dont on veut le nombre de mots.
        Returns:
            Le nombre de mots de la chaine `str`
    """

    # Récupération de la liste de mots du texte
    words = tokenize(str)
    return len(words)


def occurrences(text) -> dict:
    """Effectue un mapping mot -> nombre d'occurence du mot.
        Args:
            text:
                Le text sur lequel on veut effectuer notre mapping.
        Returns:
                Une table d’association (dictionnaire) dont la clé est le mot
                et la valeur le nombre d’occurrences du mot dans le texte passé enparamètre.
    """

    # Récupération de la liste de mots du texte
    words = tokenize(text)
    # Elimination des doublons
    unique_words = list(dict.fromkeys(words))

    return {word: occurrence(word, text) for word in unique_words}


def tokenize(str) -> list:
    """Renvoie la liste de mots du texte français passé en argument.
        Args:
            str: Le text dont on veut la liste de mots
        Returns:
            Une liste de mots
    """

    # Création d'un tokenizer pour la langue française.
    french_tokenizer = nltk.RegexpTokenizer(r'''^\w'|\w+|[^\w\s]|\w-''')
    # Génération du tableau de tokens
    tokens = french_tokenizer.tokenize(str)
    # Filtrage sur les tokens qui sont des mots (on ignore les ponctuations)
    words = [word.lower() for word in tokens if word.isalnum()]
    return words


def occurrence(word, text) -> int:
    """Renvoie le nombre d'occurence d'un mot dans un texte.

            Args:
                word: Le mot dont on veut le nombre d'occurence

            Returns:
                Le nombre d'occurence du mot `word` dans le texte `text`
    """
    words = tokenize(text)
    return words.count(word)


def extractKeywords(text, nb_keywords) -> list:
    language = "fr"
    max_ngram_size = 1  # nous voulons un mot par expression clé, pas plus.

    french_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, top=nb_keywords)
    extracted_keywords = french_kw_extractor.extract_keywords(text)

    return [{'keyword': word, 'relevance': score} for word, score in extracted_keywords]
