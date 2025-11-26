import streamlit as st
import matplotlib.pyplot as plt

# Buat Data Sample
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'ags', 'sep', 'oct', 'nov', 'dec']
Product_A_sales = [10, 20, 15, 25, 30, 45, 40, 50, 60, 55, 65, 70]
Product_B_sales = [5, 10, 8, 15, 18, 20, 22, 30, 25, 35, 40, 45]

# layout streamlit
st.title("Visualisasi penjualan produk")
st.sidebar.header("pengaturan grafik")
option = st.sidebar.selectbox("pilih tipe visualisasi",("single line plot" ,
                                                        "multiple&Customizations",
                                                        "jenis garis untuk menunjukan tren",
                                                        "subplot"))
# identitas kelompok 
st.caption("praktikum 3 - matplotlib line chart")
st.markdown("""
kelompok : 
         - nama anggota (nim)  - nama anggota (nim)
            """)

# Single Line Plot
def line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, Product_A_sales, label="Product A")
    ax.set_title('Penjualan Produk A per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Penjualan')
    ax.show()
    st.pyplot(fig)


# Multiple Line Plot & Customizations
def customize_line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, Product_A_sales, label='Product A', color='blue', linestyle='-', marker='o')
    ax.plot(months, Product_B_sales, label='Product B', color='red', linestyle='--', marker='x')
    ax.set_title('Penjualan Produk Per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Penjualan')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

def trend_lines_plot():
    fig, ax = plt.subplots()
    ax.plot(months, Product_A_sales, label='Product A Trend', linestyle='--', color='blue')
    ax.plot(months, Product_B_sales, label='Product B Trend', linestyle='--', color='red')
    ax.set_title('Tren Penjualan Produk Per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Penjualan')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)
def subplots():
    fig, axs = plt.subplots(2, 1, figsize=(10, 8))

    # Plot for Product A
    axs[0].plot(months, Product_A_sales, label='Product A', color='blue', marker='o')
    axs[0].set_title('Penjualan Produk A Per Bulan')
    axs[0].set_xlabel('Bulan')
    axs[0].set_ylabel('Jumlah Penjualan')
    axs[0].legend()
    axs[0].grid(True)

    # Plot for Product B
    axs[1].plot(months, Product_B_sales, label='Product B', color='red', marker='x')
    axs[1].set_title('Penjualan Produk B Per Bulan')
    axs[1].set_xlabel('Bulan')
    axs[1].set_ylabel('Jumlah Penjualan')
    axs[1].legend()
    axs[1].grid(True)

    plt.tight_layout()
    st.pyplot(fig)

if option == "Line Plot":
    line_plot()
elif option == "Kustomisasi Line Plot":
    customize_line_plot()
elif option == "Garis Berbeda untuk Menunjukkan Trend":
    trend_lines_plot()
elif option == "Subplot":
    subplots()