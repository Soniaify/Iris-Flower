# Iris Flower Classifier Web App

This project is a simple machine learning web application that classifies Iris flower species based on user-provided measurements. It uses a trained classification model (e.g., Logistic Regression, KNN, or Decision Tree) and provides predictions through a clean and responsive HTML form.

## Demo
Try the app by entering:
- Sepal Length (cm)
- Sepal Width (cm)
- Petal Length (cm)
- Petal Width (cm)

## Dataset
The Iris dataset is a well-known dataset included in `scikit-learn`. It contains 150 rows with 4 features and 3 target classes:
- **Setosa**
- **Versicolor**
- **Virginica**

## Technologies Used
- Python
- scikit-learn
- Flask (Backend)
- HTML/CSS (Frontend)
- Jinja2 (Templating)

## Project Structure
KNN/
├── app.py # Flask backend
├── knn_leaf.pkl # Trained ML model
├── templates/
│ └── index.html # HTML form
├── knn.ipynb
├── IRIS.csv

