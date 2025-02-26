from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

mapping = {
    0: 'setosa',
    1: 'versicolor',
    2: 'virginica'
}


@app.route("/")
def home():
    result = ""
    return render_template("index.html", result=result)  


@app.route("/predict", methods=["POST", "GET"])
def predict():
    result = ""
    if request.method == "POST":
        sepal_lenght = float(request.form['sepal length (cm)'])
        sepal_width = float(request.form['sepal width (cm)'])
        petal_lenght = float(request.form['petal length (cm)'])
        petal_width = float(request.form['petal width (cm)'])

        # Use the same column names as used during model training
        input_data = pd.DataFrame([[sepal_lenght, sepal_width, petal_lenght, petal_width]],
                                   columns=['sepal length (cm)', 'sepal width (cm)',
                                            'petal length (cm)', 'petal width (cm)'])

        # predict
        prediction = model.predict(input_data)
        
        # Map prediction to category
        result = mapping.get(prediction[0], "Unknown Category")

    return render_template("index.html", result=result)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host = '0.0.0.0', port=5000)