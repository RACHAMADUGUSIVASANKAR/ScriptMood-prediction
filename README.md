🎬 ScriptMood – Movie Genre Prediction App

A Flask web application that predicts the genre of a movie based on its description or script snippet.
It uses Machine Learning (Naive Bayes + CountVectorizer) trained on a Kaggle dataset of 22,000+ movie reviews.

📂 Project Structure
ScriptMood-prediction/
│── app.py                     # Flask web app
│── requirements.txt           # Dependencies
│── Procfile                   # For deployment (Heroku)
│── kaggle_movie_train.csv     # Training dataset (22k reviews)
│── cv-transform.pkl           # Saved CountVectorizer (text → numbers)
│── movie-genre-mnb-model.pkl  # Saved trained ML model
│── static/                    # CSS, icons, videos
│   └── styles.css
│── templates/                 # HTML frontend
│   ├── index.html             # Input page
│   └── result.html            # Prediction result page
│── .gitattributes             # Git settings

🗂️ Explanation of Key Files

**1. kaggle_movie_train.csv**
- Training dataset from Kaggle.
- Contains 22,000+ movie reviews and their genres.
- Example:
              **review_text**	              **genre**
             "A thrilling adventure!"	       Action
             "Hilarious comedy scenes"	     Comedy
             "Heartwarming story"	           Romance

👉 Used only for training. Not required for predictions in the web app.

**2. cv-transform.pkl**
- Saved CountVectorizer (text → numbers).
- Learns the vocabulary of all movie reviews.
- Converts user input (e.g., "A scary haunted house") → a vector of word counts.

**3. movie-genre-mnb-model.pkl**
- Saved Multinomial Naive Bayes classifier.
- Learns patterns from the training dataset.
- Uses the CountVectorizer’s numeric features to predict genres.

**4. app.py**
- Flask application file.
- Loads .pkl files (vectorizer + trained model).
- Provides routes:
- / → Home page (form to enter movie text)
- /predict → Shows predicted genre

**5. templates/ folder**
- index.html → Form to enter text.
- result.html → Displays prediction result.
  
**6. Procfile**
- Needed for Heroku deployment.
- Contains:
             web: gunicorn app:app

 **⚙️ Installation (Run Locally)**
 
**Step 1: Clone the repo**
         git clone https://github.com/RACHAMADUGUSIVASANKAR/ScriptMood-prediction.git
         cd ScriptMood-prediction

**Step 2: Create a virtual environment**
         python -m venv venv
Activate it:
         venv\Scripts\activate
  
**Step 3: Install dependencies**
         pip install --upgrade pip
         pip install -r requirements.txt
- (If Flask or scikit-learn are missing, install them manually:)
         pip install Flask scikit-learn gunicorn
  
**Step 4: Run the app locally**
          python app.py

Now open http://127.0.0.1:5000

  **🚀 Deploying to Heroku**
**Step 1: Install Heroku CLI**
👉 Download here : https://devcenter.heroku.com/articles/heroku-cli

**Step 2: Login to Heroku**
           heroku login

**Step 3: Create a new Heroku app**
           heroku create your-app-name

**Step 4: Push code to Heroku**
          git add .
          git commit -m "Deploy app"
          git push heroku main

**Step 5: Open app in browser**
          heroku open

          
**🧠 How the Model Works**

**1. Training Phase**
- Load dataset (kaggle_movie_train.csv)
- Preprocess text (lowercase, remove stopwords, punctuation, stemming)
- Convert text → numbers using CountVectorizer
- Train Naive Bayes classifier on these vectors
- Save trained model + vectorizer as .pkl files

**2. Prediction Phase (app.py)**
- User enters text
- Text → vector (via cv-transform.pkl)
- Model (movie-genre-mnb-model.pkl) predicts genre
- Result shown on webpage

**📊 Workflow Diagram**

 Kaggle Dataset (CSV) ──> Preprocessing & Training ──> Model + Vectorizer (.pkl)
        |                                                   |
        v                                                   v
    Training Script                                    Flask App (app.py)
                                                           |
                                                           v
                                                   User enters text
                                                           |
                                                           v
                                                   Predicted Genre

**🙌 Contribution**

Feel free to fork this repo and try:
- Using a bigger dataset
- Trying other ML models (Logistic Regression, SVM, BERT)
- Adding more genres

**👨‍💻 Author**

Sivasankar R
AI & ML Engineering Student
