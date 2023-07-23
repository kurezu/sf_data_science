from flask import Flask, request, jsonify
import pickle
import numpy as np
import catboost

# загружаем модель из файла
with open('./models/model.pkl', 'rb') as pkl_file:
    model = pickle.load(pkl_file)

# создаём приложение
app = Flask(__name__)

@app.route('/')
def index():
    msg = "Тестовое сообщение. Сервер запущен!"
    return msg

@app.route('/predict', methods=['POST'])
def predict():
    features = request.json
    features = np.array(features).reshape(1, 12)
    prediction = np.round(model.predict(features))
    return  jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run('localhost', 5000)