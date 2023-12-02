import requests
import streamlit as st

st.title("Image Captioning")
API_URL = "https://api-inference.huggingface.co/models/nlpconnect/vit-gpt2-image-captioning"
headers = {"Authorization": "Bearer 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"}


def query(filename):
    data = filename
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()


inp_img_link = st.text_input("Enter Image Link")
button_sub = st.button("Submit")
try:
    if button_sub:
    st.image(inp_img_link, caption="Uploaded Image")
# output = query("https://st.depositphotos.com/1718692/3527/i/450/depositphotos_35272435-stock-photo-forest-on-a-steep-mountain.jpg")
    output = query(inp_img_link)
    st.write(output[0]['generated_text'])
except:
    st.write("Enter Valid Image Link")