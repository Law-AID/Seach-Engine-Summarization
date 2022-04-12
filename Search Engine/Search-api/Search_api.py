# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 21:27:46 2022

@author: HP
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
#from chat import get_response
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
from nltk.corpus import stopwords
#nltk.download('punkt')
#nltk.download('stopwords')
app = Flask(__name__)
CORS(app)

@app.route("/predict/", methods =['POST'])

def predict():
    ps = PorterStemmer()
    f = open('C:/Users/HP/Desktop/Search Engine/COI-updated.txt', encoding="utf8")
    a = sent_tokenize(f.read())
    
    # removal of stopwords
    stop_words = list(stopwords.words('english'))
    
    # removal of punctuation signs
    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    s = [(word_tokenize(a[i])) for i in range(len(a))]
    outer_1 = []
    
    for i in range(len(s)):
    	inner_1 = []
    	
    	for j in range(len(s[i])):
    		
    		if s[i][j] not in (punc or stop_words):
    			s[i][j] = ps.stem(s[i][j])
    			
    			if s[i][j] not in stop_words:
    				inner_1.append(s[i][j].lower())
    	
    	outer_1.append(set(inner_1))
    rvector = outer_1[0]
    
    for i in range(1, len(s)):
    	rvector = rvector.union(outer_1[i])
    outer = []
    
    for i in range(len(outer_1)):
    	inner = []
    	
    	for w in rvector:
    		
    		if w in outer_1[i]:
    			inner.append(1)
    		
    		else:
    			inner.append(0)
    	outer.append(inner)
    
    comparison = input("Input: ")
    
    
    check = (word_tokenize(comparison))
    check = [ps.stem(check[i]).lower() for i in range(len(check))]
    
    
    check1 = []
    for w in rvector:
    	if w in check:
    		check1.append(1) # create a vector
    	else:
    		check1.append(0)
    
    ds = []
    
    for j in range(len(outer)):
    	similarity_index = 0
    	c = 0
    	
    	if check1 == outer[j]:
    		ds.append(0)
    	else:
    		for i in range(len(rvector)):
    
    			c += check1[i]*outer[j][i]
    
    		similarity_index += c
    		ds.append(similarity_index)
    
    
    ds
    maximum = max(ds)
    print()
    print()
    print("Similar sentences: ")
    for i in range(len(ds)):
    
    	if ds[i] == maximum:
    		print(a[i])

if __name__ == "__main__":
    app.run(debug=True)
