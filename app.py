import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model dan label encoder
model = joblib.load('model.pkl')
label_encoders = {}  # Jika memang tidak ada encoding


st.title("🎓 Prediksi Risiko Dropout Mahasiswa")
st.write("Masukkan data di bawah ini untuk memprediksi apakah mahasiswa berpotensi dropout atau lulus.")

# Input dari user
tuition = st.selectbox("Tuition Fees Up to Date", [0, 1])
debtor = st.selectbox("Debtor", [0, 1])

grade_1 = st.slider("1st Semester Grade", 0.0, 200.0, 120.0)
grade_2 = st.slider("2nd Semester Grade", 0.0, 200.0, 120.0)
admission_grade = st.slider("Admission Grade", 0.0, 200.0, 140.0)

approved_1 = st.number_input("1st Semester Approved Units", 0, 20, 5)
approved_2 = st.number_input("2nd Semester Approved Units", 0, 20, 5)
enrolled_2 = st.number_input("2nd Semester Enrolled Units", 0, 20, 6)

unemployment = st.slider("Unemployment Rate (%)", 0.0, 25.0, 6.0)
gdp = st.slider("GDP per Capita", 0.0, 100000.0, 15000.0)

# Fitur yang digunakan
selected_features = [
    'Tuition_fees_up_to_date', 'Debtor',
    'Curricular_units_1st_sem_grade', 'Curricular_units_2nd_sem_grade',
    'Admission_grade', 'Curricular_units_1st_sem_approved',
    'Curricular_units_2nd_sem_approved', 'Curricular_units_2nd_sem_enrolled',
    'Unemployment_rate', 'GDP'
]

# Masukkan data ke DataFrame
df_input = pd.DataFrame([{
    'Tuition_fees_up_to_date': tuition,
    'Debtor': debtor,
    'Curricular_units_1st_sem_grade': grade_1,
    'Curricular_units_2nd_sem_grade': grade_2,
    'Admission_grade': admission_grade,
    'Curricular_units_1st_sem_approved': approved_1,
    'Curricular_units_2nd_sem_approved': approved_2,
    'Curricular_units_2nd_sem_enrolled': enrolled_2,
    'Unemployment_rate': unemployment,
    'GDP': gdp
}], columns=selected_features)

# Encode kolom kategorikal jika ada
for col in label_encoders:
    le = label_encoders[col]
    val = df_input.loc[0, col]
    try:
        df_input[col] = le.transform([val])
    except Exception as e:
        st.error(f"Nilai '{val}' tidak dikenali untuk kolom {col}: {e}")
        st.stop()

# Tombol prediksi
if st.button("🔍 Prediksi"):
    prediction = model.predict(df_input)[0]
    proba = model.predict_proba(df_input)[0][1] * 100  # Probabilitas Dropout

    st.subheader("📊 Hasil Prediksi:")
    if prediction == 1:
        st.warning(f"⚠️ Mahasiswa ini diprediksi **Dropout** dengan probabilitas {proba:.2f}%")
    else:
        st.success(f"✅ Mahasiswa ini diprediksi **Lulus (Graduate)** dengan probabilitas Dropout {proba:.2f}%")
