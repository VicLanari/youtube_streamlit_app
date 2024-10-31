import streamlit as st

st.set_page_config(page_title='Automate Youtube App')

if "y" == 'y':
    from src.components import sidebar
    sidebar.show_sidebar()




st.title('Automate Youtube Facilitator')
st.write('This app was made to facilitate creators jobs in organizing, downloading transcripts, and more')