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
        <style>
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }
        @keyframes shimmer {
            0% { background-position: -200% center; }
            100% { background-position: 200% center; }
        }
        .win-container {
            text-align: center;
            padding: 2rem 1rem;
            animation: fadeInUp 0.8s ease forwards;
        }
        .win-trophy {
            font-size: 80px;
            animation: pulse 1.5s infinite;
            display: block;
            margin-bottom: 1rem;
        }
        .win-title {
            font-size: 48px;
            font-weight: 900;
            background: linear-gradient(90deg, #f7971e, #ffd200, #f7971e);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: shimmer 2s linear infinite;
            margin-bottom: 0.5rem;
        }
        .win-subtitle {
            font-size: 22px;
            color: #888;
            margin-bottom: 1.5rem;
        }
        .win-number {
            font-size: 64px;
            font-weight: 900;
            color: #f7971e;
            margin: 0.5rem 0;
        }
        .win-stats {
            display: flex;
            justify-content: center;
            gap: 2rem;
            margin: 1.5rem 0;
            flex-wrap: wrap;
        }
        .win-stat-box {
            background: linear-gradient(135deg, #1a1a2e, #16213e);
            border: 2px solid #f7971e;
            border-radius: 16px;
            padding: 1rem 2rem;
            min-width: 140px;
        }
        .win-stat-label {
            font-size: 13px;
            color: #aaa;
            margin-bottom: 4px;
        }
        .win-stat-value {
            font-size: 28px;
            font-weight: 800;
            color: #ffd200;
        }
        .win-message {
            font-size: 18px;
            color: #ccc;
            margin: 1rem 0 2rem;
            font-style: italic;
        }
        .stars-row {
            font-size: 32px;
            letter-spacing: 8px;
            margin-bottom: 1rem;
        }
        </style>

        <div class='win-container'>
            <span class='win-trophy'>🏆</span>
            <div class='win-title'>YOU WON!</div>
            <div class='stars-row'>⭐⭐⭐⭐⭐</div>
            <div class='win-subtitle'>Incredible! You cracked the code!</div>
            <div class='win-number'>🎯</div>
        </div>
        """, unsafe_allow_html=True)

        guesses_used = len(st.session_state.history)
        if guesses_used == 1:
            performance = "🤯 LEGENDARY — First try?!"
        elif guesses_used <= 3:
            performance = "🔥 OUTSTANDING — Only a few guesses!"
        elif guesses_used <= 6:
            performance = "😎 GREAT — Well played!"
        else:
            performance = "👏 NICE — You got there!"

        st.markdown(f"""
        <div style='text-align:center;'>
            <div class='win-stats'>
                <div class='win-stat-box'>
                    <div class='win-stat-label'>Secret Number</div>
                    <div class='win-stat-value'>{st.session_state.secret_number}</div>
                </div>
                <div class='win-stat-box'>
                    <div class='win-stat-label'>Guesses Used</div>
                    <div class='win-stat-value'>{guesses_used}</div>
                </div>
                <div class='win-stat-box'>
                    <div class='win-stat-label'>Guesses Left</div>
                    <div class='win-stat-value'>{st.session_state.guesses_left}</div>
                </div>
            </div>
            <div class='win-message'>{performance}</div>
        </div>
        """, unsafe_allow_html=True)

        st.snow()

        if st.session_state.history:
            st.markdown("### 📊 Your Guess Journey")
            for i, g in enumerate(st.session_state.history, 1):
                if g == st.session_state.secret_number:
                    st.markdown(f"**{i}.** `{g}` ✅ **WINNER!**")
                else:
                    st.markdown(f"**{i}.** `{g}`")

        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🏠 Play Again", use_container_width=True):
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

        st.components.v1.html(
            """
            <script>
                const inputs = window.parent.document.querySelectorAll('input[type=number]');
                if (inputs.length > 0) {
                    inputs[0].focus();
                }
            </script>
            """,
            height=0
        )

        if st.button("🎯 Submit Guess"):
            if guess is None:
                st.warning("Please enter a number first!")
                st.stop()

            st.session_state.history.append(guess)
            distance = abs(guess - st.session_state.secret_number)

            if distance == 0:
                st.session_state.won = True
                st.balloons()
                st.rerun()

            st.session_state.guesses_left -= 1

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
