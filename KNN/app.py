from flask import Flask, render_template, request, jsonify
import numpy as np
import joblib

model = joblib.load('KNN/knn_leaf.pkl')

app = Flask(__name__)
@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        pl = float(request.form['petal_length'])
        pw = float(request.form['petal_width'])
        sl = float(request.form['sepal_length'])
        sw = float(request.form['sepal_width'])
        
        data = np.array([sl, sw, pl, pw,]).reshape(-1, 4)
        prediction = model.predict(data)
        if prediction[0] == 0:
           return jsonify({'prediction': 'Iris-setosa'})
        elif prediction[0] == 1:
           return jsonify({'prediction': 'Iris-versicolor'})
        else:
           return jsonify({'prediction': 'Iris-virginica'})
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)