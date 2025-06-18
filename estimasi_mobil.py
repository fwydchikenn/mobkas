import pickle
import streamlit as st

# Mengatur konfigurasi halaman Streamlit
st.set_page_config(
    page_title="Estimasi Harga Mobil Bekas",
    page_icon="",
    layout="centered",
    initial_sidebar_state="auto"
)

# Memuat model
model = pickle.load(open('estimasi_mobil.sav', 'rb'))

# --- Header Aplikasi ---
st.markdown(
    """
    <style>
    .main-header {
        font-size: 3.5em;
        font-weight: bold;
        color: #4CAF50; /* Hijau cerah */
        text-align: center;
        margin-bottom: 0.5em;
        text-shadow: 2px 2px 4px #aaaaaa;
    }
    .subheader {
        font-size: 1.5em;
        color: #555555;
        text-align: center;
        margin-bottom: 2em;
    }
    .stButton>button {
        background-color: #4CAF50; /* Hijau cerah */
        color: white;
        font-size: 1.2em;
        padding: 10px 24px;
        border-radius: 8px;
        border: none;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #45a049; /* Sedikit lebih gelap saat hover */
        box-shadow: 3px 3px 6px rgba(0,0,0,0.3);
    }
    .stNumberInput>div>div>input {
        background-color: #f0f2f6; /* Warna input field */
        border-radius: 5px;
        padding: 10px;
        border: 1px solid #cccccc;
    }
    .stSelectbox>div>div {
        background-color: #f0f2f6; /* Warna selectbox */
        border-radius: 5px;
        border: 1px solid #cccccc;
    }
    .result-box {
        background-color: #e8f5e9; /* Latar belakang untuk hasil */
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #4CAF50;
        margin-top: 2em;
        font-size: 1.2em;
        color: #333333;
    }
    </style>
    <div class="main-header">🚗 Estimasi Harga Mobil Bekas 🚗</div>
    <div class="subheader">Jangan Kira-Kira, Cek di Sini!</div>
    """,
    unsafe_allow_html=True
)

# --- Input Pengguna ---
st.write("---") # Garis pemisah
st.subheader("Detail Mobil Anda:")

Model_Mobil = [
    'Auris', 'Avensis', 'Aygo', 'C-HR', 'Camry', 'Corolla', 'GT86', 'Hilux', 'IQ',
    'Land Cruiser', 'PROACE VERSO', 'Prius', 'RAV4', 'Supra', 'Urban Cruiser',
    'Verso', 'Verso-S', 'Yaris'
]

pilihan = st.selectbox(
    'Pilih Model Mobil Anda:',
    Model_Mobil
)

col1, col2 = st.columns(2)

with col1:
    year = st.number_input('Tahun Keluaran Mobil (cth: 2018)', min_value=1990, max_value=2025, value=2015)
    mileage = st.number_input('Jarak Tempuh Mobil (KM)', min_value=0, value=50000)
    tax = st.number_input('Pajak Tahunan Mobil (Pounds)', min_value=0, value=150)

with col2:
    mpg = st.number_input('Konsumsi BBM (MPG - Miles per Gallon)', min_value=0.0, value=45.0, format="%.1f")
    engineSize = st.number_input('Kapasitas Mesin (CC)', min_value=0.0, max_value=5.0, value=1.5, format="%.1f")

st.write("---") # Garis pemisah

# --- Tombol Prediksi dan Hasil ---
predict = ''
if st.button('Estimasi Harga Sekarang!'):
    predict = model.predict(
        [[year, mileage, tax, mpg, engineSize]]
    )
    
    st.markdown('<div class="result-box">', unsafe_allow_html=True)
    st.write(f'**Model Mobil Anda:** `{pilihan}`') # Menampilkan jenis mobil yang dipilih
    st.markdown("---") # Garis pemisah dalam result box

    # Menggunakan kolom untuk menampilkan prediksi
    col_pounds, col_idr = st.columns(2)

    with col_pounds:
        st.metric(label="Estimasi Harga (Pounds)", value=f"£{predict[0]:,.2f}")
    
    with col_idr:
        idr_price = predict[0] * 22000
        st.metric(label="Estimasi Harga (IDR Juta)", value=f"Rp{idr_price:,.2f}")
    
    st.markdown('</div>', unsafe_allow_html=True)

st.sidebar.markdown("### Tentang Aplikasi Ini")
st.sidebar.info(
    "Aplikasi ini membantu Anda mengestimasi harga mobil bekas berdasarkan beberapa parameter. "
    "Data yang digunakan untuk model adalah mobil yang dijual di pasar."
)