import random
import streamlit as st

if "secret_number" not in st.session_state:
    st.session_state.secret_number = None
    st.session_state.guesses_left = 0
    st.session_state.history = []
    st.session_state.game_started = False
    st.session_state.input_key = 0
    st.session_state.hint = None
    st.session_state.hint_type = None
    st.session_state.won = False

def go_home():
    st.session_state.secret_number = None
    st.session_state.guesses_left = 0
    st.session_state.history = []
    st.session_state.game_started = False
    st.session_state.input_key += 1
    st.session_state.hint = None
    st.session_state.hint_type = None
    st.session_state.won = False

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
        st.session_state.hint = None
        st.session_state.hint_type = None
        st.session_state.won = False
        st.balloons()

if st.session_state.game_started:

    # WIN SCREEN
    if st.session_state.won:
        st.markdown("""
        <div style='text-align:center; padding: 2rem 0;'>
            <h2>🎉 Congratulations!</h2>
            <p style='font-size:18px;'>You guessed the number correctly!</p>
            <p style='font-size:28px; font-weight:bold;'>⭐ You're a champion! ⭐</p>
        </div>
        """, unsafe_allow_html=True)

        st.success(f"The secret number was **{st.session_state.secret_number}** and you got it in **{len(st.session_state.history)}** guess(es)!")

        if st.session_state.history:
            st.markdown("### 📊 Your Guesses")
            for i, g in enumerate(st.session_state.history, 1):
                st.markdown(f"**{i}.** `{g}`")

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🏠 Finish & Go Home"):
            go_home()
            st.rerun()

    # GAME SCREEN
    else:
        st.subheader("🎮 Game Running")

        if st.button("🏠 Finish Game"):
            st.warning("Returning to home...")
            go_home()
            st.rerun()

        st.write(f"💖 Guesses left: **{st.session_state.guesses_left}**")

        # Show hint from previous guess
        if st.session_state.hint:
            if st.session_state.hint_type == "error":
                st.error(st.session_state.hint)
            elif st.session_state.hint_type == "warning":
                st.warning(st.session_state.hint)
            elif st.session_state.hint_type == "info":
                st.info(st.session_state.hint)
            else:
                st.write(st.session_state.hint)

        guess = st.number_input(
            "Enter your guess",
            min_value=0,
            max_value=500,
            value=None,
            placeholder="Type a number...",
            step=1,
            key=f"guess_input_{st.session_state.input_key}"
        )

        if st.button("🎯 Submit Guess"):
            if guess is None:
                st.warning("Please enter a number first!")
                st.stop()

            st.session_state.history.append(guess)
            distance = abs(guess - st.session_state.secret_number)

            # WIN
            if distance == 0:
                st.session_state.won = True
                st.balloons()
                st.rerun()

            st.session_state.guesses_left -= 1

            # Save hint to session state
            if distance <= 5:
                st.session_state.hint = "🔥 BOILING HOT!"
                st.session_state.hint_type = "error"
            elif distance <= 15:
                st.session_state.hint = "🌡️ Hot"
                st.session_state.hint_type = "warning"
            elif distance <= 30:
                st.session_state.hint = "🙂 Warm"
                st.session_state.hint_type = "info"
            elif distance <= 60:
                st.session_state.hint = "❄️ Cold"
                st.session_state.hint_type = "write"
            else:
                st.session_state.hint = "🥶 Freezing"
                st.session_state.hint_type = "write"

            # LOSE
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
