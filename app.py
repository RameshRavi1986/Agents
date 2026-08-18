import os

import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic


# Load environment variables
load_dotenv()


st.set_page_config(
    page_title="Hello Agent",
    page_icon="🤖",
    layout="wide"
)


st.title("🤖 Hello Agent")
st.subheader("CSV FAQ Agent")

st.write(
    "Upload one or more CSV files and ask a question about the information "
    "contained in them."
)


# Check API key
api_key = os.getenv("OPENAI_KEY")

if not api_key:
    st.error(
        "OPENAI_API_KEY was not found. Add it to your .env file "
        "before running the application."
    )
    st.stop()


# ---------------------------------------------------------
# File upload
# ---------------------------------------------------------

uploaded_files = st.file_uploader(
    "Upload CSV files",
    type=["csv"],
    accept_multiple_files=True
)


if not uploaded_files:
    st.info("Upload one or more CSV files to get started.")
    st.stop()


# ---------------------------------------------------------
# Read CSV files
# ---------------------------------------------------------

dataframes = []

for uploaded_file in uploaded_files:

    try:
        df = pd.read_csv(uploaded_file)

        dataframes.append(df)

        st.markdown(f"### 📄 {uploaded_file.name}")

        st.dataframe(
            df.head(),
            use_container_width=True
        )

    except Exception as e:
        st.error(
            f"Could not read {uploaded_file.name}: {e}"
        )


if not dataframes:
    st.error("No valid CSV files were uploaded.")
    st.stop()


# ---------------------------------------------------------
# Question input
# ---------------------------------------------------------

st.markdown("---")

question = st.text_input(
    "Ask a question about the uploaded data",
    placeholder="Example: What is the return policy for electronics?"
)


# ---------------------------------------------------------
# Ask the agent
# ---------------------------------------------------------

if st.button("Ask Agent", type="primary"):

    if not question.strip():
        st.warning("Please enter a question.")
        st.stop()

    with st.spinner("Reading the CSV data..."):

        try:

            llm = ChatAnthropic(
                model="claude-sonnet-4-6",
                max_tokens=1000,
                api_key=api_key
            )

            system_instructions = """
You are Hello Agent, a CSV FAQ assistant.

Your answers MUST come only from the information contained
in the uploaded Pandas DataFrames.

Rules:

1. Do not use general world knowledge.
2. Do not guess or invent information.
3. Search the uploaded data carefully before answering.
4. If the requested information cannot be found in the
   uploaded CSV data, say exactly:

   "I could not find this information in the uploaded files."

5. For questions involving numbers, calculate totals,
   averages, or other required values using the data.
6. Give the answer in clear, concise English.
7. Do not claim information that is not supported by the data.
"""

            agent = create_pandas_dataframe_agent(
                llm,
                dataframes,
                verbose=False,
                allow_dangerous_code=True,
                agent_type="tool-calling",
                prefix=system_instructions
            )

            response = agent.invoke(
                {
                    "input": question
                }
            )

            answer = response["output"]

            st.markdown("### 💬 Answer")
            st.success(answer)

        except Exception as e:

            st.error(
                f"Something went wrong while answering the question: {e}"
            )