import os
import streamlit as st
import pickle
import string
import nltk

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

def transform_txt(txt):
    txt = txt.lower() #Converting text to lower case
    txt = nltk.word_tokenize(txt) #Tokenization
    
    x = []
    for i in txt:
        if i.isalnum(): #Removing special characters
            x.append(i)
    
    txt = x[:]
    x.clear()

    for i in txt:
        if i not in stopwords.words('english') and i not in string.punctuation:
            x.append(i)

    txt = x[:]
    x.clear()

    for i in txt:
        x.append(ps.stem(i))
            
    return " ".join(x)

os.chdir(os.path.dirname(os.path.abspath(__file__)))

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

#Giving Title
st.title("SMS Classifier")

input_sms = st.text_input("Enter the message: ")

#button to get the output
if st.button('Predict'):

    #1. preprocess
    transformed_sms = transform_txt(input_sms)
    #2. vectorize
    vector_input = tfidf.transform([transformed_sms])
    #3. predict
    result = model.predict(vector_input)[0]
    #4. display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")