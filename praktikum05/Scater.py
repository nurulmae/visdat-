import streamlit as st
import matplotlib.pyplot as plt

# Data dummy
suhu = [20, 22, 24, 26, 28, 30, 32, 34, 36]
penjualan = [50, 60, 70, 90, 100, 110, 130, 150, 180]

# Judul aplikasi
st.title('Visualisasi Hubungan Penjualan Es Krim dengan Suhu')

# Scatter plot menggunakan Matplotlib
fig, ax = plt.subplots()
ax.scatter(suhu, penjualan, color='blue')
ax.set_title('Hubungan Penjualan Es Krim dan Suhu')
ax.set_xlabel('Suhu (°C)')
ax.set_ylabel('Penjualan Es Krim')

# Tampilkan di Streamlit
st.pyplot(fig)

import streamlit as st
import matplotlib.pyplot as plt

# Data dummy (diambil dari screenshot lain yang berisi data)
suhu = [20, 22, 24, 26, 28, 30, 32, 34, 36]
penjualan = [50, 60, 70, 90, 100, 110, 130, 150, 180]

# Kustomisasi scatter plot
fig, ax = plt.subplots()
ax.scatter(suhu, penjualan, color='orange', s=100, edgecolor='black', alpha=0.7)
ax.set_title('Hubungan Penjualan Es Krim dan Suhu (Kustom)')
ax.set_xlabel('Suhu (°C)')
ax.set_ylabel('Penjualan Es Krim')
ax.grid(True)

# Tampilkan di Streamlit
st.pyplot(fig)

import streamlit as st
import matplotlib.pyplot as plt

# Data dummy
suhu = [20, 22, 24, 26, 28, 30, 32, 34, 36]
penjualan_kerja = [50, 60, 70, 80, 90, 100, 110, 120, 130]
penjualan_akhir_pekan = [60, 70, 80, 100, 110, 120, 140, 160, 200]

# Judul aplikasi
st.title('Visualisasi Perbandingan Penjualan Es Krim Berdasarkan Hari')

# Membuat figure dan axes untuk plot
fig, ax = plt.subplots()

# Scatter plot multiple
# Hari Kerja (Warna Hijau)
ax.scatter(suhu, penjualan_kerja, color='green', label='Hari Kerja', s=80)
# Akhir Pekan (Warna Ungu)
ax.scatter(suhu, penjualan_akhir_pekan, color='purple', label='Akhir Pekan', s=80)

# Kustomisasi judul dan label
ax.set_title('Penjualan Es Krim Berdasarkan Hari')
ax.set_xlabel('Suhu (°C)')
ax.set_ylabel('Penjualan Es Krim')

# Menampilkan legenda
ax.legend()

# Tampilkan di Streamlit
st.pyplot(fig)

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Data dummy
data = {
    'Suhu': [20, 22, 24, 26, 28, 30, 32, 34, 36],
    'Penjualan_Cokelat': [50, 60, 70, 80, 90, 100, 110, 120, 130],
    'Penjualan_Vanila': [60, 70, 80, 90, 100, 110, 120, 130, 140],
    'Penjualan_Stroberi': [40, 50, 60, 70, 80, 90, 100, 110, 120],
    'Kelembapan': [60, 65, 70, 75, 80, 85, 90, 95, 100]
}

# Konversi data ke DataFrame
df = pd.DataFrame(data)

# Judul aplikasi
st.title('Analisis Penjualan Es Krim Berdasarkan Suhu')

# Pilih jenis es krim
jenis_eskrim = st.selectbox('Pilih Jenis Es Krim:', ['Cokelat', 'Vanila', 'Stroberi'])

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Data dummy
data = {
    'Suhu': [20, 22, 24, 26, 28, 30, 32, 34, 36],
    'Penjualan_Cokelat': [50, 60, 70, 80, 90, 100, 110, 120, 130],
    'Penjualan_Vanila': [60, 70, 80, 90, 100, 110, 120, 130, 140],
    'Penjualan_Stroberi': [40, 50, 60, 70, 80, 90, 100, 110, 120],
    'Kelembapan': [60, 65, 70, 75, 80, 85, 90, 95, 100]
}


# Konversi data ke DataFrame
df = pd.DataFrame(data)

# Judul aplikasi
st.title('Analisis Penjualan Es Krim Berdasarkan Suhu')

# Pilih jenis es krim (Widget Streamlit)
jenis_eskrim = st.selectbox('Pilih Jenis Es Krim:', ['Cokelat', 'Vanila', 'Stroberi'])

# Menentukan kolom penjualan berdasarkan pilihan
if jenis_eskrim == 'Cokelat':
    penjualan = df['Penjualan_Cokelat']
elif jenis_eskrim == 'Vanila':
    penjualan = df['Penjualan_Vanila']
else:
    penjualan = df['Penjualan_Stroberi']

# Tampilkan tabel data
st.subheader('Data Penjualan dan Suhu')
st.dataframe(df)

# Membuat Scatter Plot (Bubble Chart)
fig, ax = plt.subplots()
scatter = ax.scatter(
    df['Suhu'], 
    penjualan, 
    c=df['Kelembapan'], 
    s=100, 
    cmap='coolwarm', 
    alpha=0.7
)

# Kustomisasi plot
ax.set_title(f'Hasil Penjualan {jenis_eskrim} vs Suhu dan Kelembapan')
ax.set_xlabel('Suhu (°C)')
ax.set_ylabel(f'Penjualan Es Krim ({jenis_eskrim})')

# Menambahkan Colorbar (Legenda Kelembapan)
fig.colorbar(scatter, label='Kelembapan (%)')

# Tampilkan plot di Streamlit
st.pyplot(fig)