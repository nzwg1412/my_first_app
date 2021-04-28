import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time


dt = pd.read_csv("treatmentpara.csv")
df = pd.read_csv("fractures.csv")

# st.title("streamlit demo")
# st.write("""s
# Hello *world!!*
# """)
# st.write("""
# Here are our dataset prepared for machine learning methods:
#     """)
# st.write(pd.DataFrame(df))


"""
# My first app
Here are our dataset prepared for machine learning methods:
"""
if st.checkbox("Show the treatment parameters"):
    dt = pd.read_csv("fractures.csv")
    dt

option = st.sidebar.selectbox(
    'Please select the stage_fluid',
    dt.iloc[:,1])

'You selected: ', option

option = st.selectbox(
    'Please select the volume',
    dt.iloc[:,2])

'You selected: ', option

option = st.selectbox(
    'Please select the sand rate',
    dt.iloc[:,3])

'You selected: ', option
option = st.selectbox(
    'Please select the preratio',
    dt.iloc[:,4])

'You selected: ', option



if st.checkbox("Show the fractures' parameters"):
    df = pd.read_csv("fractures.csv")
    df

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data
########好玩###########
st.write("""
*Break Time!!*
""")
left_column, right_column = st.beta_columns(2)
pressed = left_column.button('Press me?')
if pressed:
    right_column.write("Woohoo!")

expander = st.beta_expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")

'Starting a long computation...'
# st.empty()
# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'

# @st.cache
# def load_data(path):
#     df = pd.read_csv(path)
#     df.columns = df.columns.str.lower()
#     df["date"] = pd.to_datetime(df["transaction_date"]).dt.date
#     df["price"] = df["price"].str.replace(",","").astype(float)
#     return df

# df = load_data("SalesJan2009.csv")
# st.write(f.run(window=15))
# 
# 
# chart_data = pd.DataFrame(
#      np.random.randn(20, 3),
#      columns=['a', 'b', 'c'])

# st.line_chart(chart_data)
# chart_data = pd.DataFrame(df.iloc[:,1])

# print(df.iloc[:,1])
# st.bar_chart(pd.DataFrame(df.iloc[:,1]))
# st.bar_chart(pd.DataFrame(df.iloc[:,2]))
# st.bar_chart(pd.DataFrame(df.iloc[:,3]))
# st.bar_chart(pd.DataFrame(df.iloc[:,4]))

# 
# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])

# st.map(map_data)
# 
# 
# 
