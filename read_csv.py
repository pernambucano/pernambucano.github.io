# -*- coding: UTF-8 -*-
import csv
import sys
import itertools
import pprint
from json import dumps, load

theDict = {}



def getting_users():
    users = []
    mDictPart = []
    counter = 0
    with open('contra_e_a_favor_dilma.csv', 'r') as f, open('retweets.json', 'w') as cd:
        reader = csv.reader(f)

        for row in reader:
            if counter >= 234:
                group = 2
            else:
                group = 1
            
            first_item = row[0]
            second_item = row[1]
            if first_item not in users:

                intDict = {}
                intDict["name"] = first_item
                intDict["group"] = group
                users.append(first_item)
                intDict["posicao"] = counter
                mDictPart.append(intDict)
                counter += 1

            elif second_item not in users:

                intDict = {}
                intDict["name"] = second_item
                intDict["group"] = group
                intDict["posicao"] = counter
                users.append(second_item)
                mDictPart.append(intDict)
                counter += 1


        pp = pprint.PrettyPrinter(indent=4)

        myDict = {}
        myDict["nodes"] = mDictPart
        # pp.pprint(myDict)
        cd.write(dumps(myDict, cd, indent=4))
        
        return users, myDict



def replacing_users_with_location(myDict):

    with open('contra_e_a_favor_dilma.csv', 'r') as input_file, open('output_file1.csv', 'w') as output_file:
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)


        for d in reader:
                
            for row in myDict["nodes"]:
                if row["name"] == d[0] or row["name"] == d[1]:
                    index = d.index(row["name"])
                    d[index] = row["posicao"]
                    newrow = d
                    writer.writerow(newrow)

    with open('output_file1.csv', 'r') as input_file, open('output_file2.csv', 'w') as output_file:
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)


        for d in reader:
                
            for row in myDict["nodes"]:
                if row["name"] == d[0] or row["name"] == d[1]:
                    index = d.index(row["name"])
                    d[index] = row["posicao"]
                    newrow = d
                    writer.writerow(newrow)
                    


def create_json_links():
    with open('output_file2.csv', 'r') as input_data, open('links.json', 'w') as output_data:
        reader = csv.reader(input_data)
        writer = csv.writer(output_data)

        mDict = {}

        links = []
        for d in reader:
            mInternalDict = {}
            mInternalDict["source"] = int(d[0])
            mInternalDict["target"] = int(d[1])
            mInternalDict["value"] = 1
            links.append(mInternalDict)

        mDict["links"] = links
        output_data.write(dumps(mDict, output_data, indent=4))



def count_repetition():
    with open('output_file2.csv', 'r') as input_data, open('result_wo_rep.csv', 'w') as output_data:
        reader = csv.reader(input_data)
        writer = csv.writer(output_data)
    
        seen = set() # set for fast O(1) amortized lookup
        for line in input_data:
            if line in seen: continue # skip duplicate

            seen.add(line)
            output_data.write(line)
            
        
    
    
users, mDict = getting_users()
replacing_users_with_location(mDict)
create_json_links()
# count_repetition()


    # with open("pro_dilma.json", "w") as file:
    #     file.write(dumps(myDict, file, indent=4))
