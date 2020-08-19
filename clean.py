import re
from num2words import num2words
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import decimal


def numberize(w):
    def has_number(tok):
        return bool(re.search(r'\d', tok))

    def ordinal(tok):
        ordins = ['th', 'rd', 'st', 'nd']
        if tok[-2:] in ordins and has_number(tok[-3]):
            return True
        else:
            return False

    def has_letters(tok):
        for t in tok:
            if not has_number(t):
                return True
        return False

    try:
        # normal case - fifty-three
        if has_number(w) and not ordinal(w):
            # if it has letters, let her go (n95, covid19)
            if not has_letters(w):
                w = str(num2words(int(w)))
        # unless its an ordinal!
        elif has_number(w) and ordinal(w):
            w = str(num2words(w[:-2], ordinal=True))
    except decimal.InvalidOperation:
        print('Error: Numberize')
    return w


def lemmatize_and_stem(line):
    lemmatizer = WordNetLemmatizer()
    stemmer = PorterStemmer()
    for w in line:
        try:
            line[line.index(w)] = lemmatizer.lemmatize(w)
            line[line.index(w)] = stemmer.stem(w)
        except ValueError as e:
            continue
    return line


def clean_tweet(tweet):
    clean_tw = []
    tweet = tweet.split()
    for word in tweet:
        if word[0] != "@":
            clean = re.sub(r'^https?:\/\/.*[\r\n]*', '', word, flags=re.MULTILINE)
            clean = re.sub(r'[^\w\s]', '', clean)
            clean = clean.lower()
            clean = numberize(clean)
            stop_words = set(stopwords.words('english'))
            stop_words.update('and')
            if len(clean) > 2 and clean not in stop_words:
                clean_tw.append(clean)
    return clean_tw
