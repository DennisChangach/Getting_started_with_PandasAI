import streamlit as st
import pandas as pd
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai
from dotenv import load_dotenv
from pandasai import SmartDataframe
from pandasai import SmartDatalake
from pandasai.llm import BambooLLM
from pandasai import Agent
import os

# Load environment variables
load_dotenv()

#Configuring Langsmith
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Configure the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Dictionary to store the extracted dataframes
data = {}

def main():
    st.set_page_config(page_title = "PandasAI",page_icon = "🐼")
    st.title("💬 Chat with Your Data using PandasAI:🐼")
    #reading the csv file
    
    #Side Menu Bar
    with st.sidebar:
        st.title("Configuration:⚙️")
        #Activating Demo Data
        st.text("Data Setup: 📝")
        file_upload = st.file_uploader("Upload your Data",accept_multiple_files=False,type = ['csv','xls','xlsx'])

        st.warning("Please ensure the first row has the column names.")

        #selecting LLM to use
        llm_type = st.selectbox(
                            "Please select LLM",
                            ('Bamboo','gemini-pro'),index=0)

    if file_upload is not None:
        data  = extract_dataframes(file_upload)
        df = st.selectbox("Here's your uploaded data!",
                          tuple(data.keys()),index=0
                          )
        st.dataframe(data[df])

        #Creating LLM object based on the llm type selected:
        if llm_type == 'Bamboo':
            llm = BambooLLM()
        elif llm_type =='gemini-pro':
            llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
        

        analyst = get_analyst(data)


        question = st.text_input("What are you curious about")

        if st.button("Ask Question"):
            response = analyst.chat(question)
            st.write(response)

        if st.button("Explain"):
            explanation = analyst.explain()
            st.write(explanation)
        

    else:
        st.warning("Please upload your data first! You can upload a CSV or an Excel file.")


def get_analyst(data):
    """
    The function creates a data lake based on the dataframes exctracted from the uploaded files
    input: Dictionary
    Output: SmartDatalake or Agent
    """
    lake = Agent(list(data.values()))

    return lake


def extract_dataframes(raw_file):
    """
    This function extracts dataframes from the uploaded file/files
    imput: Upload_File object & type of file
    Processing: Based on the type of file read_csv or read_excel to extract the dataframes
    Output: Should return a dictionary with the dataframes
    
    """
    dfs = {}
    if raw_file.name.split('.')[1] == 'csv':
        csv_name = raw_file.name.split('.')[0]
        df = pd.read_csv(raw_file)
        dfs[csv_name] = df

    elif (raw_file.name.split('.')[1] == 'xlsx') or (raw_file.name.split('.')[1] == 'xls') :
        # Read the Excel file
        xls = pd.ExcelFile(raw_file)

        # Iterate through each sheet in the Excel file and store them into dataframes
        dfs = {}
        for sheet_name in xls.sheet_names:
            dfs[sheet_name] = pd.read_excel(raw_file, sheet_name=sheet_name)

    #return the dataframes
    return dfs

if __name__ == "__main__":
    main()


