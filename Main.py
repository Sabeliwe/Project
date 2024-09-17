from flask import Flask, render_template, request
from utils.data_processing import load_crop_data
from models.crop_recommendation_model import train_crop_model, recommend_crop

app = Flask(__name__)

# Load and prepare data
crop_data = load_crop_data('data/crop_data.csv')
model = train_crop_model(crop_data)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    rainfall = request.form['rainfall']
    temperature = request.form['temperature']
    soil_type = request.form['soil_type']
    crop = recommend_crop(model, [rainfall, temperature, soil_type])
    return render_template('result.html', crop=crop)

if __name__ == '__main__':
    app.run(debug=True)