from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import string
# import nltk

# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    '''
    description:
        this function takes a text as input and apply lowercasing, removing punctuation,
    tokenization, removing stop words and lammatization on it
    paramters: normal text (str)
    output: cleaned text (str)
    '''
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    tokens = word_tokenize(text)
    lemmas = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    
    
    return " ".join(lemmas)
