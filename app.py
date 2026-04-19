import random
import streamlit as st

if "secret_number" not in st.session_state:
    st.session_state.secret_number = None
    st.session_state.guesses_left = 0
    st.session_state.history = []
    st.session_state.game_started = False
    st.session_state.input_key = 0

def go_home():
    st.session_state.secret_number = None
    st.session_state.guesses_left = 0
    st.session_state.history = []
    st.session_state.game_started = False
    st.session_state.input_key += 1

st.markdown("""
<h1 style='text-align:center;'>🎯 Number Guessing Game</h1>
<h3 style='text-align:center; color:grey;'>Built by Hashim Hassan 🚀</h3>
<p style='text-align:center;'>Try your luck — beat the hidden number!</p>
<hr>
""", unsafe_allow_html=True)

if not st.session_state.game_started:
    st.info("👋 Set your game settings and start!")
    min_num = st.slider("Minimum number", 1, 100, 1)
    max_num = st.slider("Maximum number", min_num + 1, 500, 100)
    guesses = st.slider("Number of guesses", 1, 20, 5)

    if st.button("🚀 Start Game"):
        st.session_state.secret_number = random.randint(min_num, max_num)
        st.session_state.guesses_left = guesses
        st.session_state.history =
