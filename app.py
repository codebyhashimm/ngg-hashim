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
        st.session_state.history = []
        st.session_state.game_started = True
        st.session_state.input_key += 1
        st.balloons()

if st.session_state.game_started:
    st.subheader("🎮 Game Running")

    if st.button("🏠 Finish Game"):
        st.warning("Returning to home...")
        go_home()
        st.rerun()

    st.write(f"💖 Guesses left: **{st.session_state.guesses_left}**")

    guess = st.number_input(
        "Enter your guess",
        min_value=0,
        max_value=500,
        value=0,
        step=1,
        key=f"guess_input_{st.session_state.input_key}"
    )

    if st.button("🎯 Submit Guess"):
        st.session_state.history.append(guess)
        distance = abs(guess - st.session_state.secret_number)

        if distance == 0:
            st.success("🎉 PERFECT GUESS! YOU WON!")
            st.balloons()
            go_home()
            st.rerun()

        st.session_state.guesses_left -= 1

        if distance <= 5:
            st.error("🔥 BOILING HOT!")
        elif distance <= 15:
            st.warning("🌡️ Hot")
        elif distance <= 30:
            st.info("🙂 Warm")
        elif distance <= 60:
            st.write("❄️ Cold")
        else:
            st.write("🥶 Freezing")

        if st.session_state.guesses_left <= 0:
            st.error(f"💀 Game Over! The number was {st.session_state.secret_number}")
            go_home()
            st.rerun()

        st.session_state.input_key += 1
        st.rerun()

    if st.session_state.history:
        st.markdown("### 📊 Guess History")
        for i, g in enumerate(st.session_state.history, 1):
            st.markdown(f"**{i}.** `{g}`")

st.markdown("""
<hr>
<p style='text-align:center; color:grey;'>
👨‍💻 Created by <b>Hashim Hassan</b><br>
Built with logic • creativity • persistence 🚀
</p>
""", unsafe_allow_html=True)
