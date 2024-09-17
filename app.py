from flask import Flask, render_template, request
from data_processing import get_weather_data
from advisory import generate_advisory

app = Flask(__name__)
from flask import Flask, render_template
import os

app = Flask(__name__, template_folder=os.path.abspath('templates'))

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/')
def home():
    return render_template('index.html')
app.config['TEMPLATES_AUTO_RELOAD'] = True

from flask import Flask
from config import DevelopmentConfig, ProductionConfig

app = Flask(__name__)

# Use environment-specific configuration
if app.env == "development":
    app.config.from_object(DevelopmentConfig)
else:
    app.config.from_object(ProductionConfig)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

@app.route('/get_advisory', methods=['POST'])
def get_advisory():
    # Get form data
    location = request.form['location']
    crop_type = request.form['crop_type']
    
    # Fetch the weather data
    weather_data = get_weather_data(location)
    
    if weather_data:
        # Example: pest outbreaks could be fetched from another source
        pest_outbreaks = ["locust", "armyworm"]  
        
        # Generate the advisory based on weather data and pest outbreaks
        advisory = generate_advisory(crop_type, weather_data, pest_outbreaks)
        
        # Render the advisory template with the generated advisory
        return render_template('advisory.html', advisory=advisory)
    else:
        return "Error fetching weather data."

if __name__ == '__main__':
    app.run(debug=True)


