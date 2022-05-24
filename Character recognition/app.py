import numpy as np
import streamlit as st
import pytesseract as pt
from PIL import Image #python Imaging library, to open image, streamlit does not support cv2 directly

st.set_option('deprecation.showfileUploaderEncoding',False) #to warning ignore
st.title("*Optical Character Recognition*")  #print title and text
st.text("Upload the Image file by clicking Browse button")

uploaded_file=st.sidebar.file_uploader("Drag and Drop or Choose an image...",type=['jpg','png','jpeg'])
if uploaded_file is not None:
  img=Image.open(uploaded_file) #reads the image,similar to cv2.imread
  st.image(img,caption="uploaded Image",use_column_width=True) #similar to cv2.imwrite
  st.write("") #print black space

  if st.button("PREDICT"):  #creates a button called as predict
    st.write("Recognised characters by the image as below....")
    op=pt.image_to_string(img) # pytesseract converts img to text and prints
    st.title(op)
