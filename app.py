import streamlit as st
from groq import Groq

st.set_page_config(page_title='AI_Interview_Assistant', layout= 'centered')
st.title('AI_Interview_Assistant')
st.caption('Practice Interview with AI generated question')
st.caption('Launch by Likitha')
st.write('Department of AI&DS')

try:
  client=Groq(api_key=st.secrets['GROQ_API'])
  st.write("API connection Successfull")
except(KeyError, FileNotFoundError):
  st.error('GROQ_API is missing. Add it to the Streamlit Cloud--> App setting')
  st.stop()

role= st.selectbox("Select Job Role", [
  "Python Developer",
  "Java Developer",
  "Data Analyst",
  "Machine Learning Engineering",
  "Software Enigineer",
  "HR Executive"
])

if st.button("Generate Interview Question"):

  prompt= "Generate 5 interview questions for the role of " + role 

response = client.chat.completions.create(
    model= "openai/gpt-oss-120b",
    messages= [
        {"role": "system", "content": "You are expert technical interviewer"},
        {"role": "user", "content": "prompt"}
    ]
)
output=response.choices[0].message.content

st.write(output)

  
