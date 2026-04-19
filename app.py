import random
import streamlit as st

# 🔥 HEADER
st.markdown("""
<h1 style='text-align: center;'>🎯 Number Guessing Game</h1>
<h3 style='text-align: center; color: grey;'>
Built by Hashim Hassan 🚀
</h3>
<p style='text-align: center; font-size:16px;'>
Think you’ve got sharp instincts? Put them to the test.<br>
Every guess counts — how close can you get?
</p>
<hr>
""", unsafe_allow_html=True)

# Initialize session state
if "secret_number" not in st.session_state:
    st.session_state.secret_number = None
    st.session_state.guesses_left = 0
    st.session_state.history = []
    st.session_state.game_started = False

# Inputs (defaults = "press Enter" behavior)
min_num = st.number_input("Minimum number (default = 1)", value=1)
max_num = st.number_input("Maximum number (default = 100)", value=100)

# Validate range
if min_num >= max_num:
    st.error("Minimum must be less than maximum")

# Start game
if st.button("Start Game") and min_num < max_num:
    st.session_state.secret_number = random.randint(int(min_num), int(max_num))
    st.session_state.guesses_left = st.number_input(
        "Number of guesses", min_value=1, value=5
    )
    st.session_state.history = []
    st.session_state.game_started = True

# Game logic
if st.session_state.game_started:

    st.write(f"Guesses left: {st.session_state.guesses_left}")

    user_guess = st.number_input("Enter your guess", step=1)

    if st.button("Submit Guess"):

        st.session_state.history.append(user_guess)

        distance = abs(user_guess - st.session_state.secret_number)

        if distance == 0:
            st.success("🎉 You guessed it!")
            st.session_state.game_started = False

        else:
            st.session_state.guesses_left -= 1

            if st.session_state.guesses_left == 0:
                st.error(f"💀 Game over! Number was {st.session_state.secret_number}")
                st.session_state.game_started = False

            # Temperature hints
            if distance <= 5:
                st.write("🔥 Boiling hot")
            elif distance <= 15:
                st.write("🌡️ Hot")
            elif distance <= 30:
                st.write("🙂 Warm")
            elif distance <= 60:
                st.write("❄️ Cold")
            else:
                st.write("🥶 Freezing")

        st.write("Your guesses:", st.session_state.history)

# ⚡ FOOTER
st.markdown("""
<hr>
<p style='text-align: center; color: grey; font-size:14px;'>
👨‍💻 Created by <b>Hashim Hassan</b><br>
Powered by Python & Streamlit<br><br>

🚀 Built with logic, creativity, and a passion for coding.<br>
Simple idea — executed with precision.
</p>
""", unsafe_allow_html=True)
