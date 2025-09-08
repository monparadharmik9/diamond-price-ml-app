import streamlit as st
import pandas as pd
import pickle as pk

try:
    regressor = pk.load(open("diamond_regressor.pkl", "rb"))
    scaler = pk.load(open("diamond_scaler.pkl", "rb"))
except FileNotFoundError:
    st.error("Model or scaler file not found. Please upload the required `.pkl` files.")
    st.stop()

st.header("💎 Diamond Price Prediction System")

carat = st.number_input("Carat",0.01, 500.5)

cut = st.selectbox("GIA Cut Grading System", ['Ideal', 'Premium', 'Good', 'Fair', 'Very Good'])
cut_map = {'Ideal': 0, 'Premium': 1, 'Good': 2, 'Fair': 3, 'Very Good': 4}
cut_s = cut_map[cut]
st.image("GIA-cut-grading.png", caption="GIA cut Grading")


color = st.selectbox("Color Priority", ['D', 'E', 'F', 'G', 'H', 'I', 'J'])
color_map = {'D': 0, 'E': 1, 'F': 2, 'G': 3, 'H': 4, 'I': 5, 'J': 6}
color_s = color_map[color]
st.image("diamond-color-priority.png", caption="Diamond color Priority")

clarity = st.selectbox("Clarity", ['SI1', 'SI2', 'VS1', 'VS2', 'VVS1', 'VVS2', 'IF', 'FL'])
clarity_map = {'SI1': 0, 'SI2': 1, 'VS1': 2, 'VS2': 3, 'VVS1': 4, 'VVS2': 5, 'IF': 6, 'FL': 7}
clarity_s = clarity_map[clarity]
st.image("diamond-Clarity.png", caption="Clarity")

depth = st.number_input("Depth", 42, 80, step= 1)

table = st.number_input("Table", 42, 95, step= 1)

x = st.number_input("X (mm)", 0.00, 10.74, step = 0.2)
y = st.number_input("Y (mm)", 0.00, 58.90, step = 0.2)
z = st.number_input("Z (mm)", 0.00, 31.80, step=0.1)

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://images.unsplash.com/photo-1664044020180-b75bfddf9776?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8ZGlhbW9uZCUyMGJhY2tncm91bmR8ZW58MHx8MHx8fDA%3D");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
    }}
    </style>
    """,
    unsafe_allow_html=True
)


if st.button("Predict"):
    input_data = pd.DataFrame([[
        carat, cut_s, color_s, clarity_s, depth, table, x, y, z
    ]], columns=[
        'carat', 'cut', 'color', 'clarity', 'depth', 'table', 'x', 'y', 'z'
    ])

    input_scaled = scaler.transform(input_data)
        
    prediction = regressor.predict(input_scaled)

    st.markdown(f"Predicted Diamond Price: ₹ {prediction[0]:,.2f}")
    st.success("Your diamond is worth this much! ✨")