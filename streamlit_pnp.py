import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

# --- 1. LOAD MODEL & SCALER ---
model = joblib.load('model_rf.pkl')
scaler = joblib.load('scaler.pkl')

# --- 2. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="HR Attrition Predictor", layout="wide")
st.title("📊 Sistem Prediksi Attrition Karyawan")
st.markdown("Aplikasi ini menggunakan model **Random Forest** untuk memprediksi apakah karyawan akan bertahan atau resign.")

st.divider()

# --- 3. INPUT DATA USER ---
st.subheader("📝 Masukkan Data Karyawan")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Umur", min_value=18, max_value=65, value=30)
    business_travel = st.selectbox("Perjalanan Bisnis", ["Travel_Rarely", "Travel_Frequently", "Non-Travel"])
    daily_rate = st.number_input("Daily Rate", value=800)
    department = st.selectbox("Departemen", ["Sales", "Research & Development", "Human Resources"])
    distance = st.number_input("Jarak dari Rumah (km)", min_value=1, value=5)

with col2:
    job_role = st.selectbox("Jabatan", ["Sales Executive", "Research Scientist", "Laboratory Technician", "Manufacturing Director", "Healthcare Representative", "Manager", "Sales Representative", "Research Director", "Human Resources"])
    job_level = st.slider("Level Pekerjaan", 1, 5, 2)
    monthly_income = st.number_input("Pendapatan Bulanan", min_value=1000, value=5000)
    overtime = st.selectbox("Kerja Lembur", ["Yes", "No"])
    stock_level = st.selectbox("Stock Option Level", [0, 1, 2, 3])

with col3:
    marital = st.selectbox("Status Pernikahan", ["Single", "Married", "Divorced"])
    total_working = st.number_input("Total Tahun Bekerja", min_value=0, value=10)
    years_at_co = st.number_input("Tahun di Perusahaan", min_value=0, value=5)
    gender = st.selectbox("Jenis Kelamin", ["Male", "Female"])
    education_field = st.selectbox("Bidang Pendidikan", ["Life Sciences", "Medical", "Marketing", "Technical Degree", "Other", "Human Resources"])

# --- 4. PROSES PREDIKSI ---
if st.button("🚀 Prediksi Sekarang"):
    
    # Memanggil data asli sebagai template agar jumlah kolom sama persis dengan fit time
    df_temp = pd.read_csv(r'C:\Users\aryod\Downloads\employee_data.csv')
    
    # Drop kolom yang sama seperti di coding Colab
    cols_to_drop = ['Attrition', 'EmployeeId', 'EmployeeCount', 'Over18', 'StandardHours']
    df_temp = df_temp.drop(columns=[col for col in cols_to_drop if col in df_temp.columns], errors='ignore')
    
    # Ambil 1 baris dummy
    input_data = df_temp.iloc[[0]].copy()
    
    # Timpa kolom dummy dengan input user
    input_data['Age'] = age
    input_data['BusinessTravel'] = business_travel
    input_data['DailyRate'] = daily_rate
    input_data['Department'] = department
    input_data['DistanceFromHome'] = distance
    input_data['JobRole'] = job_role
    input_data['JobLevel'] = job_level
    input_data['MonthlyIncome'] = monthly_income
    input_data['OverTime'] = overtime
    input_data['StockOptionLevel'] = stock_level
    input_data['MaritalStatus'] = marital
    input_data['TotalWorkingYears'] = total_working
    input_data['YearsAtCompany'] = years_at_co
    input_data['Gender'] = gender
    input_data['EducationField'] = education_field

    # Re-run Label Encoding seperti di Colab (agar teks jadi angka)
    categorical_cols = input_data.select_dtypes(include=['object']).columns
    le = LabelEncoder()
    # Kita perlu fit encoder pada data asli dulu supaya mapping angkanya konsisten
    for col in categorical_cols:
        le.fit(df_temp[col].astype(str))
        input_data[col] = le.transform(input_data[col].astype(str))

    # Scaling
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)
    probability = model.predict_proba(input_scaled)

    st.divider()
    
    # --- 5. TAMPILKAN HASIL ---
    if prediction[0] == 1:
        st.error(f"### HASIL: BERPOTENSI RESIGN (1)")
        st.write(f"Keyakinan Model: **{probability[0][1]*100:.2f}%**")
        st.info("💡 **Rekomendasi:** Berikan perhatian khusus pada beban kerja dan keseimbangan waktu kerja (Work-Life Balance).")
    else:
        st.success(f"### HASIL: TETAP BERTAHAN (0)")
        st.write(f"Keyakinan Model: **{probability[0][0]*100:.2f}%**")
        st.balloons()

st.divider()
st.caption("Proyek Akhir Edutech - Aryo Dwi Haryanto")