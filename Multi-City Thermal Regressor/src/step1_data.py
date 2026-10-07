import requests
import pandas as pd
import time

print("🚀 Bismillah! 'Bulletproof Chunking' Technique se 10-Saal ka Big Data download ho raha hai... ⏳")

cities = {
    'Karachi': {'lat': 24.8607, 'lon': 67.0011},
    'Lahore': {'lat': 31.5204, 'lon': 74.3587},
    'Islamabad': {'lat': 33.6938, 'lon': 73.0652},
    'Rawalpindi': {'lat': 33.6007, 'lon': 73.0679}, 
    'Peshawar': {'lat': 34.0150, 'lon': 71.5805},
    'Quetta': {'lat': 30.1920, 'lon': 67.0281},
    'Multan': {'lat': 30.1984, 'lon': 71.4687},
    'Astore': {'lat': 35.3667, 'lon': 74.8500}
}

years = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
all_city_data = []

for city, coords in cities.items():
    print(f"\n📡 {city} ka data nikal raha hai...")
    
    for year in years:
        start_date = f"{year}-01-01"
        end_date = f"{year}-12-31"
        
        url = f"https://archive-api.open-meteo.com/v1/archive?latitude={coords['lat']}&longitude={coords['lon']}&start_date={start_date}&end_date={end_date}&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m,precipitation,soil_temperature_0_to_7cm,shortwave_radiation&timezone=auto"
        
        try:
            # JADOO: 15 seconds ka timeout set kar diya hai taake crash na ho
            response = requests.get(url, timeout=15)
            
            if response.status_code == 200:
                data = response.json()
                df = pd.DataFrame({
                    'City': city,
                    'Date_Time': data['hourly']['time'],
                    'Temperature_API': data['hourly']['temperature_2m'],
                    'Humidity_API': data['hourly']['relative_humidity_2m'],
                    'WindSpeed_API': data['hourly']['wind_speed_10m'],
                    'Rain_API': data['hourly']['precipitation'],
                    'Soil_Temp_API': data['hourly']['soil_temperature_0_to_7cm'],
                    'Solar_Radiation_API': data['hourly']['shortwave_radiation']
                })
                all_city_data.append(df)
                print(f"   ✅ {year} Done")
            else:
                print(f"   ⚠️ {year} mein error aaya: {response.status_code}. Skip kar rahe hain.")
                
        # Agar internet drop ho jaye ya Timeout ho jaye toh code yahan aayega
        except requests.exceptions.RequestException as e:
            print(f"   ❌ {year} mein Internet/Timeout ka masla aya. Skip kar rahe hain.")
            
        # API ko sakoon dene ke liye wait
        time.sleep(3) 
            
    # Ek shehar mukammal hone ke baad break
    time.sleep(5)

# Sab Data ko ek sath jorna
if len(all_city_data) > 0:
    final_df = pd.concat(all_city_data, ignore_index=True)
    file_name = "All_Pakistan_10_Years_Chunked_Weather.csv"
    final_df.to_csv(file_name, index=False)
    print(f"\n🎉 JADOO! Data '{file_name}' mein save ho gaya!")
    print(f"📊 Total Records: {len(final_df)} rows!")
else:
    print("\n❌ Koi data download nahi hua.")