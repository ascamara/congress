import tweet
import pandas as pd
import math
import findauthor
import json
from tqdm import tqdm
import os

def initialize_accounts(account_tuples, dict_of_authors):
    dict_of_accounts = {}
    #print([key for key in dict_of_authors])
    for account in account_tuples:
        uid = account[0]
        username = account[1]
        author = findauthor.search(uid, dict_of_authors)
        if author == -1:
            continue
        else:
            dict_of_accounts[username] = tweet.Account(author, username, uid)
    return dict_of_accounts

def initialize_authors():
    dict_of_authors = {}
    df = pd.read_csv('legislators-current.csv', header=0)
    for index, row in df.iterrows():
        icpsr = row['icpsr_id']
        fname = row['first_name']
        lname = row['last_name']
        party = row['party'][0]
        state = row['state']
        if row['type'] == 'rep':
            chamber = 'H'
        elif row['type'] == 'sen':
            chamber = 'S'
        else:
            chamber = 'U'
        if chamber != 'H':
            district = 'ATL'
        else:
            district = row['district']
        if not math.isnan(icpsr):
            dict_of_authors[icpsr] = tweet.Author(icpsr, fname, lname, party, state, chamber, district)
    return dict_of_authors

def get_raw_tweets(directory_stem, data):
    list_of_raw_tweets = []
    for file in tqdm(os.listdir(directory_stem + '\\' + data), ascii=True, desc='Files', leave=True):
        with open(data + '\\' + file, 'r', encoding='utf-8') as f:
            elements = json.load(f)
            for element in elements:
                list_of_raw_tweets.append(element)
    return list_of_raw_tweets

def get_authors(list_of_raw_tweets):
    author_tuples = []
    for tweet in list_of_raw_tweets:
        try:
            pair = (tweet['user_id'], tweet['screen_name'])
            author_tuples.append(pair)
        except KeyError:
            print('Failed')
    return set(author_tuples)