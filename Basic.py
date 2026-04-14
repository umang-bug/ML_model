import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("hello World")
st.subheader("welcome to my app")
st.write("this is a simple streamlit app to demonstrate how to deploy a machine learning")

option = st.radio("Choose an option", ["option 1","option 2","option 3"])
