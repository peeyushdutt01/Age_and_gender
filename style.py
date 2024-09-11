import streamlit as st

def apply_custom_style():
    st.markdown(
        """
        <style>
        .main {
            background-color: #151533;
            color: #ffffff;
            font-family: monospace;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
