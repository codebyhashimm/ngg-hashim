import random
import streamlit as st

# -----------------------------
# SESSION STATE INIT
# -----------------------------
if "secret_number" not in st.session_state:
    st.session_state.secret_number = None
    st.session_state.guesses_left = 0
    st.session_state.history = []
    st.session_state.game_started = False
    st.session_state.input_key = 0

# -----------------------------
# RESET FUNCTION (HOME)
# -----------------------------
def go_home():
    st.session_state.secret_number = None
    st.session_state.guesses_left = 0
    st.session_state.history = []
    st.session_state.game_started = False
    st.session_state.input_key += 1

# -----------------------------
# HEADER
# -----------------------------
st.markdown("""
<h
