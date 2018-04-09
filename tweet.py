import helpers

def classify(tweets, positives, negatives):
    """
    classify all tweets in filename
    prints the number of tweets classified as either
    positive / negative / neutral
    """

    # your code goes here
    # TODO

    # print result
    # print("Trump's tweets classified:")
    # print("    positive: {}".format(n_positives))
    # print("    negative: {}".format(n_negatives))
    # print("    neutral : {}".format(n_neutral))

def positive_word(tweets, positives):
    """prints the top 5 most used positive words"""

    # your code goes here
    # TODO

    # consider printing in the following format:
    # Trump's top 5 most used positive words:
    #     amazing 20
    #     awesome 10
    #     fantastic 6
    #     good 5
    #     wow 3

def bad_days(dates, tweets, positives, negatives):
    """
    prints all days that trump
    tweeted more negatively than positively
    """

    # your code goes here
    # TODO

    # consider printing in the following format:
    # Trump's bad days:
    #     20 3 2018
    #     16 2 2018
    #     3 12 2017
    # ...

if __name__ == "__main__":
    # get the dates and tweets from tweet_filename
    dates, tweets = helpers.read_tweets("trump.txt")

    # get the lists of negative and positive words
    positives = helpers.read_words("positive_words.txt")
    negatives = helpers.read_words("negative_words.txt")

    classify(tweets, positives, negatives)
    positive_word(tweets, positives)
    bad_days(dates, tweets, positives, negatives)
