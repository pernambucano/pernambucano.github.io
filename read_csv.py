# -*- coding: UTF-8 -*-
import csv
import sys
import itertools
import pprint
from json import dumps, load


users = []
links = []
#
# def getDupes(c):
#         '''sort/tee/izip'''
#         a, b = itertools.tee(sorted(c))
#         next(b, None)
#         r = None
#         for k, g in itertools.izip(a, b):
#             if k != g: continue
#             if k != r:
#                 yield k
#                 r = k

with open('pro_dilma.csv', 'r') as f:
    reader = csv.reader(f)
    counter = 0;
    for row in reader:
        first_item = row[0]
        second_item = row[1]
        if first_item not in users:
            counter += 1
            intDict = {}
            intDict["name"] = first_item
            intDict["group"] = 1
            users.append(intDict)
            intDict["posicao"] = counter

        elif second_item not in users:
            counter += 1
            intDict = {}
            intDict["name"] = second_item
            intDict["group"] = 1
            intDict["posicao"] = counter
            users.append(intDict)

    pp = pprint.PrettyPrinter(indent=4)

    myDict = {}
    myDict["nodes"] = users
    pp.pprint(myDict)




with open('pro_dilma.csv', 'r') as csvfile:

    mreader = csv.reader(csvfile)
    data = csvfile.readlines()

    for u in users:
        name = u["name"]
        for d in data:

            if name in data:
                print (name,data)
                data = ([w.replace(u["name"], str(u["posicao"])) for w in data])

    print data
    # with open("pro_dilma.json", "w") as file:
    #     file.write(dumps(myDict, file, indent=4))
