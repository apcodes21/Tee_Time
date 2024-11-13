import streamlit as st

# Custom CSS for the header (dark green background)
st.markdown("""
    <style>
        .header {
            background-color: #006400;  /* Dark green color */
            color: white;
            padding: 10px;
            text-align: center;
            font-size: 32px;
            font-weight: bold;
        }
        .tab-content {
            padding: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="header">Guess the PGA Player\'s Swing</div>', unsafe_allow_html=True)

# Sidebar or Tab navigation using `st.radio`
tabs = ["Home", "Instructions", "Leaderboard", "About"]
selected_tab = st.radio("Select a tab", tabs)

# Tab Content
if selected_tab == "Home":
    st.subheader("Welcome to the PGA Player Swing Guessing Game!")
    st.write("""
        Look at the swing GIF and try to guess the player performing the swing. You can select the player's name 
        from the suggestions that appear as you type.
    """)
    # Display the GIF of the player's swing (replace with an actual player's swing GIF)
    st.image("https://media.giphy.com/media/7zNrjA7lZ4QwI/giphy.gif", use_column_width=True)  # Example GIF URL
    
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
                        st.error(f"Oops! {guess} is not correct. Try again.
