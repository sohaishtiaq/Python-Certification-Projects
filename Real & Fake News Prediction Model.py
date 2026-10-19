import pandas as pd
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
nltk.download('stopwords')
fake = pd.read_csv('/content/Fake.csv')
true = pd.read_csv('/content/True.csv')
fake['label'] = 0   # Fake News
true['label'] = 1   # Real News
data = pd.concat([fake, true], axis=0)
data = data.sample(frac=1, random_state=42)
data = data.dropna()
data = data.drop_duplicates()
data = data[['text', 'label']]
ps = PorterStemmer()
def clean_text(text):
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.lower()
    words = text.split()
    words = [ps.stem(word) for word in words if word not in stopwords.words('english')]
    return " ".join(words)
data['text'] = data['text'].apply(clean_text)
X = data['text']
y = data['label']
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
def predict_news(news):
    news = vectorizer.transform([news])
    prediction = model.predict(news)
    
    if prediction[0] == 0:
        return "Fake News"
    else:
        return "Real News"
print(predict_news("Breaking: Government announces new policy today"))
