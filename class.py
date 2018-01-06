import pandas as pd
#from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import os
#from sklearn.metrics.classification import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
data = pd.read_csv('C:\\Users\\Vaishali\\Desktop\\job_classification\\buckets.csv')
print(data)

train = data['text'].values
targets = data['labels'].values

#vectorizer = CountVectorizer(ngram_range=(1,2), min_df=2,lowercase=True, stop_words="english",decode_error='ignore', strip_accents='unicode')
#vectorizer = CountVectorizer(ngram_range=(1,1), min_df=2,lowercase=True)   #, stop_words="english",decode_error='ignore', strip_accents='unicode')
vectorizer = TfidfVectorizer(ngram_range=(1,2),stop_words='english')
X = vectorizer.fit_transform((train))
vocab = vectorizer.get_feature_names()
print(X.shape)

features = pd.DataFrame(X.A, columns=vectorizer.get_feature_names())
print(features)
 
with open("C:\\Users\\Vaishali\\Desktop\\job_classification\\file_vocab.txt", "w",encoding="utf-8") as output:
        output.write(str(vocab))

clf = MultinomialNB()
clf = clf.fit(X,targets)

path= 'C:\\Users\\Vaishali\\Desktop\\text_08_all\\'
d1 = pd.DataFrame
def built2(path):
    rows1=[]
    for filename in os.listdir(path):
        k1 = filename
        test_file= os.path.join(path,k1)
        with open(test_file,encoding = 'iso-8859-1') as f2:
            content = f2.read().replace('\n', ' ')
        
        rows1.append({'text1': content, 'name': k1 })
    d1 = pd.DataFrame(rows1)    
 
    return(d1)  

test = pd.DataFrame({'text1': [], 'name':[]})
test = test.append(built2(path))
#print(test)
test.to_csv("C:\\Users\\Vaishali\\Desktop\\job_classification\\files_content3.csv",encoding='utf-8')

t = test['name'].values
content1 = test['text1'].values

Y = vectorizer.transform(test['text1']).toarray()
print(Y)
pre = clf.predict(Y)

res1 = pd.DataFrame(t,pre)
#print(res1)


print(res1)
res1.to_csv("C:\\Users\\Vaishali\\Desktop\\job_classification\\file_info3.csv",  encoding='utf-8')

