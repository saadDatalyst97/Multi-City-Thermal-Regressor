import pandas as pd
import numpy as np

print("⚙️ 7 Lakh Rows ka Data Prepare ho raha hai... (Big Data Processing) ⏳")

# 1. Jo nayi 10 saal wali file aapne banayi hai usko open karein
df = pd.read_csv("All_Pakistan_10_Years_Chunked_Weather.csv")

# 2. Missing values ko hata dein (Data Cleaning)
df = df.dropna()

# 3. NAYA FEATURE: AI ko aur smart banane ke liye Date_Time se 'Month' aur 'Hour' nikalna
df['Date_Time'] = pd.to_datetime(df['Date_Time'])
df['Month'] = df['Date_Time'].dt.month
df['Hour'] = df['Date_Time'].dt.hour

# 4. 'Real_Temperature' ka naya column banate hain (Target/Label)
np.random.seed(42) # Taake sab ke paas same random numbers aayen
noise = np.random.uniform(0.5, 2.5, len(df))
df['Real_Temperature'] = round(df['Temperature_API'] + noise, 2)

# 5. Nayi ML-Ready file save karein
file_name = "All_Pakistan_10_Years_ML_Ready.csv"
df.to_csv(file_name, index=False)

print("\n✅ Step 2 Done! 🎉 AI ki training ke liye PRO-MAX data tayyar hai.")
print(f"📊 Final Cleaned Records: {len(df)} rows")
print("\nYeh dekhein aapka naya Advanced Data:")
print(df[['City', 'Month', 'Hour', 'Temperature_API', 'Rain_API', 'Real_Temperature']].head())