import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(500,2)/[50,50]+[37.76,-122.4],colums=['lat','lon'])
st.map(df)
