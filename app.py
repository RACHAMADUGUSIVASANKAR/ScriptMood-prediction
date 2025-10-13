from flask import Flask, render_template, request
import pickle

# Load model and vectorizer
classifier = pickle.load(open('movie-genre-mnb-model.pkl','rb'))
cv = pickle.load(open('cv-transform.pkl','rb'))

app = Flask(__name__)

# Genre names mapped by index
index_to_genre = [
    "Miscellaneous", "Action", "Adventure", "Comedy", "Drama",
    "Horror", "Romance", "Sci-Fi", "Thriller"
]

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

    # Probability values for each genre
    probs = [round(p * 100, 2) for p in classifier.predict_proba(vect)[0]]

    # Get genre names for x-axis and tooltip display
    genres = index_to_genre

    # Predicted genre name
    predicted_genre = genres[int(my_prediction[0])]

    return render_template(
        'result.html',
        prediction=my_prediction[0],        # Predicted genre index
        predicted_genre=predicted_genre,    # Predicted genre name
        genres=genres,                      # List of genre names
        probs=probs                         # Probabilities
    )

if __name__ == '__main__':
    app.run(debug=True)
