import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# defining random values in a dataframe using pandas and numpy
df = pd.DataFrame(
    np.random.randn(30, 10),
    columns=('col_no %d' % i for i in range(10))
)
st.dataframe(df)

# defining random values in a dataframe using pandas and numpy
df = pd.DataFrame(
    np.random.randn(30, 10),
    columns=('col_no %d' % i for i in range(10))
)
# Highlighting minimum value objects
st.dataframe(df.style.highlight_min(axis=0))

# defining random values in a dataframe in a dataframe using pandas and numpy
df = pd.DataFrame(
    np.random.randn(30, 10),
    columns=('col_no %d' % i for i in range(10))
)
# defining data in table
st.table(df)

# Defining Metrics
st.metric(label="Temperature", value="31 °C", delta="1.2 °C")

# Defining Columns
c1, c2, c3 = st.columns(3)

# Defining Metrics
c1.metric(label="Rainfall", value="100 cm", delta="10 cm")
c2.metric(label="Population", value="123 Billions", delta="1 Billions", delta_color="inverse")
c3.metric(label="Customers", value=100, delta=10, delta_color="off")
st.metric(label="Speed", value=None, delta=0)
st.metric(label="Trees", value="91456", delta="-1132649")

df = pd.DataFrame(
    np.random.randn(30, 10),
    columns=('col_no %d' % i for i in range(10))
)
# Defining multiple arguments in write function
st.write("Here is our Data", df, "Data is in dataframe format.\n\nWrite is Super function")


# Defining Random Values for Chart
df = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['a', 'b']
)
# Defining Chart
chart = alt.Chart(df).mark_bar().encode(
    x='a', y='b', tooltip=['a', 'b']
).interactive() # Make the chart interactive

# Passing chart in write() function
st.write(chart)