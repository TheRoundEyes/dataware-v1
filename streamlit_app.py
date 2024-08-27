import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_title="DataWare")

st.title("DataWare V1.0")

st.caption('DataWare is a simple ETL tool that allows you to Extract, Transform and Load data from a CSV file.')
#
# col1, col2 = st.columns(2)
#
#
# def extract_data(uploaded_file):
#     if uploaded_file is not None and uploaded_file.name.split('.')[-1] == 'csv':
#         df = pd.read_csv(uploaded_file)
#     elif uploaded_file is not None and uploaded_file.name.split('.')[-1] == 'json':
#         df = pd.read_json(uploaded_file)
#     elif uploaded_file is not None and uploaded_file.name.split('.')[-1] == 'xlsx':
#         excel_file = pd.ExcelFile(uploaded_file)
#         sheet_name = excel_file.sheet_names
#         selected_sheet = st.selectbox('Select a sheet', sheet_name)
#         if selected_sheet:
#             df = pd.read_excel(uploaded_file, sheet_name=selected_sheet)
#
#     return df
#
# def filter(df):
#     selected_column = st.selectbox('Select a column', df.columns)
#     if selected_column is not None:
#         filter_text = st.text_input('Enter a text to filter')
#         if filter:
#             df = df[df[selected_column].str.contains(filter_text,case=False, na=False)]
#
#     return df
# try:
#     uploaded_file = st.file_uploader("Choose a file (CSV, JSON, XLSX)", type=['csv', 'json', 'xlsx', 'xls'],
#                                      accept_multiple_files=False
#                                      )
#     with col1:
#         df = extract_data(uploaded_file)
#         st.dataframe(df)
#     with col2:
#         filter_data = st.button("Filter Data")
#         if filter_data:
#             filter(df)
# except Exception as e:
#     print(e)
