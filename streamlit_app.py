import streamlit as st

# Custom CSS for full-width layout
st.markdown("""
    <style>
        /* Remove default padding and margins */
        body {
            margin: 0;
            padding: 0;
        }

        /* Full-width header */
        .header {
            background-color: #006400;  /* Dark green color */
            color: white;
            padding: 20px 0;
            text-align: center;
            font-size: 32px;
            font-weight: bold;
            width: 100%;
            box-sizing: border-box;
        }

        /* Button styling */
        .tab-buttons {
            display: flex;
            justify-content: center;
            margin-top: 20px;
            margin-bottom: 20px;
        }

        .tab-buttons button {
            background-color: #006400;
            color: white;
            padding: 10px 20px;
            border: none;
            margin: 0 10px;
            cursor: pointer;
            font-size: 16px;
        }

        .tab-buttons button:hover {
            background-color: #004d00;
        }

        /* Full-width content */
        .content {
            width: 100%;
            padding: 20px;
            box-sizing: border-box;
        }

        /* Main content area */
        .main-content {
            width: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        /* Align image and other elements properly */
        .main-content img {
            width: 100%;
            max-width: 1000px; /* Limit max width to prevent over-expansion */
            margin-top: 20px;
        }

        /* Make buttons for tabs appear full width and centered */
        .tab-buttons button {
            width: auto;
            margin: 0 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="header">Guess the PGA Player\'s Swing</div>', unsafe_allow_html=True)

# Tab Buttons for navigation
tabs = ["Home", "Instructions", "Leaderboard", "About"]
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
    if st.button('Leaderboard'):
        selected_tab = "Leaderboard"
with col4:
    if st.button('About'):
        selected_tab = "About"

# Main content area (centered)
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Tab Content
if selected_tab == "Home":
    st.subheader("Welcome to the PGA Player Swing Guessing Game!")
    st.write("""
        Look at the swing GIF and try to guess the player performing the swing. You can select the player's name 
        from the suggestions that appear as you type.
    """)
    # # Display the GIF of the player's swing (replace with an actual player's swing GIF)
    # st.video("https://vimeo.com/1029391107")  # Example GIF URL

    # Vimeo video ID
    video_id = "1029391107"  # Replace with your Vimeo video ID
    
    # Embed the Vimeo video with autoplay and loop enabled
    embed_code = f"""
    <iframe src="https://player.vimeo.com/video/{video_id}?autoplay=1&loop=1" width="640" height="360" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
    """
    # Display the embedded video using markdown
    st.markdown(embed_code, unsafe_allow_html=True)


    
    # List of players for guessing
    players = ['Tiger Woods', 'Rory McIlroy', 'Phil Mickelson', 'Dustin Johnson', 'Brooks Koepka', 
               'Jordan Spieth', 'Justin Thomas', 'Jon Rahm', 'Bryson DeChambeau', 'Collin Morikawa']
    
    # Text input box for user to type the player's name
    player_input = st.text_input("Start typing the name of the PGA player:")

    # Only show suggestions if the user has typed something
    if player_input:
        # Filter players based on the input text
        filtered_players = [player for player in players if player_input.lower() in player.lower()]

        # If there are matching players, display them as clickable buttons
        if filtered_players:
            st.write("**Suggestions**:")
            for player in filtered_players:
                if st.button(player):  # Create a button for each filtered player
                    # If a suggestion is clicked, store the player's name as the guess
                    guess = player
                    # Correct player for the swing (you can change this dynamically based on the GIF)
                    correct_player = "Tiger Woods"  # Replace this with the actual player for the GIF

                    # Check if the guess is correct and provide feedback
                    if guess == correct_player:
                        st.success(f"Congratulations! {guess} is correct!")
                    else:
                        st.error(f"Oops! {guess} is not correct. Try again.")
        else:
            st.write("No matching players found.")
    else:
        st.write("Start typing to see suggestions.")

elif selected_tab == "Instructions":
    st.subheader("How to Play:")
    st.write("""
        1. Look at the swing GIF displayed above.
        2. Start typing the name of the PGA player you think is performing the swing.
        3. Suggestions will appear based on your input.
        4. Click on a suggestion to make your guess.
        5. After selecting a player, feedback will be provided (correct or incorrect).
    """)

elif selected_tab == "Leaderboard":
    st.subheader("Leaderboard")
    st.write("""
        Here we will display a leaderboard once we add functionality to track and save scores.
    """)

elif selected_tab == "About":
    st.subheader("About the Game")
    st.write("""
        This game lets you guess which PGA Tour player is performing a golf swing based on GIFs of their swings.
        It's a fun way to test your knowledge of the PGA players!
    """)

st.markdown('</div>', unsafe_allow_html=True)
