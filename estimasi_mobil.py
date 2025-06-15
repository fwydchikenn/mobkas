import pickle
import streamlit as st

model = pickle.load(open('estimasi_mobil.sav', 'rb'))
st.title('ESTIMASI HARGA MOBIL BEKAS')
st.subheader('Mau beli mobil bekas?Jangan Kira-Kira, Cek di Sini!')


Model_Mobil = ['Auris', 'Avensis', 'Aygo', 'C-HR', 'Camry', 'Corolla', 'GT86', 'Hilux', 'IQ', 'Land Cruiser', 'PROACE VERSO', 'Prius', 'RAV4', 'Supra', 'Urban Cruiser', 'Verso', 'Verso-S', 'Yaris'            ]


pilihan = st.selectbox(
    'Pilih Model Mobil Anda:',
    Model_Mobil
)



year = st.number_input('Input Tahun Keluaran Mobil')
mileage = st.number_input('Input KM Mobil')
tax = st.number_input('Input Pajak Mobil')
mpg = st.number_input('Input Konsumsi BBM Mobil')
engineSize = st.number_input('Input Kapasitas Mesin')
predict = ''
if st.button('Estimasi Harga'):
    predict = model.predict(
        [[year, mileage, tax, mpg, engineSize]]
    )
    st.write('Estimasi harga mobil bekas dalam pounds: ', predict)
    st.write('Estimasi harga mobil bekas dalam IDR (Juta): ',predict*22000)



