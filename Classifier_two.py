'''
Created on Jan 3, 2018

@author: SIJA
'''
import os
import csv
import pandas as pd
from pathlib import Path
from pandas import DataFrame
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import path

path = open('E:/data/buckets1.csv', encoding = "ISO-8859-1")
df=pd.read_csv(path)
#print(df['SKILLS'])

tfidf_vectorizer = TfidfVectorizer(lowercase=True, use_idf=True)
tfidf_matrix = tfidf_vectorizer.fit_transform(df['SKILLS'])

#vectorizer = CountVectorizer(ngram_range=(1,3), lowercase=True)
#counts = vectorizer.fit_transform(df['SKILLS'])

classifier = MultinomialNB()
targets = df['PROFILE']
classifier.fit(tfidf_matrix, targets)

test_dir = 'E:/jobdiva_text/08_text/'
d1 = DataFrame
def built2(test_dir):
    rows1=[]
    for filename in os.listdir(test_dir):
        k1 = filename
        test_file= os.path.join(test_dir,k1)
        with open(test_file, encoding='iso-8859-1') as f2:
            content = f2.read().replace('\n', ' ')
        
        rows1.append({'text1': content, 'name': k1 })
    d1 = DataFrame(rows1)
    d1.to_csv("E:/Classifier_output/data_file2.csv")    
    #  print(d1['text1'])    
    return(d1)  

tdata = DataFrame({'text1': [], 'name':[]})
tdata = tdata.append(built2(test_dir))  

example = tfidf_vectorizer.transform(tdata['text1'])
pred = classifier.predict(example)
#print(pred)

file_ext = pd.DataFrame({'Predicted': pred, 'filename':tdata['name']})
file_ext.to_csv("E:/Classifier_output/pred_file.csv")
#print(file_ext)
print("done")

with open('E:/Classifier_output/pred_file.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        fname = row[1]
        n_path = 'E:/Classifier_output/'+fname        
        new_folder = Path(n_path)
        if new_folder.is_dir():
            print("")
        else:
            print("created")
           
