from tqdm import tqdm
from datetime import date
import os
import create
from clean import clean_tweet
import pickle
import organize
from collections import defaultdict
import math



class Author:
    def __init__(self, icpsr, fname, lname, party, state, chamber, district):
        self.tweets = []
        self.accounts = []
        # ICPSR Member ID
        self.icpsr = icpsr
        # First Name
        self.fname = fname
        # Last name
        self.lname = lname
        # D, R, I
        self.party = party
        # NY, CA, FL
        self.state = state
        # H, S
        self.chamber = chamber
        # H: 1; S: ATL (At-Large)
        self.district = district

    def __str__(self):
        return "{}, ({}-{})".format(self.lname + ", " + self.fname, self.party, self.state)

    def __repr__(self):
        return "{}".format(self.icpsr)


class Tweet:
    def __init__(self, tweet, dict_of_authors, dict_of_accounts):
        self.content = ' '.join(clean_tweet(tweet['text']))
        self.account = dict_of_accounts[tweet['screen_name']]
        self.author = dict_of_authors[float(self.account.author.icpsr)]
        self.day = date(int(tweet['time'][0:4]), int(tweet['time'][5:7]), int(tweet['time'][8:10]))
        self.day_in_2020 = (self.day - date(2020, 1, 1)).days + 1

    def __str__(self):
        return self.content

    def __repr__(self):
        return "{} by {} on {}".format(self.content, self.author, self.day)


class Account:
    def __init__(self, author, username, uid):
        self.tweets = []
        self.author = author
        self.username = username
        self.uid = uid

    def __str__(self):
        return self.username

    def __repr__(self):
        return self.uid


def setup(directory_stem, data_folder):
    # set up authors
    if not os.path.isfile('dict_of_authors'):
        dict_of_authors = create.initialize_authors()

        # get tuples of ids and account names
        list_of_raw_tweets = create.get_raw_tweets(directory_stem, data_folder)
        author_tuples = create.get_authors(list_of_raw_tweets)

        # set up accounts
        dict_of_accounts = create.initialize_accounts(author_tuples, dict_of_authors)
        for key, value in dict_of_accounts.items():
            dict_of_authors[float(value.author.icpsr)].accounts.append(value)

        # set up tweets, put tweet in account, put tweet in author
        count = 0
        for tweet in tqdm(list_of_raw_tweets, ascii=True, desc='Reading in tweets', leave=True):
            try:
                if tweet['time'][0:4] == '2020':
                    count += 1
                    tw = Tweet(tweet, dict_of_authors, dict_of_accounts)
                    dict_of_accounts[tweet['screen_name']].tweets.append(tw)
                    dict_of_authors[float(dict_of_accounts[tweet['screen_name']].author.icpsr)].tweets.append(tw)
            except KeyError:
                pass
                # print('Failed')
        with open('dict_of_authors', 'wb') as fp:
            pickle.dump(dict_of_authors, fp)
        with open('dict_of_accounts', 'wb') as fp:
            pickle.dump(dict_of_accounts, fp)
    else:
        dict_of_authors = pickle.load(open('dict_of_authors', 'rb'))
        dict_of_accounts = pickle.load(open('dict_of_accounts', 'rb'))
    return dict_of_authors, dict_of_accounts








if __name__ == '__main__':
    directory_stem = r'C:\Users\ascam\PycharmProjects\congress_tweeter'
    data_folder = 'data'
    dict_of_authors, dict_of_accounts = setup(directory_stem, data_folder)

    # dict_of_authors can be recalled by an author's ICPSR ID number
    # authors have tweets, account handles, first, last name, party, state, chamber, and district
    # tweets have content, author, account, full date, and days since Jan 1 2020
    # accounts have tweets, authors, usernames, and user ids

    # currently implemented: comment out what you need or write new stuff
    # by party (all time)
    # by state (all time)
    # by state and party (all time)
    # by n-week and party
    # change this variable to get a biweekly, n-weekly list
    NUMBER_OF_WEEK_CHUNKS = 1

    # by party
    '''
    partisan_list = organize.party(dict_of_authors)
    list_of_democratic_tweets, list_of_republican_tweets = partisan_list[0], partisan_list[1]
    with open('republicans', 'w', encoding='utf-8') as fp:
        print(*list_of_republican_tweets, sep='\n', file=fp)
    with open('democrats', 'w', encoding='utf-8') as fp:
        print(*list_of_democratic_tweets, sep='\n', file=fp)
    '''

    # by state
    '''
    state_dict = organize.states(dict_of_authors)
    for key, value in state_dict.items():
        with open('{}'.format(key), 'w', encoding='utf-8') as fp:
            print(*value, sep='\n', file=fp)
    '''

    # by week
    '''
    week_dict = defaultdict(list)
    for key, value in dict_of_authors.items():
        for tweet in value.tweets:
            week_dict[math.ceil(tweet.day_in_2020 / (7 * NUMBER_OF_WEEK_CHUNKS))].append(tweet)
    for key, value in week_dict.items():
        dem_tweets = []
        rep_tweets = []
        for tweet in value:
            if tweet.author.party == "R" or tweet.author.party == "L":
                rep_tweets.append(tweet.content)
            if tweet.author.party == "D" or tweet.author.party == "I":
                dem_tweets.append(tweet.content)
        with open('rep_{}'.format(str(key)), 'w', encoding='utf-8') as fp:
            print(*rep_tweets, sep='\n', file=fp)
        with open('dem_{}'.format(str(key)), 'w', encoding='utf-8') as fp:
            print(*dem_tweets, sep='\n', file=fp)
    '''
