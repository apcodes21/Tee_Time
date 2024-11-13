import streamlit as st

# List of players to be included in the search suggestions
players = ['Tiger Woods', 'Rory McIlroy', 'Phil Mickelson', 'Dustin Johnson', 'Brooks Koepka',
           'Jordan Spieth', 'Justin Thomas', 'Jon Rahm', 'Bryson DeChambeau', 'Collin Morikawa']

# Title of the app
st.markdown("""
    <h1 style="text-align: center;">Tee & Tell</h1>
""", unsafe_allow_html=True)

# Display the GIF of the player's swing (replace with an actual player's swing GIF)
st.image("https://media1.giphy.com/media/KQGFjLggOsvUsSD5ha/200.webp?cid=790b7611lowkco26j5fqc4azn3k967ka1clq3fcsfvm9i4h7&ep=v1_gifs_search&rid=200.webp&ct=g", use_container_width=True)  # Example GIF URL

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
                correct_player = "Dustin Johnson"  # Replace this with the actual player for the GIF

                # Check if the guess is correct and provide feedback
                if guess == correct_player:
                    st.success(f"Congratulations! {guess} is correct!")
                else:
                    st.error(f"Oops! {guess} is not correct. Try again.")
    else:
        st.write("No matching players found.")
else:
    st.write("Start typing to see suggestions.")

# Optionally, provide instructions or additional details
st.markdown("""
### How to Play:
- Look at the swing GIF above.
- Start typing the name of the PGA player you think this swing belongs to.
- Suggestions will appear as you type.
- Click on the name to submit your guess.
""")
