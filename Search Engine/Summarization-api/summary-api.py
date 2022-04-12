# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 23:42:20 2022

@author: HP
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import json
#from chat import get_response

app = Flask(__name__)
CORS(app)

@app.route("/predict/", methods =['POST'])

def predict():
    #text = "The Taj Mahal is located on the right bank of the Yamuna River in a vast Mughal garden that encompasses nearly 17 hectares, in the Agra District in Uttar Pradesh. It was built by Mughal Emperor Shah Jahan in memory of his wife Mumtaz Mahal with construction starting in 1632 AD and completed in 1648 AD, with the mosque, the guest house and the main gateway on the south, the outer courtyard and its cloisters were added subsequently and completed in 1653 AD. The existence of several historical and Quaranic inscriptions in Arabic script have facilitated setting the chronology of Taj Mahal. For its construction, masons, stone-cutters, inlayers, carvers, painters, calligraphers, dome builders and other artisans were requisitioned from the whole of the empire and also from the Central Asia and Iran. Ustad-Ahmad Lahori was the main architect of the Taj Mahal.The Taj Mahal is considered to be the greatest architectural achievement in the whole range of Indo-Islamic architecture. Its recognised architectonic beauty has a rhythmic combination of solids and voids, concave and convex and light shadow; such as arches and domes further increases the aesthetic aspect. The colour combination of lush green scape reddish pathway and blue sky over it show cases the monument in ever changing tints and moods. The relief work in marble and inlay with precious and semi precious stones make it a monument apart. "

    #text = input("INPUT: ")
    text = request.get_json()
    #text = json.dumps(data)
    # Tokenizing the text
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text)
    
    # Creating a frequency table to keep the
    # score of each word
    
    freqTable = dict()
    for word in words:
    	word = word.lower()
    	if word in stopWords:
    		continue
    	if word in freqTable:
    		freqTable[word] += 1
    	else:
    		freqTable[word] = 1
    
    # Creating a dictionary to keep the score
    # of each sentence
    sentences = sent_tokenize(text)
    sentenceValue = dict()
    
    for sentence in sentences:
    	for word, freq in freqTable.items():
    		if word in sentence.lower():
    			if sentence in sentenceValue:
    				sentenceValue[sentence] += freq
    			else:
    				sentenceValue[sentence] = freq
    
    
    
    sumValues = 0
    for sentence in sentenceValue:
    	sumValues += sentenceValue[sentence]
    
    # Average value of a sentence from the original text
    
    average = int(sumValues / len(sentenceValue))
    
    # Storing sentences into our summary.
    summary = ''
    for sentence in sentences:
    	if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
    		summary += " " + sentence
    return jsonify(summary)
    

if __name__ == "__main__":
    app.run(debug=True)