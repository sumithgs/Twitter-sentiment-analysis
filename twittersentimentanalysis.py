from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 
import pandas as pd
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

dataset = pd.read_csv('/home/sumithgs/Documents/Datasets/SuicideWatchposts_labeled1.csv')

def sentiment_scores(sentence): 

    sid_obj = SentimentIntensityAnalyzer() 
    sentiment_dict = sid_obj.polarity_scores(sentence) 
      
    print("Overall sentiment dictionary is : ", sentiment_dict) 
    print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative") 
    print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral") 
    print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive") 
    print("Sentence Overall Rated As", end = " ") 
    if sentiment_dict['compound'] >= 0.05 : 
        print("Positive") 
  
    elif sentiment_dict['compound'] <= - 0.05 : 
        print("Negative") 
  
    else : 
        print("Neutral") 

    
#if __name__ == "__main__" : 

    """
    sentence = "Geeks For Geeks is the best portal for computer science engineering students." 
    print("1st statement :" + sentence) 
    sentiment_scores(sentence) 
  
    sentence = "study is going on as usual"
    print("2nd Statement :"+sentence)
    sentiment_scores(sentence) 
  
    sentence = "I am vey sad today."
    print("3rd Statement :"+sentence)
    sentiment_scores(sentence) 
    """
corpus = []
for i in range(0,len(dataset)):
    def remove_data(vTEXT):
        vTEXT = re.sub('@[A-Za-z0–9]+', '', vTEXT)
        vTEXT = re.sub('#', '', vTEXT)  # Removing '#' hash tag
        vTEXT = re.sub('RT[\s]+', '', vTEXT)  # Removing RT
        vTEXT = re.sub('https?:\/\/\S+', '', vTEXT)  # Removing hyperlink
        vTEXT = re.sub('[^a-zA-Z]', ' ', vTEXT, flags=re.MULTILINE)
        vTEXT = vTEXT.lower()
        vTEXT = vTEXT.split()
        all_stopwords = stopwords.words('english')
        all_stopwords.remove('not')
        vTEXT = [word for word in vTEXT if not word in set(all_stopwords)]
        return vTEXT
    review = remove_data(str(dataset['body'][i]))
    review = ' '.join(review)
    review = sentiment_scores(review)
    corpus.append(review)
print(corpus)