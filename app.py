
import streamlit as st
import pandas as pd


st. write ('# 설비 장비 요청 작업 현황')
view = [100,150,30]
view

st.bar_chart(view)

sview = pd.Series(view)
sview