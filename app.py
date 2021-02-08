from flask import Flask, render_template, request, session
from javalang.parser import JavaSyntaxError
import joblib
from features_extractor import extract

app = Flask(__name__)
app.config['SECRET_KEY'] = 'p0owgnY8NC9CEuzRZqc2aamEZesAuCID'.encode('utf8')


@app.route('/')
def home():
    return render_template('home.html',
                           mode=session.get('mode'))


@app.route('/app')
def app_route():
    return render_template('app.html',
                           mode=session.get('mode'))


@app.route('/result', methods=['post'])
def result():
    model = joblib.load('model.sav')
    try:
        features = extract(request.form['code'])
    except JavaSyntaxError as e:
        return render_template('syntax_error.html',
                               mode=session.get('mode'),
                               error=e)
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
        features_labeled[i] = [features_labeled[i], str(features[i])[:8]]
    return render_template('result.html',
                           mode=session.get('mode'),
                           classification_string=classification_string,
                           features=features_labeled)


@app.route('/api/get-class-and-features', methods=['post'])
def get_class_and_features():
    model = joblib.load('model.sav')
    features = extract(request.form['code'])
    prediction = model.predict([features])[0]
    features.insert(0, prediction)
    features = [str(i)[:8] for i in features]
    return "\n".join(features)


@app.route('/attribution')
def attribution():
    return render_template('attribution.html',
                           mode=session.get('mode'))


@app.route('/dark-mode')
def dark_mode():
    session['mode'] = 'dark'
    return ('', 200)


@app.route('/light-mode')
def light_mode():
    session['mode'] = 'light'
    return ('', 200)
