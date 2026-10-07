import os
import pandas as pd
import pickle
import warnings
warnings.filterwarnings('ignore') # Faltu warnings chup karwane ke liye

print("🚀 All-Pakistan PRO-MAX Model Live Test Shuru ho raha hai...\n")

# 1. 🛡️ Bulletproof Path Setup (Yeh khud folder dhoondh lega)
script_dir = os.path.dirname(os.path.abspath(__file__)) # Pata lagayen script kahan hai
model_path = os.path.join(script_dir, '..', 'models', 'MultiCity_Thermal_Model_PRO.pkl') # Wahan se models folder mein jayen

# 2. Naya PRO Model load karein
with open(model_path, 'rb') as f:
    model = pickle.load(f)
print("🤖 10-Saal wala AI Model successfully load ho gaya hai!\n")

expected_columns = model.feature_names_in_

# (Iske neechay aapka wo 'test_samples' aur baqi ka sara code same rahega...)

# 2. Sab 8 shehron ka Advanced Sample Data (Farz karein June ka mahina hai aur dopahar ke 2 baj rahe hain)
test_samples = [
    {'City': 'Karachi', 'Month': 6, 'Hour': 14, 'Temperature_API': 28.0, 'Humidity_API': 80.0, 'WindSpeed_API': 8.5, 'Rain_API': 0.0, 'Soil_Temp_API': 32.0, 'Solar_Radiation_API': 600.0},
    {'City': 'Lahore', 'Month': 6, 'Hour': 14, 'Temperature_API': 31.0, 'Humidity_API': 70.0, 'WindSpeed_API': 4.0, 'Rain_API': 0.0, 'Soil_Temp_API': 35.0, 'Solar_Radiation_API': 650.0},
    {'City': 'Islamabad', 'Month': 6, 'Hour': 14, 'Temperature_API': 26.5, 'Humidity_API': 75.0, 'WindSpeed_API': 3.5, 'Rain_API': 0.0, 'Soil_Temp_API': 30.0, 'Solar_Radiation_API': 550.0},
    {'City': 'Rawalpindi', 'Month': 6, 'Hour': 14, 'Temperature_API': 27.0, 'Humidity_API': 74.0, 'WindSpeed_API': 4.2, 'Rain_API': 0.0, 'Soil_Temp_API': 30.5, 'Solar_Radiation_API': 560.0},
    {'City': 'Peshawar', 'Month': 6, 'Hour': 14, 'Temperature_API': 29.0, 'Humidity_API': 68.0, 'WindSpeed_API': 2.0, 'Rain_API': 0.0, 'Soil_Temp_API': 33.0, 'Solar_Radiation_API': 620.0},
    {'City': 'Quetta', 'Month': 6, 'Hour': 14, 'Temperature_API': 22.0, 'Humidity_API': 30.0, 'WindSpeed_API': 5.5, 'Rain_API': 0.0, 'Soil_Temp_API': 25.0, 'Solar_Radiation_API': 800.0},
    {'City': 'Multan', 'Month': 6, 'Hour': 14, 'Temperature_API': 33.5, 'Humidity_API': 45.0, 'WindSpeed_API': 6.0, 'Rain_API': 0.0, 'Soil_Temp_API': 38.0, 'Solar_Radiation_API': 700.0},
    {'City': 'Astore', 'Month': 6, 'Hour': 14, 'Temperature_API': 17.5, 'Humidity_API': 85.0, 'WindSpeed_API': 1.7, 'Rain_API': 0.0, 'Soil_Temp_API': 19.0, 'Solar_Radiation_API': 400.0}
]

print("🎯 --- ALL-PAKISTAN CITIES LIVE TEST RESULTS (PRO) ---")

# 3. Har shehar par Ninja Trick lagayen aur predict karein
for row in test_samples:
    # Model ke liye blank format set karein
    input_data = {col: 0 for col in expected_columns}
    
    # User ki values daalein
    for key in ['Month', 'Hour', 'Temperature_API', 'Humidity_API', 'WindSpeed_API', 'Rain_API', 'Soil_Temp_API', 'Solar_Radiation_API']:
        input_data[key] = row[key]
        
    # City wali trick (Sirf is shehar ko 1 karo baki sab 0)
    city_col_name = f"City_{row['City']}"
    if city_col_name in expected_columns:
        input_data[city_col_name] = 1
        
    # Prediction lagayen
    df_input = pd.DataFrame([input_data])
    predicted_temp = model.predict(df_input)[0]
    
    print(f"📍 Shehar: {row['City']:<10} | API Temp: {row['Temperature_API']:<5}°C ---> 🤖 AI Predicted Temp: {round(predicted_temp, 2)}°C")

print("\n🎉 Jadoo mukammal! Sab shehron ka live test kamyab raha.")