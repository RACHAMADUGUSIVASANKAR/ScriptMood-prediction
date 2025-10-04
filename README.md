
# 🎬 ScriptMood – Emotion Prediction App

- A Flask web application that predicts the genre of a movie based on its description or script snippet.  
- It uses Machine Learning (Naive Bayes + CountVectorizer) trained on a Kaggle dataset of 22,000+ movie reviews.

---

```markdown

## 📂 Project Structure


ScriptMood-prediction/
│── app.py                     # Flask web app
│── requirements.txt           # Dependencies
│── Procfile                   # For deployment (Heroku)
│── kaggle_movie_train.csv     # Training dataset (22k reviews)
│── cv-transform.pkl           # Saved CountVectorizer (text → numbers)
│── movie-genre-mnb-model.pkl  # Saved trained ML model
│── static/                    # CSS, icons, videos
│   ├── styles.css
|   ├── logo-favicon.ico
|   └── Watch the Video.mp4
│── templates/                 # HTML frontend
│   ├── index.html             # Input page
│   └── result.html            # Prediction result page
│── .gitattributes             # Git settings
```

---

## 🗂️ Key Components

### `kaggle_movie_train.csv`
- Contains 22,000+ movie reviews and their genres.
- Training dataset from Kaggle.
- Used only for training, not required during prediction.
- Examples:
```
review_text                       	genre
"A thrilling adventure!"           	Action
"Hilarious comedy scenes"	        Comedy
"Heartwarming story"	            Romance
```

---
### `cv-transform.pkl`
- Saved CountVectorizer (text → numbers).
- Learns the vocabulary of all movie reviews.
- Converts user input (e.g., "A scary haunted house") → a vector of word counts.

### `movie-genre-mnb-model.pkl`
- Trained Multinomial Naive Bayes classifier.
- Learns patterns from the training dataset.
- Uses the CountVectorizer’s numeric features to predict genres.

### `app.py`
- Flask backend.
- Loads `.pkl` files (vectorizer + trained model).
- Routes:
  - `/` → Home page (form to enter movie text)
  - `/predict` → Genre prediction result

### `templates/`
- `index.html` → Input form
- `result.html` → Displays prediction

### `Procfile`
- Required for Heroku deployment:
- Contains:
  ```
  web: gunicorn app:app
  ```

---

###📊 Workflow Diagram
```
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
```
---

## ⚙️ Installation (Run Locally)

```bash
# Step 1: Clone the repo
git clone https://github.com/RACHAMADUGUSIVASANKAR/ScriptMood-prediction.git
cd ScriptMood-prediction

# Step 2: Create a virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows

# Step 3: Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
pip install Flask scikit-learn gunicorn  # If needed

# Step 4: Run the app
python app.py
```

Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🚀 Deploying to Heroku

1. [Install Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)  
2. Login: `heroku login`  
3. Create app: `heroku create your-app-name`  
4. Push code:
   ```bash
   git add .
   git commit -m "Deploy app"
   git push heroku main
   ```
5. Open app: `heroku open`
6. Reference video for heroku setup process: [video](https://youtu.be/aUW5GAFhu6s?si=TwAcja6qtxoDSWeE)
---

## 🧠 How the Model Works

### Training Phase
- Preprocess text (lowercase, remove stopwords, punctuation, stemming)
- Vectorize using CountVectorizer
- Train Naive Bayes classifier
- Save model and vectorizer as `.pkl` files

### Prediction Phase
- User input → vector (via `cv-transform.pkl`)
- Model (`movie-genre-mnb-model.pkl`) predicts genre
- Result displayed on webpage

---

### 📝 Example Prediction

Input (user):
```
"A heartwarming love story set in Paris."
```
Output (app):
```
Predicted Genre: Romance
```
---

### Demo output video


https://github.com/user-attachments/assets/b66195ea-16af-40be-a2eb-b0ef50cffc0e




## 🙌 Contribution

Feel free to fork and enhance:
- Use a larger dataset
- Experiment with other ML models (Logistic Regression, SVM, BERT)
- Expand genre coverage

---

## 👨‍💻 Author

**Sivasankar R**  
AI & ML Engineering Student  
GitHub: [RACHAMADUGUSIVASANKAR](https://github.com/RACHAMADUGUSIVASANKAR)
Linkidin: [RACHAMADUGUSIVASANKAR](https://www.linkedin.com/in/sivasankar-rachamadugu/)


---

## 📄 License

This project is licensed under the MIT License.
```

Let me know if you'd like this formatted for a GitHub Pages site or want badges (e.g., build status, license, Python version) added!
