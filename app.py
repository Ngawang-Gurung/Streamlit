import streamlit as st  

import pandas as pd
import numpy as np
import seaborn as sns   # Static plots
import plotly.express as px # Interactive plots
import time

np.random.seed(42)

st.write("Hello World!")

# Write dataframe
st.header("Dataframe")
df = pd.DataFrame({
    'X': [1, 2, 3, 4, 5],
    'y': [10, 20, 30, 40, 50]
    })

df # This is same as st.write(df). Streamlit magic understands this.

# st.table(df)  # Static table

st.subheader('Another dataframe')
dataframe = pd.DataFrame(
    data=np.random.randn(5, 5)
    )

st.dataframe(dataframe.style.highlight_max(axis=0))

# Draw charts and maps
st.header("Charts and Maps")
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c']
     )

if st.checkbox("Show line chart"):
    st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
    )

# Check box to show or hide data 
if st.checkbox("Show map"):
    st.map(map_data)

# Plotting searborn charts
iris = sns.load_dataset("iris")
plot = sns.histplot(data=iris, x='sepal_width', kde=True)

if st.checkbox("Show seaborn chart"):
    st.pyplot(plot.get_figure())

# Plotting plotly charts
iris = px.data.iris()
fig = px.scatter(iris, x = "sepal_width", y = "sepal_length")

if st.checkbox("Show plotly chart"):
    st.plotly_chart(fig)

# Widgets
# Each element that is passed into st.sidebar is pinned to left

st.header("Widgets: Slider and Selectbox")
x = st.sidebar.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

# Selectbox for options
option = st.sidebar.selectbox(
    'Choose a number', df['X']
)

'You selected: ', option

# Layout
st.header("Layout")
left_column, right_column = st.columns(2)

with left_column:
    st.subheader("Left Column")
    st.button("Press me!")

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    st.subheader("Right Column")
    choice = st.radio('Sorting hat', 
                      ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {choice} house!")

# Show progress
st.header("Progress")
'Starting a long computation'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # Update the progress bar with each iteration

    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.05)

'... and now we\'re done'

