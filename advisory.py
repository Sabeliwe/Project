# advisory.py

def generate_advisory(crop_data, weather_data, pest_outbreaks):
    advisory = f"Advisory for {crop_data['crop']}:"
    advisory += f"\n- Soil moisture: {crop_data['soil_moisture']}%"
    advisory += f"\n- Temperature: {crop_data['temperature']}°C"
    advisory += f"\n- Rainfall: {weather_data['rainfall']} mm"
    advisory += f"\n- Humidity: {weather_data['humidity']}%"
    
    if pest_outbreaks['armyworms']:
        advisory += "\n- Warning: Armyworm outbreak detected."
    if pest_outbreaks['locusts']:
        advisory += "\n- Warning: Locust outbreak detected."
    
    return {"recommendation": advisory}

