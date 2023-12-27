import streamlit as st
from utils.studio_style import apply_studio_style


if __name__ == '__main__':
    st.set_page_config(
        page_title="Welcome"
    )
    apply_studio_style()
    st.title("Moving Along SMB Website Generator Demo")
    st.markdown("Prototype demonstration of some of the amazing technologies on offer by AI21, created for Moving Along LLC")
    st.markdown("Demo by Ian Maddox, AI21 Solutions Architect")
    st.markdown("December 27, 2023, ian@ai21.com")
