import os
import json
from tqdm import tqdm
import pickle

# Changing directory, change to fit as per your directory structure.
os.chdir("../Dataset/")
print(os.path.abspath(os.curdir))


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


RequiredAspects = {'location', 'service', 'value',
                   'rooms', 'sleep quality', 'cleanliness'}

Records = 0
Unique_Hotels = set()
ExceptionCount = 0

with open("HotelRec.txt", 'r') as file1:
    with open("FetchedRecords.txt", 'w') as file2:
        for line in tqdm(file1, total=50264531):
            line_dict = json.loads(line)
            aspects = set(key for key in line_dict["property_dict"])

            if aspects == RequiredAspects:
                try:
                    review = getUseful(line_dict)
                    Records += 1
                    Unique_Hotels.add(review['name'])
                    output = json.dumps(review) + '\n'
                    file2.write(output)
                except Exception as e:
                    print("Exception caught : ", e)
                    ExceptionCount += 1
                    continue


with open('UniqueHotels.pkl', 'wb') as file:
    pickle.dump(Unique_Hotels, file)

print("Exceptions hit: ", ExceptionCount)
print("Total Records Saved: ", Records)
print("Unique Hotels: ", len(Unique_Hotels))
