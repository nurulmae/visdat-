import streamlit as st
import matplotlib.pyplot as plt


#buat data sampel
months = ['Jan', 'Feb', 'Mar', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
product_A_sales = [10, 20, 15, 25, 30, 45, 40, 50, 60, 55,65, 70]
product_B_sales = [5, 10, 8, 15, 18, 20, 22, 30, 25, 35, 40, 45]

#layout stremalit
st.title("Visualisasi penjualan produk")
st.sidebar.header("Pengaturan Grafik")
option = st.sidebar.selectbox("Pilih tipe visualisasi", ("Single Line Plot",
                                                         "Multiple & Customizations",
                                                         "Jenis Garis untuk Menunjukkan Tren",
                                                         "Subplot"))

#identitas kelompok
st.caption("Praktikum 3 - Mataplotlib Line Chart")
st.markdown("*Kelompok 23*")
st.markdown("""
    - Amru Abdurrahman Azzam - 0110122322
    - Hayatunnisa - 0110222118
    - Nurul Maedatul Awaliah - 0110122222
 """)

#single line plot
def line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label="Product A")
    ax.set_title('Penjualan produk A per bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Penjualan')
    st.pyplot(fig)

#multiple line plot & cutomization
def customize_line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label="Product A", color="red", linestyle='--', marker='o')
    ax.plot(months, product_B_sales, label="Product B", color="black", linestyle='-', marker='x')
    
    ax.set_title('Penjualan produk per bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Penjualan')
    ax.legend() 
    ax.grid(True)
    st.pyplot(fig)

#data sample tambahan
product_C_sales = [18,2,25,28,32,38,42,48,52,56,60,55]
product_D_sales = [7,9,11, 13,16,18,20,23,25,28,30,33]
def tren_line_plot():
    fig, axs = plt.subplots()
    axs.plot(months, product_C_sales, label="Product C", color="yellow", linestyle='-.', marker='o')
    axs.plot(months, product_D_sales, label="Product D", color="green", linestyle=':', marker='x')

    axs.set_title('Penjualan produk per bulan')
    axs.set_xlabel('Bulan')
    axs.set_ylabel('Penjualan')
    axs.legend()
    axs.grid(True)
    st.pyplot(fig)

#subplot
def subplots():
    fig, axs = plt.subplots(2, 1, figsize=(10, 8))

    #plot pertama untuk produk C
    axs[0].plot(months, product_C_sales, label='Product C', color='blue', marker='d')
    axs[0].set_title('Penjualan Produk C per Bulan')
    axs[0].set_xlabel('Bulan')
    axs[0].set_ylabel('Jumlah Penjualan')
    axs[0].legend()
    axs[0].grid(True)

    #plot pertama untuk produk D
    axs[1].plot(months, product_D_sales, label='Product D', color='red', marker='s')
    axs[1].set_title('Penjualan Produk D per Bulan')
    axs[1].set_xlabel('Bulan')
    axs[1].set_ylabel('Jumlah Penjualan')
    axs[1].legend()
    axs[1].grid(True)

    plt.tight_layout()
    st.pyplot(fig)
    

#logika untuk menampilkan visualisasi sesuai menu
if option == 'Single Line Plot':
    line_plot()
elif option == "Multiple & Customizations":
    customize_line_plot()
elif option == "Jenis Garis untuk Menunjukkan Tren":
    tren_line_plot()
elif option == "Subplot":
    subplots()