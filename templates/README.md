## 🎬 ScriptMood: Emotion Predictor for Movie Scripts

ScriptMood is a web-based application that predicts the **emotional genre** of a movie script snippet using machine learning. Users can input a short script (up to 100 words), and the app will classify it into one of several moods or genres such as Action, Comedy, Drama, Horror, Romance, Sci-Fi, and more.

---

### 📁 HTML Files Overview

#### 1. `index.html` – Script Input Page

This is the landing page where users can submit their movie script for emotion prediction.

**Key Features:**
- ✍️ **Text Area Form**: Users enter a short script (100 words max).
- 🎬 **Predict Button**: Submits the form to the backend (`/predict` route).
- 🎥 **Watch the Video**: Opens a modal with a demo video explaining the project.
- ✨ **AOS Animations**: Smooth entrance animations for UI elements.
- 🎨 **Tailwind CSS**: Responsive and modern styling.
- 🔗 **Footer Links**: GitHub and LinkedIn profile of the developer.

**Technologies Used:**
- Tailwind CSS
- Animate on Scroll (AOS)
- Font Awesome
- Google Fonts (Yatra One)

---

#### 2. `result.html` – Prediction Output Page

This page displays the predicted emotion or genre after the user submits their script.

**Key Features:**
- 🧠 **Dynamic Genre Display**: Uses Jinja2 templating to show the predicted genre based on the model output.
- 🎨 **Color-coded Genres**: Each genre is styled with a unique color for visual distinction.
- 🔁 **Try Again Button**: Allows users to return to the input page and submit another script.
- ✨ **AOS Animations**: Enhances user experience with smooth transitions.
- 🔗 **Footer Links**: Same as the input page for consistency.

**Genre Mapping:**
| Prediction Code | Genre         |
|-----------------|---------------|
| 0               | Miscellaneous | 
| 1               | Action        | 
| 2               | Adventure     | 
| 3               | Comedy        | 
| 4               | Drama         | 
| 5               | Horror        | 
| 6               | Romance       | 
| 7               | Sci-Fi        | 
| 8               | Thriller      | 

---

### 🚀 How It Works

1. User enters a short movie script.
2. The script is sent to a Flask backend via POST request.
3. A machine learning model processes the script and returns a genre prediction.
4. The result is displayed on the `result.html` page.

---

Would you like me to help you write the backend Flask code or model integration section for the README as well?
