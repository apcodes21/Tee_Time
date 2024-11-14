import streamlit as st
from streamlit_option_menu import option_menu

# Set page config (for better control over the title and layout)
st.set_page_config(page_title="Tee it Up", page_icon=":golf:", layout="wide", initial_sidebar_state='collapsed')

# List of past swings with dates and associated GIF URLs
past_swings = [
    {"date": "11/14/2024", "gif_url": "https://github.com/apcodes21/Tee_Time/blob/main/image0.gif?raw=true"},
    {"date": "11/07/2024", "gif_url": "https://github.com/apcodes21/Tee_Time/blob/main/image1.gif?raw=true"},
    {"date": "10/31/2024", "gif_url": "https://github.com/apcodes21/Tee_Time/blob/main/image2.gif?raw=true"},
    # Add more records as necessary
]

# 1. Sidebar menu
with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Instructions', 'Past Swings'], 
                           icons=['house', 'gear', 'clock'], menu_icon="golf", default_index=0)
    
    # Display content based on the selection
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
            6. If you are correct, wait till next week's player swing!
        """)
    
    elif selected == "Past Swings":
        st.title("Past Swings")

        # Display past swings as clickable items
        st.markdown("### Past Player Swings")
        st.write("""
            Here are some of the past player's swings with the corresponding dates. 
            Click on any date to view the swing video in the home page:
        """)

        # Create a scrollable list of past swings
        for entry in past_swings:
            if st.button(entry["date"], key=entry["date"]):
                st.session_state.selected_swing = entry  # Save the selected swing info to session state

# Sidebar: Date selection for GIF
if selected == "Home":
    # Add a dropdown for selecting a date (this could be a selectbox or radio button)
    date_options = [entry['date'] for entry in past_swings]
    selected_date = st.sidebar.radio("Select a Past Swing Date", date_options, index=0)

    # Find the selected swing based on the date
    selected_swing = next((entry for entry in past_swings if entry['date'] == selected_date), None)

    if selected_swing:
        st.session_state.selected_swing = selected_swing  # Update session state with the selected swing

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
        .toc {
            font-size: 18px;
            font-weight: bold;
            color: #4CAF50;
            padding: 0px;
            background-color: #f4f4f4;
            border-radius: 8px;
        }
        .toc-item {
            padding-left: 0px;
            margin-bottom: 0px;
        }
        .toc-item a {
            text-decoration: none;
            color: #0073e6;
        }
        .toc-item a:hover {
            color: #0056b3;
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

# Main page: Displaying Player Swing and Guessing Section
if selected == "Home":
    # If a user has clicked a past swing date, show the corresponding video
    if 'selected_swing' in st.session_state:
        selected_swing = st.session_state.selected_swing
        st.markdown(f"### Swing from {selected_swing['date']}")
        st.markdown(f'<div style="display: flex; justify-content: center; align-items: center; height: 45vh;">'
                    f'<img src="{selected_swing["gif_url"]}" alt="GIF" style="height: 495px;"></div>', unsafe_allow_html=True)
    else:
        # Default display message when no swing has been selected yet
        st.markdown('''<p>Click on a date from "Past Swings" to view the video here.</p>''')

    st.subheader("#1: 11/14/2024")
    
    # List of players for guessing
    players = [
        "Jon Rahm", "Sahith Theegala", "Rory McIlroy", "Scottie Scheffler", "Patrick Cantlay", 
        "Collin Morikawa", "Jordan Spieth", "Xander Schauffele", "Brooks Koepka", "Justin Thomas", 
        "Cameron Smith", "Hideki Matsuyama", "Sam Burns", "Will Zalatoris", "Viktor Hovland", "Tony Finau",
        "Matt Fitzpatrick", "Tom Kim", "Tommy Fleetwood", "Jason Day", "Dustin Johnson"
    ]

    col1, col2, col3 = st.columns([1, 1, 1])  # Adjust the column ratios to control the width

    with col2:
        player_input = st.text_input("", placeholder="Guess the Tour Pro Name")
    
        # Only show suggestions if the user has typed something
        if player_input:
            # Filter players based on the input text
            filtered_players = [player for player in players if player_input.lower() in player.lower()]
        
            # If there are matching players, display them as clickable buttons
            if filtered_players:
                for player in filtered_players:
                    if st.button(player):  # Create a button for each filtered player
                        # If a suggestion is clicked, store the player's name as the guess
                        guess = player
                        # Correct player for the swing (you can change this dynamically based on the GIF)
                        correct_player = "Scottie Scheffler"  # Replace this with the actual player for the GIF
        
                        # Check if the guess is correct and provide feedback
                        if guess == correct_player:
                            st.success(f"Aced it! {guess} is correct!")
                        else:
                            st.error(f"Good guess! But {guess} is not correct. Please try again.")
            else:
                st.write("No matching players found.")
