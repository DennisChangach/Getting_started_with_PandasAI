# Chat with Your Data using PandasAI and Streamlit
This repository provides a Streamlit app that leverages PandasAI to enable you to have an interactive conversation with your data! Ask questions about your CSV or Excel files in plain English and get clear, actionable insights directly within the app.

## What is PandasAI?
PandasAI seamlessly integrates with pandas, the go-to library for data manipulation in Python. It empowers you to interact with your data conversationally. Imagine asking questions like "What are the top 5 countries by sales?" or "Show me a scatter plot of customer age vs. purchase amount." PandasAI utilizes large language models (LLMs) to understand your natural language queries and then interacts with your data using pandas to deliver results.

## Key Features of the App
- Intuitive Interface: The Streamlit framework provides a user-friendly interface for uploading your data, selecting the LLM, and interacting with your data through a chat window.
- Natural Language Conversation: Ask questions about your data in plain English, eliminating the need to write complex code.
- Automatic Insights: PandasAI can not only answer your questions but also generate data visualizations like charts and graphs, providing a more holistic understanding of your data.
- Multiple LLM Support: The app allows you to choose between different LLMs like BambooLLM or Gemini-pro, depending on your preference and requirements..

## How to Use the App
**Clone the Repository:**
Use git clone [invalid URL removed] to clone this repository to your local machine. (Replace 'your-username' and 'your-repo-name' with your details)

**Install Dependencies:**
Navigate to the cloned repository directory and run `pip install -r requirements.txt` to install the required Python libraries.

**Run the App:**
Within the project directory, execute `streamlit run main.py` to launch the Streamlit app in your web browser.

**Interact with the App:**
- Upload your CSV or Excel data file.
- Select the desired LLM from the dropdown menu. (Provide your API key).
- Ask questions about your data in the chat window. The app will analyze your data and respond to your questions with clear and informative answers.

Additional Notes
- You can read more on the project here: Medium Article
- Here's the link to the app on Streamlit Cloud:
