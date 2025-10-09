from flask import Flask, render_template, request
import pickle

# Load model and vectorizer
classifier = pickle.load(open('movie-genre-mnb-model.pkl','rb'))
cv = pickle.load(open('cv-transform.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    message = request.form['message']
    data = [message]
    vect = cv.transform(data).toarray()

    # Prediction
    my_prediction = classifier.predict(vect)

    # Convert classes to list of strings
    genres = [str(g) for g in classifier.classes_]
    probs = [round(p * 100, 2) for p in classifier.predict_proba(vect)[0]]

    # Map predicted index to genre name
    predicted_genre = genres[int(my_prediction[0])]

    return render_template(
        'result.html',
        prediction=my_prediction[0],        # send index
        predicted_genre=predicted_genre,   # send actual genre name
        genres=genres,                     # send list of genre names
        probs=probs
    )

if __name__ == '__main__':
    app.run(debug=True)
