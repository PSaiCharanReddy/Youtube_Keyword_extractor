import streamlit as st 
from bs4 import BeautifulSoup
import requests
st.markdown("<h1 style='text-align:center'>Youtube Keyword Extractor</h1>",unsafe_allow_html=True)
st.markdown("---",unsafe_allow_html=True)
urls=st.text_input("Youtube url here ")
if urls:
    page=requests.get(url=urls)
    soup=BeautifulSoup(page.content, 'lxml')
    meta=soup.select("meta[name='keywords']")
    title=soup.find('title')
    key=(meta[0]["content"])
    st.title("Title")
    st.markdown(f"<h5 style='color:purple'>{title.text}</h5>",unsafe_allow_html=True)
    st.title('Tags')
    st.markdown(f"<h5 style='color:purple'>{key}</h5>",unsafe_allow_html=True)