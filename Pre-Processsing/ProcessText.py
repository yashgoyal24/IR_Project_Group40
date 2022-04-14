import os
import re
import string
import nltk

import json
from tqdm import tqdm
from collections import defaultdict
import pickle

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')


# Changing directory, change to fit as per your directory structure.
os.chdir("../Dataset/")
print(os.path.abspath(os.curdir))

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()


def preprocessing(data):
    # Remove numbers
    result = re.sub(r'\d+', '', data)
    # Remove punctuation
    result = result.translate(str.maketrans("", "", string.punctuation))
    # Change to lowercase
    result = result.lower()
    # Remove stop words and tokenize
    tokens = word_tokenize(result)
    tokens = [token for token in tokens if token not in stop_words]
    # Lemmatization
    result = [lemmatizer.lemmatize(token) for token in tokens]

    return ' '.join(result)


def processReview(text):
    sentences = text.split('.')
    processed_sentences = [preprocessing(sentence) for sentence in sentences]
    return '. '.join(processed_sentences) + '.'


Records = 0
ExceptionCount = 0

with open("FetchedRecords.txt", 'r') as inputFile:
    with open("ProcessedText.txt", 'w') as outputFile:
        for line in tqdm(inputFile, total=15697111):
            review = json.loads(line)
            try:
                review['text'] = processReview(review['text'])
                Records += 1
                output = json.dumps(review) + '\n'
                outputFile.write(output)
            except Exception as e:
                print("Exception caught : ", e)
                ExceptionCount += 1
                continue

print("Exceptions hit: ", ExceptionCount)
print("Total Reviews Processed: ", Records)
