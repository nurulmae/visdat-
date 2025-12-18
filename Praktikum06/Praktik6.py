import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Stacked Vertical Bar Chart")

# Data
stores = ['Store A', 'Store B', 'Store C']
male_population = [150, 200, 180]
female_population = [120, 230, 170]

# Grafik
fig, ax = plt.subplots()
x = np.arange(len(stores))

ax.bar(x, male_population, label='Male', color='blue')
ax.bar(x, female_population, bottom=male_population, label='Female', color='pink')

ax.set_xlabel('Stores')
ax.set_ylabel('Population')
ax.set_title('Population by Gender and Store')
ax.set_xticks(x)
ax.set_xticklabels(stores)
ax.legend()

# Tampilkan di Streamlit
st.pyplot(fig)

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.subheader("Membuat Stacked Vertical Bar Chart dengan Matplotlib")

# Data Transaksi Penjualan
stores = ['Store A', 'Store B', 'Store C']
product_a_sales = [200, 250, 300]
product_b_sales = [150, 300, 250]

fig, ax = plt.subplots()
x = np.arange(len(stores))

# Membuat batang bertumpuk
ax.bar(x, product_a_sales, label='Product A', color='blue')
ax.bar(x, product_b_sales, bottom=product_a_sales, label='Product B', color='green')

# Penyesuaian Label dan Judul
ax.set_xlabel('Stores')
ax.set_ylabel('Sales')
ax.set_title('Sales Transactions by Store')
ax.set_xticks(x)
ax.set_xticklabels(stores)
ax.legend()

# Tampilkan di Streamlit
st.pyplot(fig)

st.subheader("Kustomisasi Stacked Vertical Bar Chart")

for i in range(len(x)):
    plt.text(x[i], product_a_sales[i] / 2, str(product_a_sales[i]), ha='center', color='white')
    plt.text(x[i], product_a_sales[i] + product_b_sales[i] / 2, str(product_b_sales[i]), ha='center', color='black')

st.pyplot(fig)

import matplotlib.pyplot as plt
import numpy as np

# Data
stores = ['Store A', 'Store B', 'Store C']
male_population = [150, 200, 180]
female_population = [120, 230, 170]

# Bar positions
x = np.arange(len(stores))

# Membuat Stacked Bar Chart
plt.bar(x, male_population, label='Male', color='blue')
plt.bar(x, female_population, bottom=male_population, label='Female', color='pink')

# Penyesuaian
plt.xlabel('Stores')
plt.ylabel('Population')
plt.title('Population by Gender and Store')
plt.xticks(x, stores)
plt.legend()

# Tampilkan
plt.show()