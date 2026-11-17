import streamlit as st
if "a" not in st.session_state: 
    st.session_state.a = 0 
if st.button("Click me!"): 
    st.session_state.a += 1 
st.write(st.session_state.a) 
