import streamlit as st
from rembg import remove
from PIL import Image
from streamlit_image_comparison import image_comparison
import easyocr as ocr
import numpy as np

#set page config
st.set_page_config(page_title = "My_First_Image_App", layout ='centered')
st.subheader('[미니프로젝트]이미지 배경제거 + 글자추출 웹서비스')
st.markdown("### :arrow_forward::sunglasses: Remove Background")
st.markdown('#### sample result')

uploaded_file = st.file_uploader("이미지를 업로드하세요", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    input = Image.open(uploaded_file)
    st.image(input, caption='원본 이미지', use_column_width=True)
    output = remove(input) #배경제거된 파일
    st.image(output, caption='배경 제거 이미지', use_column_width=True)
