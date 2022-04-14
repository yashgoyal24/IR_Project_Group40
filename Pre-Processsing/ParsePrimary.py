
import os
import json
from tqdm import tqdm


os.chdir("../Dataset/")
print(os.path.abspath(os.curdir))

RECORDS = 100000


def getUseful(record):
    review = dict()

    url = record['hotel_url']
    t = url.split('-')
    name, loc = t[4], t[5].split('.')[0]
    review['name'] = name
    review['loc'] = loc
    review['text'] = record['text']
    review['property_dict'] = record['property_dict']

    return review


with open("HotelRec.txt", 'r') as file1:
    with open("Processed.txt", 'a') as file2:

        for _ in tqdm(range(RECORDS)):
            oneline = file1.readline()
            line_dict = json.loads(oneline)

            if len(line_dict["property_dict"]) > 0:
                review = getUseful(line_dict)
                output = json.dumps(review) + '\n'
                file2.write(output)


N = 2
print(f'Reading {N} lines from Precessed.txt')
with open('Processed.txt', 'r') as f:
    for _ in tqdm(range(N)):
        line = f.readline()
        print(line)
        line_dict = json.loads(line)
        print(line_dict['property_dict'])
