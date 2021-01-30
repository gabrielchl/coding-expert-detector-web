from flask import Flask, render_template, request, jsonify
import joblib
from features_extractor import extract

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/result', methods=['post'])
def result():
    model = joblib.load('model.sav')
    features = extract(request.form['code'])
    prediction = model.predict([features])[0]
    if prediction:
        classification_string = 'expert'
    else:
        classification_string = 'novice'
    features_labeled = [
        'Number of lines',
        'Number of empty lines',
        'Average length of lines',
        'Number of variables',
        'Average length of variables',
        'Number of if statements',
        'Number of for statements',
        'Number of do statements',
        'Number of while statements',
        'Number of catch statements',
        'Number of casts',
        'Ratio of bracket without to with a space before it',
        'Ratio of curly bracket starting in same line to new line',
        'Number of spaces (excluding those for indentation)'
    ]
    for i in range(len(features_labeled)):
        features_labeled[i] = [features_labeled[i], features[i]]
    return render_template('result.html',
                           classification_string=classification_string,
                           features=features_labeled)


@app.route('/api/get-class-and-features', methods=['post'])
def get_class_and_features():
    model = joblib.load('model.sav')
    features = extract(request.form['code'])
    prediction = model.predict([features])[0]
    features.insert(0, prediction)
    features = [str(i) for i in features]
    return "\n".join(features)
