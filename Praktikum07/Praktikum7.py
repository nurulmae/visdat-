import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Penjualan Smartphone Berdasarkan Merek")
st.subheader("Horizontal Bar Chart Sederhana")

# Data Penjualan Smartphone
brands = ['Brand A', 'Brand B', 'Brand C', 'Brand D']
sales = [350, 420, 300, 280]

# Membuat Horizontal Bar Chart
fig, ax = plt.subplots()
y = np.arange(len(brands))  # Posisi untuk batang
ax.barh(y, sales, color='skyblue')
ax.set_yticks(y)
ax.set_yticklabels(brands)
ax.set_xlabel('Total Sales (in Units)')
ax.set_title('Smartphone Sales by Brand')

# Tampilkan di Streamlit
st.pyplot(fig)

# Warna berbeda untuk setiap batang
colors = ['blue', 'green', 'orange', 'red']

fig, ax = plt.subplots()
ax.barh(y, sales, color=colors)

# Menambahkan nilai pada batang
for i, v in enumerate(sales):
    ax.text(v + 10, i, str(v), color='black', va='center')  # Posisi teks

ax.set_yticks(y)
ax.set_yticklabels(brands)
ax.set_xlabel('Total Sales (in Units)')
ax.set_title('Customized Smartphone Sales by Brand')

# Tampilkan di Streamlit
st.pyplot(fig)

st.subheader("Multiple Horizontal Bar Chart")

# Data Penjualan
brands = ['Brand A', 'Brand B', 'Brand C', 'Brand D']
q1_sales = [350, 400, 300, 250]
q2_sales = [370, 420, 310, 280]

bar_width = 0.4  # Lebar batang
y = np.arange(len(brands))

fig, ax = plt.subplots()

# Membuat Multiple Horizontal Bar Chart
ax.barh(y - bar_width / 2, q1_sales, height=bar_width, label='Q1 Sales', color='skyblue')
ax.barh(y + bar_width / 2, q2_sales, height=bar_width, label='Q2 Sales', color='salmon')

# Penyesuaian tampilan
ax.set_yticks(y)
ax.set_yticklabels(brands)
ax.set_xlabel('Total Sales (in Units)')
ax.set_title('Smartphone Sales by Brand (Multiple Periods)')
ax.legend()

# Tampilkan di Streamlit
st.pyplot(fig)

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Contoh data penjualan
brands = ['Brand A', 'Brand B', 'Brand C']
sales_2022 = [350, 450, 300]
sales_2023 = [400, 500, 320]

def create_stacked_bar_chart():
    fig, ax = plt.subplots(figsize=(10, 6))
    y = np.arange(len(brands))
    ax.barh(y, sales_2022, label='2022', color='skyblue')
    ax.barh(y, sales_2023, left=sales_2022, label='2023', color='orange')
    ax.set_yticks(y)
    ax.set_yticklabels(brands)
    ax.set_xlabel('Sales')
    ax.set_title('Smartphone Sales by Brand')
    ax.legend()
    return fig

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Contoh data penjualan
brands = ['Brand A', 'Brand B', 'Brand C']
sales_2022 = [350, 450, 300]
sales_2023 = [400, 500, 320]

def create_stacked_bar_chart():
    fig, ax = plt.subplots(figsize=(10, 6))
    y = np.arange(len(brands))
    ax.barh(y, sales_2022, label='2022', color='skyblue')
    ax.barh(y, sales_2023, left=sales_2022, label='2023', color='orange')
    ax.set_yticks(y)
    ax.set_yticklabels(brands)
    ax.set_xlabel('Sales')
    ax.set_title('Smartphone Sales by Brand')
    ax.legend()
    return fig

# Render chart di Streamlit
st.title("Smartphone Sales Visualization")
st.pyplot(create_stacked_bar_chart())

def create_custom_stacked_bar_chart():
    fig, ax = plt.subplots(figsize=(10, 6))
    y = np.arange(len(brands))
    
    # Bar 2022 dengan pola hatch
    ax.barh(y, sales_2022, label='2022', color='blue', edgecolor='black', hatch='//')
    # Bar 2023 dengan pola hatch
    ax.barh(y, sales_2023, left=sales_2022, label='2023', color='green', edgecolor='black', hatch='\\')
    
    ax.set_yticks(y)
    ax.set_yticklabels(brands)
    ax.set_xlabel('Sales')
    ax.set_title('Customized Smartphone Sales by Brand')
    ax.legend()
    
    # Tambahkan anotasi angka di dalam batang
    for i in range(len(brands)):
        ax.text(sales_2022[i] / 2, i, f"{sales_2022[i]}", va='center', color='white')
        ax.text(sales_2022[i] + sales_2023[i] / 2, i, f"{sales_2023[i]}", va='center', color='black')
        
    return fig

st.pyplot(create_custom_stacked_bar_chart())