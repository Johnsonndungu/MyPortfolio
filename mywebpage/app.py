import streamlit as st
from pathlib import Path
from PIL import Image


about= st.Page(
    page="views/about.py",
    title= 'About me',
    default=True,
)
chatbot_page = st.Page(
    page= "views/chatbot.py",
    title="Ask me",
)
#Navigation Menu

pg = st.navigation(pages=[about,chatbot_page])

pg.run()                       