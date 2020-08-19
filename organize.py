from collections import defaultdict


def party(dict_of_authors):
    list_of_republican_tweets = []
    list_of_democratic_tweets = []
    for key, value in dict_of_authors.items():
        if value.party == "R":
            for tweet in value.tweets:
                list_of_republican_tweets.append(tweet.content)
        if value.party == "D":
            for tweet in value.tweets:
                list_of_democratic_tweets.append(tweet.content)
        # Amash
        if value.party == "L":
            for tweet in value.tweets:
                list_of_republican_tweets.append(tweet.content)
        # Sanders, King
        if value.party == "I":
            for tweet in value.tweets:
                list_of_democratic_tweets.append(tweet.content)
    return (list_of_democratic_tweets, list_of_republican_tweets)


def states(dict_of_authors):
    states = defaultdict(list)
    for key, value in dict_of_authors.items():
        if value.state == "AL":
            for tweet in value.tweets:
                states['AL'].append(tweet.content)
        if value.state == "AK":
            for tweet in value.tweets:
                states['AK'].append(tweet.content)
        if value.state == "AZ":
            for tweet in value.tweets:
                states['AZ'].append(tweet.content)
        if value.state == "AR":
            for tweet in value.tweets:
                states['AR'].append(tweet.content)
        if value.state == "CA":
            for tweet in value.tweets:
                states['CA'].append(tweet.content)
        if value.state == "CO":
            for tweet in value.tweets:
                states['CO'].append(tweet.content)
        if value.state == "CT":
            for tweet in value.tweets:
                states['CT'].append(tweet.content)
        if value.state == "DE":
            for tweet in value.tweets:
                states['DE'].append(tweet.content)
        if value.state == "FL":
            for tweet in value.tweets:
                states['FL'].append(tweet.content)
        if value.state == "GA":
            for tweet in value.tweets:
                states['GA'].append(tweet.content)
        if value.state == "HI":
            for tweet in value.tweets:
                states['HI'].append(tweet.content)
        if value.state == "ID":
            for tweet in value.tweets:
                states['ID'].append(tweet.content)
        if value.state == "IL":
            for tweet in value.tweets:
                states['IL'].append(tweet.content)
        if value.state == "IN":
            for tweet in value.tweets:
                states['IN'].append(tweet.content)
        if value.state == "IA":
            for tweet in value.tweets:
                states['IA'].append(tweet.content)
        if value.state == "KS":
            for tweet in value.tweets:
                states['KS'].append(tweet.content)
        if value.state == "KY":
            for tweet in value.tweets:
                states['KY'].append(tweet.content)
        if value.state == "LA":
            for tweet in value.tweets:
                states['LA'].append(tweet.content)
        if value.state == "ME":
            for tweet in value.tweets:
                states['ME'].append(tweet.content)
        if value.state == "MD":
            for tweet in value.tweets:
                states['MD'].append(tweet.content)
        if value.state == "MA":
            for tweet in value.tweets:
                states['MA'].append(tweet.content)
        if value.state == "MI":
            for tweet in value.tweets:
                states['MI'].append(tweet.content)
        if value.state == "MN":
            for tweet in value.tweets:
                states['MN'].append(tweet.content)
        if value.state == "MS":
            for tweet in value.tweets:
                states['MS'].append(tweet.content)
        if value.state == "MO":
            for tweet in value.tweets:
                states['MO'].append(tweet.content)
        if value.state == "MT":
            for tweet in value.tweets:
                states['MT'].append(tweet.content)
        if value.state == "NE":
            for tweet in value.tweets:
                states['NE'].append(tweet.content)
        if value.state == "NV":
            for tweet in value.tweets:
                states['NV'].append(tweet.content)
        if value.state == "NH":
            for tweet in value.tweets:
                states['NH'].append(tweet.content)
        if value.state == "NJ":
            for tweet in value.tweets:
                states['NJ'].append(tweet.content)
        if value.state == "NM":
            for tweet in value.tweets:
                states['NM'].append(tweet.content)
        if value.state == "NY":
            for tweet in value.tweets:
                states['NY'].append(tweet.content)
        if value.state == "NC":
            for tweet in value.tweets:
                states['NC'].append(tweet.content)
        if value.state == "ND":
            for tweet in value.tweets:
                states['ND'].append(tweet.content)
        if value.state == "OH":
            for tweet in value.tweets:
                states['OH'].append(tweet.content)
        if value.state == "OK":
            for tweet in value.tweets:
                states['OK'].append(tweet.content)
        if value.state == "OR":
            for tweet in value.tweets:
                states['OR'].append(tweet.content)
        if value.state == "PA":
            for tweet in value.tweets:
                states['PA'].append(tweet.content)
        if value.state == "RI":
            for tweet in value.tweets:
                states['RI'].append(tweet.content)
        if value.state == "SC":
            for tweet in value.tweets:
                states['SC'].append(tweet.content)
        if value.state == "SD":
            for tweet in value.tweets:
                states['SD'].append(tweet.content)
        if value.state == "TN":
            for tweet in value.tweets:
                states['TN'].append(tweet.content)
        if value.state == "TX":
            for tweet in value.tweets:
                states['TX'].append(tweet.content)
        if value.state == "UT":
            for tweet in value.tweets:
                states['UT'].append(tweet.content)
        if value.state == "VT":
            for tweet in value.tweets:
                states['VT'].append(tweet.content)
        if value.state == "VA":
            for tweet in value.tweets:
                states['VA'].append(tweet.content)
        if value.state == "WA":
            for tweet in value.tweets:
                states['WA'].append(tweet.content)
        if value.state == "WV":
            for tweet in value.tweets:
                states['WV'].append(tweet.content)
        if value.state == "WI":
            for tweet in value.tweets:
                states['WI'].append(tweet.content)
        if value.state == "WY":
            for tweet in value.tweets:
                states['WY'].append(tweet.content)
    return states


