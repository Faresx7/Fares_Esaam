import pickle
from .cleaning_text import clean_text

with open('model/student_career_model.pkl', 'rb') as f:
    data = pickle.load(f)

model = data["model"]
tfidf = data["vectorizer"]


def user_prediction(text):
    '''
    description:
    this function takes a text 
    and applies cleaning and create a tf-idf word matrix for it
    the clean_text()  functions comes from 'cleaning_text.py' file 
    paramters: normal text (str)
    output: prediction (str)
    '''
    user_clean = clean_text(text)

    user_vector = tfidf.transform([user_clean])
    
    prediction = model.predict(user_vector)
    return prediction[0]