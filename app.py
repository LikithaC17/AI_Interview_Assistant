import streamlit as st
from groq import Groq

st.set_page_config(page_title='AI_Interview_Assistant', layout= 'centered')
st.title('AI_Interview_Assistant')
st.caption('Practice Interview with AI generated question')
st.caption('Launch by Likitha')
st.write('Department of AI&DS')

try:
  client=Groq(apl_key=st.secrets['GROG_API_KEY'])
  st.write("API connection Successfull")
except(KeyError, FileNotFoundError):
  st.error('Groq_API is missing. Add it to the Streamlit Cloud')
  st.stop()