# Format: Postal Abbr. + Party Letter
def state_and_party(dict_of_authors):
    state_by_party = defaultdict(list)
    for key, value in dict_of_authors.items():
        if value.state == "AL" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['AL'].append(tweet.content)
        if value.state == "AK" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['AK'].append(tweet.content)
        if value.state == "AZ" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['AZ'].append(tweet.content)
        if value.state == "AR" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['AR'].append(tweet.content)
        if value.state == "CA" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['CA'].append(tweet.content)
        if value.state == "CO" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['CO'].append(tweet.content)
        if value.state == "CT" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['CT'].append(tweet.content)
        if value.state == "DE" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['DE'].append(tweet.content)
        if value.state == "FL" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['FL'].append(tweet.content)
        if value.state == "GA" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['GA'].append(tweet.content)
        if value.state == "HI" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['HI'].append(tweet.content)
        if value.state == "ID" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['ID'].append(tweet.content)
        if value.state == "IL" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['IL'].append(tweet.content)
        if value.state == "IN" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['IN'].append(tweet.content)
        if value.state == "IA" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['IA'].append(tweet.content)
        if value.state == "KS" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['KS'].append(tweet.content)
        if value.state == "KY" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['KY'].append(tweet.content)
        if value.state == "LA" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['LA'].append(tweet.content)
        if value.state == "ME" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['ME'].append(tweet.content)
        if value.state == "MD" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['MD'].append(tweet.content)
        if value.state == "MA" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['MA'].append(tweet.content)
        if value.state == "MI" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['MI'].append(tweet.content)
        if value.state == "MN" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['MN'].append(tweet.content)
        if value.state == "MS" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['MS'].append(tweet.content)
        if value.state == "MO" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['MO'].append(tweet.content)
        if value.state == "MT" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['MT'].append(tweet.content)
        if value.state == "NE" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['NE'].append(tweet.content)
        if value.state == "NV" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['NV'].append(tweet.content)
        if value.state == "NH" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['NH'].append(tweet.content)
        if value.state == "NJ" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['NJ'].append(tweet.content)
        if value.state == "NM" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['NM'].append(tweet.content)
        if value.state == "NY" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['NY'].append(tweet.content)
        if value.state == "NC" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['NC'].append(tweet.content)
        if value.state == "ND" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['ND'].append(tweet.content)
        if value.state == "OH" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['OH'].append(tweet.content)
        if value.state == "OK" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['OK'].append(tweet.content)
        if value.state == "OR" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['OR'].append(tweet.content)
        if value.state == "PA" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['PA'].append(tweet.content)
        if value.state == "RI" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['RI'].append(tweet.content)
        if value.state == "SC" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['SC'].append(tweet.content)
        if value.state == "SD" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['SD'].append(tweet.content)
        if value.state == "TN" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['TN'].append(tweet.content)
        if value.state == "TX" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['TX'].append(tweet.content)
        if value.state == "UT" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['UT'].append(tweet.content)
        if value.state == "VT" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['VT'].append(tweet.content)
        if value.state == "VA" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['VA'].append(tweet.content)
        if value.state == "WA" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['WA'].append(tweet.content)
        if value.state == "WV" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['WV'].append(tweet.content)
        if value.state == "WI" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['WI'].append(tweet.content)
        if value.state == "WY" and (value.party == "R" or value.party == "L"):
            for tweet in value.tweets:
                state_by_party['WY'].append(tweet.content)
        if value.state == "AL" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['AL'].append(tweet.content)
        if value.state == "AK" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['AK'].append(tweet.content)
        if value.state == "AZ" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['AZ'].append(tweet.content)
        if value.state == "AR" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['AR'].append(tweet.content)
        if value.state == "CA" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['CA'].append(tweet.content)
        if value.state == "CO" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['CO'].append(tweet.content)
        if value.state == "CT" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['CT'].append(tweet.content)
        if value.state == "DE" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['DE'].append(tweet.content)
        if value.state == "FL" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['FL'].append(tweet.content)
        if value.state == "GA" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['GA'].append(tweet.content)
        if value.state == "HI" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['HI'].append(tweet.content)
        if value.state == "ID" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['ID'].append(tweet.content)
        if value.state == "IL" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['IL'].append(tweet.content)
        if value.state == "IN" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['IN'].append(tweet.content)
        if value.state == "IA" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['IA'].append(tweet.content)
        if value.state == "KS" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['KS'].append(tweet.content)
        if value.state == "KY" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['KY'].append(tweet.content)
        if value.state == "LA" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['LA'].append(tweet.content)
        if value.state == "ME" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['ME'].append(tweet.content)
        if value.state == "MD" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['MD'].append(tweet.content)
        if value.state == "MA" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['MA'].append(tweet.content)
        if value.state == "MI" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['MI'].append(tweet.content)
        if value.state == "MN" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['MN'].append(tweet.content)
        if value.state == "MS" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['MS'].append(tweet.content)
        if value.state == "MO" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['MO'].append(tweet.content)
        if value.state == "MT" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['MT'].append(tweet.content)
        if value.state == "NE" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['NE'].append(tweet.content)
        if value.state == "NV" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['NV'].append(tweet.content)
        if value.state == "NH" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['NH'].append(tweet.content)
        if value.state == "NJ" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['NJ'].append(tweet.content)
        if value.state == "NM" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['NM'].append(tweet.content)
        if value.state == "NY" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['NY'].append(tweet.content)
        if value.state == "NC" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['NC'].append(tweet.content)
        if value.state == "ND" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['ND'].append(tweet.content)
        if value.state == "OH" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['OH'].append(tweet.content)
        if value.state == "OK" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['OK'].append(tweet.content)
        if value.state == "OR" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['OR'].append(tweet.content)
        if value.state == "PA" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['PA'].append(tweet.content)
        if value.state == "RI" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['RI'].append(tweet.content)
        if value.state == "SC" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['SC'].append(tweet.content)
        if value.state == "SD" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['SD'].append(tweet.content)
        if value.state == "TN" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['TN'].append(tweet.content)
        if value.state == "TX" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['TX'].append(tweet.content)
        if value.state == "UT" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['UT'].append(tweet.content)
        if value.state == "VT" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['VT'].append(tweet.content)
        if value.state == "VA" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['VA'].append(tweet.content)
        if value.state == "WA" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['WA'].append(tweet.content)
        if value.state == "WV" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['WV'].append(tweet.content)
        if value.state == "WI" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['WI'].append(tweet.content)
        if value.state == "WY" and (value.party == "D" or value.party == "I"):
            for tweet in value.tweets:
                state_by_party['WY'].append(tweet.content)
    return state_by_party
