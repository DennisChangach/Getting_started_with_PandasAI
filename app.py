import streamlit as st
import pandas as pd
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai
from dotenv import load_dotenv
from pandasai import SmartDataframe
import os

# Load environment variables
load_dotenv()

#reading the csv file
data  = pd.read_csv("Data\demo_data.csv")


st.set_page_config(page_title = "Caantin AI",page_icon = "🧠",
                       menu_items = {
                           'About':"""  # Caantin AI 
                                        An AI Powered Analysis & Visualization platform. 
                                        
                          """

                       })

st.title("💬 Chat with Your Data:📊")

# Configure the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
#os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
# Load the LLM - Gemini Pro
langchain_llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)


#instatioating the dataframe

gemini = SmartDataframe(data,config = {"llm":langchain_llm})


question = st.text_input("What are you curious about")

if st.button("Ask Question"):
    response = gemini.chat(question)
    st.write(response)

