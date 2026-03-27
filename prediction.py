import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# 1. Load Model dan Scaler
model = joblib.load('model_rf.pkl')
scaler = joblib.load('scaler.pkl')

# 2. Load Data Asli sebagai Template
df_template = pd.read_csv(r'C:\Users\aryod\Downloads\employee_data.csv')

# 3. Preprocessing: Menghapus kolom yang tidak digunakan saat training
cols_to_drop = ['Attrition', 'EmployeeId', 'EmployeeCount', 'Over18', 'StandardHours']
df_template = df_template.drop(columns=[col for col in cols_to_drop if col in df_template.columns])

# --- PENTING: Mengubah teks menjadi angka (Encoding) ---
# Kita lakukan hal yang sama dengan yang ada di Google Colab
categorical_cols = df_template.select_dtypes(include=['object']).columns
for col in categorical_cols:
    le = LabelEncoder()
    df_template[col] = le.fit_transform(df_template[col])

# 4. Ambil satu baris sebagai contoh data baru
new_data = df_template.iloc[[0]].copy()

# 5. Silakan ubah nilai di bawah ini untuk mencoba prediksi berbeda
new_data['Age'] = 35
new_data['OverTime'] = 1  # 1 berarti 'Yes', 0 berarti 'No'
new_data['MonthlyIncome'] = 2500  # Coba gaji rendah untuk lihat apakah dia resign

# 6. Scaling (Sekarang aman karena sudah jadi angka semua)
new_data_scaled = scaler.transform(new_data)

# 7. Prediksi
prediction = model.predict(new_data_scaled)
probability = model.predict_proba(new_data_scaled)

print("\n" + "="*30)
print("HASIL PREDIKSI KARYAWAN")
print("="*30)
if prediction[0] == 1:
    print(f"Status   : BERPOTENSI RESIGN")
    print(f"Kepastian: {probability[0][1]*100:.2f}%")
else:
    print(f"Status   : TETAP BERTAHAN")
    print(f"Kepastian: {probability[0][0]*100:.2f}%")
print("="*30)