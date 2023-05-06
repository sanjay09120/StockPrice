import streamlit as st
from PIL import Image
import pickle
model = pickle.load(open('model.pkl', 'rb'))

with st.form(key='my_form'):
    st.title("Stock Market Prediction")
    opn = st.number_input("Open Price")
    high = st.number_input("Highest price")
    low = st.number_input("Lowest Price")
    close = st.number_input("Closing Price");
    adjclose = st.number_input("Adjacent Closing Price")
    volume = st.number_input("Stock Volume")


    submit_button = st.form_submit_button(label='Submit')

    features = [[opn, high, low, close, adjclose, volume]]
    # st.write(features)
    prediction = model.predict(features)
    st.write(prediction)
   # lc = [str(i) for i in prediction]
   # ans = int("".join(lc))



