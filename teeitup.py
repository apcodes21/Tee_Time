import streamlit as st
from streamlit_option_menu import option_menu

# Set page config (for better control over the title and layout)
st.set_page_config(page_title="Tee it Up", page_icon=":golf:", layout="wide")

# Define the mapping of dates to players
date_to_player_map = {
    "11/14/2024": "Scottie Scheffler",
    "11/07/2024": "Xander Schauffele",  # Update the player for this date
    "10/31/2024": "Jon Rahm",
    # Add more dates and players as needed
}

# List of past swings (GIFs)
past_swings = [
    {"date": "11/14/2024", "gif_url": "https://github.com/apcodes21/Tee_Time/blob/main/image0.gif?raw=true"},
    {"date": "11/07/2024", "gif_url": "https://github.com/apcodes21/Tee_Time/blob/main/golf-xander-schauffele.gif?raw=true"},
    {"date": "10/31/2024", "gif_url": "https://github.com/apcodes21/Tee_Time/blob/main/image2.gif?raw=true"},
    # Add more records as necessary
]

# Sidebar Menu
with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Instructions', 'Past Swings'], 
                           icons=['house', 'gear'], menu_icon="golf", default_index=0)
    
    if selected == "Home":
        if 'radio_reset' not in st.session_state:
            st.session_state.radio_reset = False
        else:
            st.session_state.radio_reset = True
    if selected == "Home":
        st.title("Welcome to Tee & Tell")
        
    elif selected == "Instructions":
        st.title("Instructions")
        st.write("""
            How to use the app:
            
            1. Watch the GIF video of a PGA Player's swing.
            2. Guess the Player by typing in the text box (Ex. Sam)
                - This will provide a list of Players named Sam on the PGA tour
            4. Next, Select one of the suggested players that you think matches the swing
            5. If you are incorrect, delete the current name and try a new name
            6. If you are correct, wait till next weeks player swing!
        """)
    elif selected == "Past Swings":
        st.markdown("### Previous games if you missed them!")
        
        # Get list of all past swing dates
        date_options = [entry['date'] for entry in past_swings]
        
        # Default selected date to the most recent one
        most_recent_date = max(date_options)  # Find the latest date
        
        # Set the default selected date as the most recent one in the radio button
        selected_date = st.sidebar.radio("Select a Past Swing Date", date_options, index=date_options.index(most_recent_date))

        # Find the selected swing based on the date
        selected_swing = next((entry for entry in past_swings if entry['date'] == selected_date), None)
    
        if selected_swing:
            st.session_state.selected_swing = selected_swing


# Header Section
st.markdown("""
    <style>
        .header {
            font-size: 36px;
            font-weight: bold;
            color: #4CAF50;
            text-align: center;
        }
        .sub-header {
            font-size: 14px;
            color: #333333;
            margin-top: 0px;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Display Header
st.markdown('''
    <div style="display: flex; align-items: center; height: 82px;">
        <img src="https://github.com/apcodes21/Tee_Time/blob/main/TT.png?raw=true" alt="PGA Logo" style="height: 82px; margin-right: 0px;">
        <p class="header" style="font-size: 32px; margin: 0;">Guess the PGA Players swing</p>
    </div>
''', unsafe_allow_html=True)

# Select Past Swing
st.markdown("### Select a Past Swing Date:")

# Get list of past swing dates and set the default date
date_options = [entry['date'] for entry in past_swings]
most_recent_date = max(date_options)
selected_date = st.radio("Pick a Date", date_options, index=date_options.index(most_recent_date))

# Retrieve the corresponding player for the selected date
correct_player = date_to_player_map.get(selected_date, "Unknown Player")

# Display the corresponding GIF for the selected date
selected_swing = next((entry for entry in past_swings if entry['date'] == selected_date), None)
if selected_swing:
    st.image(selected_swing["gif_url"], caption=f"Swing on {selected_date}", use_column_width=True)

# Display the correct player for the selected date
st.markdown(f"**Correct Player for {selected_date}:** {correct_player}")

# Input and Guessing Section
st.subheader("Guess the PGA Player's Swing")

# Create the input box for guessing the player
player_input = st.text_input("Enter your guess:", placeholder="Type the player's name")

# List of all possible players for suggestions
players = [
    "Jon Rahm", "Sahith Theegala", "Rory McIlroy", "Scottie Scheffler", "Patrick Cantlay", "Collin Morikawa",
    "Jordan Spieth", "Xander Schauffele", "Brooks Koepka", "Justin Thomas", "Cameron Smith", "Hideki Matsuyama",
    # Add all players here...
]

# Show player suggestions if there is input
if player_input:
    filtered_players = [player for player in players if player_input.lower() in player.lower()]
    
    if filtered_players:
        for player in filtered_players:
            if st.button(player):
                # Check if the guess is correct
                if player == correct_player:
                    st.success(f"Correct! {player} is the player!")
                else:
                    st.error(f"Wrong guess! {player} is not the player. Try again!")
    else:
        st.write("No matching players found.")
else:
    st.write("Start typing the player's name to get suggestions.")
