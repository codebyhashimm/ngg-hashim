import random
import streamlit as st

st.title("🎯 Number Guessing Game")

# Initialize session state
if "secret_number" not in st.session_state:
    st.session_state.secret_number = None
    st.session_state.guesses_left = 0
    st.session_state.history = []
    st.session_state.game_started = False

# Setup game
min_num = st.number_input("Minimum number", value=1)
max_num = st.number_input("Maximum number", value=100)

if st.button("Start Game"):
    st.session_state.secret_number = random.randint(int(min_num), int(max_num))
    st.session_state.guesses_left = st.number_input("Number of guesses", min_value=1, value=5)
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
