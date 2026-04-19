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

# -----------------------------
# RESET FUNCTION (HOME PAGE)
# -----------------------------
def go_home():
    st.session_state.secret_number = None
    st.session_state.guesses_left = 0
    st.session_state.history = []
    st.session_state.game_started = False

# -----------------------------
# HEADER (WOW FACTOR)
# -----------------------------
st.markdown("""
<h1 style='text-align:center;'>🎯 Number Guessing Game</h1>
<h3 style='text-align:center; color:grey;'>Built by Hashim Hassan 🚀</h3>
<p style='text-align:center;'>
Can you beat the system, or will the number win again?
</p>
<hr>
""", unsafe_allow_html=True)

# -----------------------------
# HOME SCREEN
# -----------------------------
if not st.session_state.game_started:

    st.info("👋 Configure your game settings below and start playing!")

    # 🎚️ SLIDERS (UPGRADE)
    min_num = st.slider("Minimum number", 1, 100, 1)
    max_num = st.slider("Maximum number", min_num + 1, 500, 100)
    guesses = st.slider("Number of guesses", 1, 20, 5)

    if st.button("🚀 Start Game"):
        st.session_state.secret_number = random.randint(min_num, max_num)
        st.session_state.guesses_left = guesses
        st.session_state.history = []
        st.session_state.game_started = True
        st.balloons()  # 🎉 wow effect

# -----------------------------
# GAME SCREEN
# -----------------------------
if st.session_state.game_started:

    st.subheader("🎮 Game Running")

    # Finish button → instant home
    if st.button("🏠 Finish Game"):
        st.warning("Game ended. Returning home...")
        go_home()
        st.rerun()

    st.write(f"💖 Guesses left: **{st.session_state.guesses_left}**")

    user_guess = st.number_input("Enter your guess", step=1)

    if st.button("🎯 Submit Guess"):

        st.session_state.history.append(user_guess)
        distance = abs(user_guess - st.session_state.secret_number)

        # WIN
        if distance == 0:
            st.success("🎉 PERFECT GUESS! YOU WON!")
            st.balloons()
            go_home()
            st.rerun()

        # reduce guesses
        st.session_state.guesses_left -= 1

        # hint system (wow feedback)
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
            st.error(f"💀 Game Over! The number was {st.session_state.secret_number}")
            go_home()

    # -----------------------------
    # GUESS HISTORY (CLEAN UI)
    # -----------------------------
    if st.session_state.history:
        st.markdown("### 📊 Guess History")
        for i, guess in enumerate(st.session_state.history, start=1):
            st.markdown(f"**{i}.** `{guess}`")

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("""
<hr>
<p style='text-align:center; color:grey;'>
👨‍💻 Created by <b>Hashim Hassan</b><br>
Built with logic • creativity • persistence 🚀<br><br>
A simple idea turned into an interactive experience.
</p>
""", unsafe_allow_html=True)
