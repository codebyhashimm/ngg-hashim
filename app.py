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
    st.session_state.guess_input = ""   # 👈 FIX: controlled input

# -----------------------------
# RESET FUNCTION (HOME)
# -----------------------------
def go_home():
    st.session_state.secret_number = None
    st.session_state.guesses_left = 0
    st.session_state.history = []
    st.session_state.game_started = False
    st.session_state.guess_input = ""

# -----------------------------
# HEADER
# -----------------------------
st.markdown("""
<h1 style='text-align:center;'>🎯 Number Guessing Game</h1>
<h3 style='text-align:center; color:grey;'>Built by Hashim Hassan 🚀</h3>
<p style='text-align:center;'>
Try your luck — beat the hidden number!
</p>
<hr>
""", unsafe_allow_html=True)

# -----------------------------
# HOME SCREEN
# -----------------------------
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
        st.session_state.guess_input = ""
        st.balloons()

# -----------------------------
# GAME SCREEN
# -----------------------------
if st.session_state.game_started:

    st.subheader("🎮 Game Running")

    if st.button("🏠 Finish Game"):
        st.warning("Returning to home...")
        go_home()
        st.rerun()

    st.write(f"💖 Guesses left: **{st.session_state.guesses_left}**")

    # 👇 FIXED INPUT (no more sticky 0)
    guess = st.number_input(
        "Enter your guess",
        step=1,
        key="guess_input"
    )

    if st.button("🎯 Submit Guess"):

        st.session_state.history.append(guess)
        distance = abs(guess - st.session_state.secret_number)

        # WIN
        if distance == 0:
            st.success("🎉 PERFECT GUESS! YOU WON!")
            st.balloons()
            go_home()
            st.rerun()

        # reduce guesses
        st.session_state.guesses_left -= 1

        # hints
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

        # LOSE
        if st.session_state.guesses_left <= 0:
            st.error(f"💀 Game Over! Number was {st.session_state.secret_number}")
            go_home()

        # 👇 RESET INPUT AFTER EVERY GUESS (KEY FIX)
        st.session_state.guess_input = 0

    # -----------------------------
    # HISTORY
    # -----------------------------
    if st.session_state.history:
        st.markdown("### 📊 Guess History")
        for i, g in enumerate(st.session_state.history, 1):
            st.markdown(f"**{i}.** `{g}`")

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("""
<hr>
<p style='text-align:center; color:grey;'>
👨‍💻 Created by <b>Hashim Hassan</b><br>
Built with logic • creativity • persistence 🚀
</p>
""", unsafe_allow_html=True)
