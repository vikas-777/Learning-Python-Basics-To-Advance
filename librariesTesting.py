# gender_prediction_nltk_clean.py

import random
import numpy as np
from nltk.corpus import names
from sklearn.feature_extraction import DictVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# load names dataset from nltk
male_names = [(name, "male") for name in names.words("male.txt")]
female_names = [(name, "female") for name in names.words("female.txt")]
all_names = male_names + female_names
random.seed(42)
random.shuffle(all_names)

# feature extraction function (lowercase name)
def extract_features(name):
    name = name.lower()
    vowels = set("aeiou")
    return {
        "first_letter": name[0],
        "last_letter": name[-1],
        "last_two": name[-2:] if len(name) >= 2 else name[-1],
        "name_length": len(name),
        "vowel_count": sum(1 for ch in name if ch in vowels),
        "consonant_count": sum(1 for ch in name if ch.isalpha() and ch not in vowels),
        "has_hyphen": "-" in name
    }

# prepare feature matrix and labels
features = [extract_features(n) for n, g in all_names]
labels = [g for n, g in all_names]

vec = DictVectorizer(sparse=False)
x = vec.fit_transform(features)
y = np.array(labels)

# train-test split (stratified)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)

# model training
model = MultinomialNB()
model.fit(x_train, y_train)

# evaluation
y_pred = model.predict(x_test)
print("accuracy:", accuracy_score(y_test, y_pred))
print("\nclassification report:\n", classification_report(y_test, y_pred))
print("\nconfusion matrix:\n", confusion_matrix(y_test, y_pred))

# cross-validation
cv_scores = cross_val_score(model, x, y, cv=5, scoring="accuracy")
print("\n5-fold cv accuracy mean:", cv_scores.mean(), "std:", cv_scores.std())

# helper for single predictions
def predict_gender(name):
    feats = extract_features(name)
    x_name = vec.transform([feats])
    return model.predict(x_name)[0], model.predict_proba(x_name).max()

# examples
examples = ["Vikash", "Anjali", "Taylor", "Alex", "Sasha", "Rohit", "Priya"]
for ex in examples:
    pred, prob = predict_gender(ex)
    print(f"name: {ex:10} predicted: {pred:6} confidence: {prob:.3f}")
