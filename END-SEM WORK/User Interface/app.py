from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import re
from textblob import TextBlob
import joblib
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import sent_tokenize, word_tokenize


app = Flask(__name__)

'''Load saved location'''
loclist = joblib.load('loclist')


def query_handling_and_ranking(query, location):
    '''Model Load'''
    savedModel = joblib.load('savedModel.sav')
    '''List for Ranking'''
    list_for_ranking = joblib.load('list_for_ranking.sav')

    sentences_dup = re.split('; |, |and |but |\*|\n', query)
    sentences = []
    for s in sentences_dup:
        sentences += s.split('.')

    try:
        sentences.remove('')
    except:
        pass

    sentence_list = []
    for s in sentences:
        sentence = s.lower()
        words = word_tokenize(s)
        en_stopwords = stopwords.words('english')
        processed_words = []
        for token in words:
            if token not in en_stopwords:
                processed_words.append(token)

        tokenizer = RegexpTokenizer(r"\w+")
        word_list = tokenizer.tokenize(' '.join(processed_words))
        word_list = [w.lower() for w in word_list if len(w) != 1]
        sentence_list.append(word_list)

    sentences = []
    for s in sentence_list:
        if(len(s) != 0):
            sentences.append(' '.join(s))

    query_sentences = []
    aspects = []
    sentiments = []

    for i in range(len(sentences)):
        try:
            aspects.append(savedModel.predict(
                pd.DataFrame([sentences[i]])[0])[0])
            query_sentences.append(sentences[i])
            sentiments.append(TextBlob(sentences[i]).sentiment.polarity)
        except:
            pass

    query_df = {}

    for i in range(len(aspects)):
        query_df[aspects[i]] = 0.0

    for i in range(len(aspects)):
        query_df[aspects[i]] += sentiments[i]

    for i in range(len(aspects)):
        query_df[aspects[i]] = query_df[aspects[i]]/aspects.count(aspects[i])

    aspects = ['cleanliness', 'location', 'service', 'room', 'value']

    for key in aspects:
        if key not in query_df.keys():
            query_df[key] = 0.0

    lfr = list()
    for l in list_for_ranking:
        if l[1] == location:
            lfr.append(l)

    final_list_for_ranking = []
    for rev in lfr:
        flag = True
        for key in rev[2].keys():
            if rev[2][key] < query_df[key]-0.2:
                flag = False

        if flag == True:
            final_list_for_ranking.append(rev)

    if len(final_list_for_ranking) < 2:
        final_list_for_ranking = lfr

    final_list_for_ranking = (
        sorted(final_list_for_ranking, key=lambda l: l[-1], reverse=True))

    return final_list_for_ranking


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        data = {"": ["", "", "", "", "", ""]}
        return render_template('view.html', locationlist=loclist, data=data)
    elif request.method == 'POST':
        query = request.form['query']
        location = request.form['location']

        '''Function Call'''
        flfr = query_handling_and_ranking(query, location)
        data = dict()
        count = 0
        for dl in flfr:
            tempList = list(dl[2].values())
            tempList.append(dl[3])
            formattedList = ['%.2f' % elem for elem in tempList]
            formattedList.append(dl[0])
            data[count] = formattedList
            count += 1

        return render_template('view.html', locationlist=loclist, data=data)


if __name__ == '__main__':
    app.run()
