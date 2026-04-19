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
    st.session_state.finished = False

# -----------------------------
# HOME RESET FUNCTION
# -----------------------------
def go_home():
    st.session_state.secret_number = None
    st.session_state.guesses_left = 0
    st.session_state.history = []
    st.session_state.game_started = False
    st.session_state.finished = False

# -----------------------------
# HEADER (WOW FACTOR)
# -----------------------------
st.markdown("""
<h1 style='text-align:center;'>🎯 Number Guessing Game</h1>
<h3 style='text-align:center; color:grey;'>Built by Hashim Hassan 🚀</h3>
<p style='text-align:center;'>
Can you outsmart the system? Or will the number defeat you?
</p>
<hr>
""", unsafe_allow_html=True)

# -----------------------------
# HOME SCREEN
# -----------------------------
if not st.session_state.game_started:

    st.info("👋 Welcome! Set your game and start playing.")

    min_num = st.number_input("Minimum number", value=1)
    max_num = st.number_input("Maximum number", value=100)
    guesses = st.number_input("Number of guesses", min_value=1, value=5)

    if st.button("🚀 Start Game"):

        if min_num >= max_num:
            st.error("Minimum must be less than maximum")
        else:
            st.session_state.secret_number = random.randint(int(min_num), int(max_num))
            st.session_state.guesses_left = guesses
            st.session_state.history = []
            st.session_state.game_started = True
            st.session_state.finished = False
            st.balloons()  # 🎉 WOW EFFECT

# -----------------------------
# GAME SCREEN
# -----------------------------
if st.session_state.game_started:

    st.subheader("🎮 Game On!")

    # Finish button (instant exit)
    if st.button("🏠 Finish Game"):
        st.warning("Game ended. Returning home...")
        go_home()
        st.rerun()

    st.write(f"💖 Guesses left: **{st.session_state.guesses_left}**")

    user_guess = st.number_input("Enter your guess", step=1)

    if st.button("🎯 Submit Guess"):

        st.session_state.history.append(user_guess)
        distance = abs(user_guess - st.session_state.secret_number)

        # Win condition
        if distance == 0:
            st.success("🎉 YOU WON! Perfect guess!")
            st.balloons()
            go_home()
            st.rerun()

        # Reduce lives
        st.session_state.guesses_left -= 1

        # Hint system (WOW upgrade)
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

        # Lose condition
        if st.session_state.guesses_left <= 0:
            st.error(f"💀 Game Over! Number was {st.session_state.secret_number}")
            go_home()

    # -----------------------------
    # GUESS HISTORY (WOW LIST UI)
    # -----------------------------
    if st.session_state.history:
        st.markdown("### 📊 Your Guesses")
        for i, guess in enumerate(st.session_state.history, start=1):
            st.markdown(f"**{i}.** You guessed: `{guess}`")

# -----------------------------
# FOOTER (WOW FACTOR)
# -----------------------------
st.markdown("""
<hr>
<p style='text-align:center; color:grey;'>
👨‍💻 Created by <b>Hashim Hassan</b><br>
Built with logic • creativity • persistence 🚀<br><br>
Not just a game — a demonstration of real coding growth.
</p>
""", unsafe_allow_html=True)
