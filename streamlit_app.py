import streamlit as st
import datetime

# Custom CSS for full-width layout
st.markdown("""
    <style>
        body {
            margin: 0;
            padding: 0;
        }

        .header {
            background-color: #006400;
            color: white;
            padding: 20px 0;
            text-align: center;
            font-size: 32px;
            font-weight: bold;
            width: 100%;
            box-sizing: border-box;
        }

        .tab-buttons {
            display: flex;
            justify-content: center;
            margin-top: 20px;
            margin-bottom: 20px;
        }

        .tab-buttons button {
            background-color: #333;
            color: white;
            padding: 10px 20px;
            border: none;
            margin: 0 10px;
            cursor: pointer;
            font-size: 16px;
        }

        .tab-buttons button:hover {
            background-color: #333;
        }

        .content {
            width: 100%;
            padding: 20px;
            box-sizing: border-box;
        }

        .main-content {
            width: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .main-content img {
            width: 100%;
            max-width: 1000px;
            margin-top: 20px;
        }

        .tab-buttons button {
            width: auto;
            margin: 0 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="header">Tee & Tell - Guess the PGA Player\'s Swing</div>', unsafe_allow_html=True)

# Tab Buttons for navigation
tabs = ["Home", "Instructions", "Past Player List", "About"]
selected_tab = "Home"

# Creating buttons for each tab
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button('Home'):
        selected_tab = "Home"
with col2:
    if st.button('Instructions'):
        selected_tab = "Instructions"
with col3:
    if st.button('Past Player List'):
        selected_tab = "Past Player List"
with col4:
    if st.button('About'):
        selected_tab = "About"

# Main content area (centered)
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Initialize session state to store past guesses
if 'player_history' not in st.session_state:
    st.session_state.player_history = []

# Tab Content
if selected_tab == "Home":
    st.subheader(f"Player of the Day: {datetime.date.today().strftime('%m/%d/%Y')}")
    st.subheader("Welcome to the PGA Player Swing Guessing Game!")
    st.write("""
        Look at the swing GIF and try to guess the player performing the swing. You can select the player's name 
        from the suggestions that appear as you type.
    """)

    # Vimeo video ID for the day's player
    player_dict = {
        "name": "Scottie Scheffler",
        "video_id": "1029391107",
        "full_path": "https://player.vimeo.com/video/1029391107"
    }

    video_id = player_dict["video_id"]
    
    # Embed the Vimeo video
    embed_code = f"""
    <iframe src="https://player.vimeo.com/video/{video_id}?autoplay=1&loop=1" width="640" height="360" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
    """
    st.markdown(embed_code, unsafe_allow_html=True)

    # Add today's player to the session history (if it's not already added)
    today_date = datetime.date.today().strftime('%Y-%m-%d')
    if not any(entry['date'] == today_date for entry in st.session_state.player_history):
        st.session_state.player_history.append({
            "date": today_date,
            "player": player_dict["name"],
            "video": player_dict["full_path"]
        })

elif selected_tab == "Instructions":
    st.subheader("How to Play:")
    st.write("""
        1. Look at the swing GIF displayed above.
        2. Start typing the name of the PGA player you think is performing the swing.
        3. Suggestions will appear based on your input.
        4. Click on a suggestion to make your guess.
        5. After selecting a player, feedback will be provided (correct or incorrect).
    """)

elif selected_tab == "Past Player List":
    st.subheader("Past Player List")
    st.write("""
        Here we will display a list of previous player guesses.
    """)

    # Create the table for past player guesses
    if st.session_state.player_history:
        player_data = [(entry["date"], entry["player"], entry["video"]) for entry in st.session_state.player_history]
        st.table(player_data)
    else:
        st.write("No player data available.")

elif selected_tab == "About":
    st.subheader("About the Game")
    st.write("""
        This game lets you guess which PGA Tour player is performing a golf swing based on GIFs of their swings.
        It's a fun way to test your knowledge of the PGA players!
    """)

st.markdown('</div>', unsafe_allow_html=True)
