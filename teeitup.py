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

past_swings = [
    {"date": "11/14/2024", "gif_url": "https://github.com/apcodes21/Tee_Time/blob/main/image0.gif?raw=true"},
    {"date": "11/07/2024", "gif_url": "https://github.com/apcodes21/Tee_Time/blob/main/golf-xander-schauffele.gif?raw=true"},
    {"date": "10/31/2024", "gif_url": "https://github.com/apcodes21/Tee_Time/blob/main/image2.gif?raw=true"},
    # Add more records as necessary
]

# Sidebar menu
with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Instructions', 'Past Swings'], 
               icons=['house', 'gear'], menu_icon="golf", default_index=0)
    # Display content based on the selection
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

        # Retrieve the corresponding player for the selected date
        correct_player = date_to_player_map.get(selected_date, "Unknown Player")
        
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

# Sidebar date picker (moved here)
date_options = [entry['date'] for entry in past_swings]
most_recent_date = max(date_options)
selected_date = st.sidebar.radio("Pick a Date", date_options, index=date_options.index(most_recent_date))

# Retrieve the corresponding player for the selected date
correct_player = date_to_player_map.get(selected_date, "Unknown Player")

# Find the selected swing based on the date
selected_swing = next((entry for entry in past_swings if entry['date'] == selected_date), None)

if selected_swing:
    st.session_state.selected_swing = selected_swing

# Display the GIF for the selected date
if 'selected_swing' in st.session_state:
    selected_swing = st.session_state.selected_swing
    st.markdown(f'<div style="display: flex; justify-content: center; align-items: center; height: 45vh;">'
                f'<img src="{selected_swing["gif_url"]}" alt="GIF" style="height: 495px;"></div>', unsafe_allow_html=True)
else:
    # Default GIF if no swing is selected
    default_url = "https://github.com/apcodes21/Tee_Time/blob/main/image0.gif?raw=true"  # Change this to your desired default URL
    st.markdown(f'<div style="display: flex; justify-content: center; align-items: center; height: 45vh;">'
                f'<img src="{default_url}" alt="Default GIF" style="height: 495px;"></div>', unsafe_allow_html=True)

# Create a container for the input box to control width
col1, col2, col3 = st.columns([1, 1, 1])  # Adjust the column ratios to control the width

with col2:
    player_input = st.text_input("", placeholder="Guess the Tour Pro Name")
    
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
