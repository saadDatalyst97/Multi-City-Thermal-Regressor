import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import pickle

print("🧠 AI Model Training shuru ho rahi hai... (Sabar rakhein, Big Data process ho raha hai) ⏳")

# 1. 10 Saal wala ML-Ready Data Load karein
df = pd.read_csv("All_Pakistan_10_Years_ML_Ready.csv")

# 2. Features (X) aur Target (y) alag karein
# Computer 'Karachi' ya 'Lahore' nahi parh sakta, isliye get_dummies inhein 0/1 (Numbers) mein convert karta hai
df = pd.get_dummies(df, columns=['City'], drop_first=True)

# Date_Time ki zaroorat nahi kyunke humne Month aur Hour nikal liya hai
X = df.drop(['Date_Time', 'Real_Temperature'], axis=1)
y = df['Real_Temperature']

# 3. Data ko Train (80%) aur Test (20%) mein split karein
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"📊 Training par Data laga diya gaya hai: {len(X_train)} rows")
print("⚙️ Random Forest apna jadoo kar raha hai... (CPU apni full speed par hai) 🔥")

# 4. Model Training (n_jobs=-1 ka matlab hai laptop ke saray processor cores use karo taake jaldi ho)
# Waqt bachane aur over-fitting se bachne ke liye n_estimators=50 aur max_depth=15 rakha hai
model = RandomForestRegressor(n_estimators=50, max_depth=15, n_jobs=-1, random_state=42)
model.fit(X_train, y_train)

# 5. Model ka Test (Imtihaan)
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\n✅ JADOO! AI Model Training Mukammal ho gayi!")
print(f"🎯 Mean Absolute Error (MAE): {mae:.2f} °C (Jitna kam utna acha)")
print(f"🏆 R-Squared (Accuracy): {r2:.4f} (1.0 ke qareeb hona chahiye)")

# 6. Model ko save karein (Pickle ke zariye)
with open("MultiCity_Thermal_Model_PRO.pkl", "wb") as f:
    pickle.dump(model, f)
    
print("\n💾 Advanced AI Model 'MultiCity_Thermal_Model_PRO.pkl' ke naam se save ho gaya hai!")