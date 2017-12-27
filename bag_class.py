import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import os
from sklearn.metrics.classification import accuracy_score

# train data 
source = [('C:\\Users\\Vaishali\\Downloads\\text\\BD\\', 'BIG DATA'),
          ('C:\\Users\\Vaishali\\Downloads\\text\\BC\\', 'BIO CHEMIST'), 
          ('C:\\Users\\Vaishali\\Downloads\\text\\HFM\\', 'HFM HYPERION'),
          ('C:\\Users\\Vaishali\\Downloads\\text\\TrB\\','TRANSACTION BANKING'),
          ('C:\\Users\\Vaishali\\Downloads\\text\\UX\\','UX DESIGNER')
          ]

def build_data_frame(dpath, classification):
    rows = []
    for file_name in os.listdir(dpath):       
        fpath = os.path.join(dpath,file_name)
        rows.append({'text': fpath, 'labels': classification })
    data_frame = pd.DataFrame(rows)
    return(data_frame)

data = pd.DataFrame({'text': [], 'labels':[]})

for dpath, classification in source:
    data = data.append(build_data_frame(dpath, classification))

#path='F:/breezy_1nov/positions/positions_closed/Big Data Developer/resume_Big Data Developer/'
path= 'C:\\Users\\Vaishali\\Downloads\\text\\test\\'
text_files = [f for f in os.listdir(path)]

test = []
for i in text_files:
    fullname = os.path.join(path,i)
    test.append(fullname)


print(data)

train = data['text'].values
targets = data['labels'].values

vectorizer = CountVectorizer(ngram_range=(1,1),token_pattern=r'\b\w+\b', min_df=2,lowercase=True, stop_words="english",input='filename',decode_error='ignore', strip_accents='unicode')
X = vectorizer.fit_transform((train))
vocab = vectorizer.get_feature_names()

print(X.shape)
features = pd.DataFrame(X.A, columns=vectorizer.get_feature_names())
print(features)

clf = MultinomialNB()
y_target=['TRANSACTION BANKING', 'BIO CHEMIST', 'HFM HYPERION', 'HFM HYPERION', 'TRANSACTION BANKING', 'DOCUMENTUM', 'BIG DATA', 'UX DESIGNER']
clf = clf.fit(X,targets)
#print(test)
Y = vectorizer.transform(test).toarray()
print(Y)
pre = clf.predict(Y)

print(pre)

print(accuracy_score(y_target,pre))
