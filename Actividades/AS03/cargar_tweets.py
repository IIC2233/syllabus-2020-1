from collections import namedtuple


def cargar_tweets(path):
    """
    Carga los tweets del archivo entregado en path
    Este archivo tiene el formato enojo;texto
    Retorna una lista de namedtuples
    """
    Tweet = namedtuple("Tweet", ['enojo', 'texto'])
    tweets = []

    with open(path, 'r', encoding='utf-8') as archivo:
        for line in archivo.readlines()[1:]:
            line = line.rstrip().split(';')
            tweet = Tweet(int(line[0]), line[1])
            tweets.append(tweet)
    return tweets
