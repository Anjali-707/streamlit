# Databricks notebook source


import streamlit as st

st.title("Hello User App")

# Input from user
user_name = st.text_input("Enter your name:")

# Display greeting
if user_name:
    st.success(f"Hello, {user_name}! Welcome to Databricks Streamlit App.")


# COMMAND ----------

