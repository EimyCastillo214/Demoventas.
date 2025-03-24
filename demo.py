# prompt: Leer archivo Salidafinal.xlsx

import pandas as pd

# Replace 'Salidafinal.xlsx' with the actual file path if it's not in the current directory
try:
  df = pd.read_excel('Salidafinal.xlsx')
  print(df)
except FileNotFoundError:
  print("Error: 'Salidafinal.xlsx' not found. Please check the file path.")
except Exception as e:
  print(f"An error occurred: {e}")
  # prompt: imprimir dataframe usando Streamlit

import streamlit as st
import pandas as pd

# Replace 'Salidafinal.xlsx' with the actual file path if it's not in the current directory
try:
  df = pd.read_excel('Salidafinal.xlsx')
  st.dataframe(df) # Use st.dataframe to display the DataFrame in Streamlit
except FileNotFoundError:
  st.error("Error: 'Salidafinal.xlsx' not found. Please check the file path.")
except Exception as e:
  st.error(f"An error occurred: {e}")
