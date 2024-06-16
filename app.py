import streamlit as st
import os
import langchain
from langchain.prompts import PromptTemplate
import google.generativeai as genai

os.environ['Key'] = st.secrets['API_key']
genai.configure(api_key=os.environ['Key'])

## Function To get response from Gemini model

def getLLamaresponse(input_text, no_words, blog_style):
    ### Gemini 1.5 flash model
    llm = genai.GenerativeModel('gemini-1.5-flash-latest')

    ## Prompt Template
    template = """
        Write a blog for {blog_style} job profile for a topic {input_text}
        within {no_words} words.
            """

    prompt = PromptTemplate(input_variables=["blog_style", "input_text", 'no_words'],
                            template=template)

    ## Generate the ressponse from the Gemini model
    response = llm.generate_content(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
    print(response.text)
    return response.text


st.set_page_config(page_title="Abeeds's Blog Generator",
                   page_icon='🤖',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header("Generate Blogs 🤖")

input_text = st.text_input("Enter the Blog Topic")

## creating to more columns for additonal 2 fields

col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input('No of Words')
with col2:
    blog_style = st.selectbox('Writing the blog for',
                              ('Researcher', 'Data Scientist', 'General', 'Developer', 'Fresher','Business'), index=0)

submit = st.button("Generate")

## Final response
if submit:
    st.write(getLLamaresponse(input_text, no_words, blog_style))
