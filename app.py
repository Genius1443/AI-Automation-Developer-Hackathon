import streamlit as st
import automation as auto

st.set_page_config(page_title="Prospect Research Agent", layout="wide")

st.title("🚀 Prospect Research Agent")

# Enrich Section
st.header("🔍 Enrich Company")

url = st.text_input("Enter Company URL")

if st.button("Enrich"):
    if url:
        with st.spinner("Processing..."):
            try:
                data = auto.main(url)   # ✅ direct call
                st.success("✅ Done")
                st.json(data)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a URL")
