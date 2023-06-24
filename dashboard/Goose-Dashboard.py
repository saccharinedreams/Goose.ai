import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Goose-Dashboard")

st.sidebar.success("Select data source above.")

st.markdown(
    """
    
    **👈 Select a data source from the sidebar**.
    ### Gnosis

    ### Airstack and XMTP
    
    ### UMA

    ### ApeCoin

    ### sismo

"""
)