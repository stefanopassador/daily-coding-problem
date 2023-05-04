"""
Problem - Medium

You are given a list of (website, user) pairs that represent users visiting websites. Come up with a program that identifies the top k pairs of websites with the greatest similarity.

For example, suppose k = 1, and the list of tuples is:

[('a', 1), ('a', 3), ('a', 5),
 ('b', 2), ('b', 6),
 ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5)
 ('d', 4), ('d', 5), ('d', 6), ('d', 7),
 ('e', 1), ('e', 3), ('e': 5), ('e', 6)]
Then a reasonable similarity metric would most likely conclude that a and e are the most similar, so your program should return [('a', 'e')].
"""

websites = [
    ('a', 1), ('a', 3), ('a', 5), 
    ('b', 2), ('b', 6), 
    ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5), 
    ('d', 4), ('d', 5), ('d', 6), ('d', 7), 
    ('e', 1), ('e', 3), ('e', 5), ('e', 6)]

k = 2

def find_similarity(l, k):
    # obtain a dict with keys the websites and with values the users visited
    d = {}
    for item in websites:
        website = item[0]
        user = item[1]
        if website not in d:
            d[website] = []
        if user not in d[website]:
            d[website].append(user)

    # give a score to each couple of websites by counting the intersecting users
    couples = {}
    for i in range(0, len(d.keys())):
        for j in range(0, len(d.keys())):
            if i < j:
                a = list(d.keys())[i]
                b = list(d.keys())[j]
                set_a = set(d[a])
                set_b = set(d[b])
                couples[(a,b)] = (len(set_a.intersection(set_b)), -len(set_a.symmetric_difference(set_b)))
        
    # return the k-higher couples
    sorted_couples = {k: v for k, v in sorted(couples.items(), key=lambda item: item[1], reverse=True)}
    res = []
    for i in range(0, k):
        key = list(sorted_couples.keys())[i]
        res.append(key)

    return res

if __name__ == '__main__':
    print(find_similarity(websites, k))