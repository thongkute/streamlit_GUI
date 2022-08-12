import streamlit as st
import pandas as pd
import numpy as np
# import time

#------Page setup-------
st.set_page_config(
     page_title="Realtime Translator",
     page_icon= './icon/page_icon.png',
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
 )

#------Logo-------
left, _, right = st.columns(3)
with left:
    st.image('./icon/FRA_UAS_colored.png')
    st.markdown("""---""") 
with right:
    st.image('./icon/vgu_logo.png')
    st.markdown("""---""") 

# ------Title-------
_, mid, _ = st.columns([3,4,3])
with mid:
    title = st.title("Realtime Translator GUI")

# ------Mute Button-------
st.info("Click the box below to mute or umute the translated speech")
but, img, _ = st.columns([1,1,30])
with but:
    speaker = st.checkbox('')

with img:
    if speaker:
        st.image('./icon/mute.png')
    else:
        st.image('./icon/unmute.png')
        
# ------Main-------
# ger, but, eng = st.columns([5,0.5,5])
ger, eng = st.columns(2)

# with but:
#     change = st.button("click")
#     if change:
#         with ger:
#             st.subheader("English")  
#             st.markdown("""---""") 
#         with eng:
#             st.subheader("German")
#             st.markdown("""---""") 
#     else:
#         with ger:
#             st.subheader("German")
#             st.markdown("""---""") 
#         with eng:
#             st.subheader("English")    
#             st.markdown("""---""") 

with ger:
    with st.expander("German"):
        txt_1 = st.text_area("Input",key=1)
        # st.write('Sentiment:', run_sentiment_analysis(txt))
with eng:
    with st.expander("English"):
        txt_2 = st.text_area("Output",txt_1,key=2)

# st.select_slider("Speaker", ["Unmute", "Mute"])
