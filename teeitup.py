import streamlit as st
from streamlit_option_menu import option_menu

# Set page config
st.set_page_config(page_title="Tee it Up", page_icon=":golf:", layout="wide")

date_to_player_map = {
    "11/14/2024": "Scottie Scheffler",
    "11/07/2024": "Xander Schauffele",
    "10/31/2024": "Jon Rahm",
}

past_swings = [
    {"date": "11/14/2024", "gif_url": "https://github.com/apcodes21/Tee_Time/blob/main/image0.gif?raw=true"},
    {"date": "11/07/2024", "gif_url": "https://github.com/apcodes21/Tee_Time/blob/main/golf-xander-schauffele.gif?raw=true"},
    {"date": "10/31/2024", "gif_url": "https://github.com/apcodes21/Tee_Time/blob/main/image2.gif?raw=true"},
]

# Sidebar Menu
with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Instructions', 'Past Swings'], 
               icons=['house', 'gear'], menu_icon="golf", default_index=0)

    if selected == "Home":
        st.title("Welcome to Tee & Tell")
    elif selected == "Instructions":
        st.title("Instructions")
        st.write("""
            How to use the app:
            
            1. Watch the GIF video of a PGA Player's swing.
            2. Guess the Player by typing in the text box (Ex. Sam).
            3. Select one of the suggested players that you think matches the swing.
            4. If you are incorrect, delete the current name and try a new name.
            5. If you are correct, wait till next week's player swing!
        """)
    elif selected == "Past Swings":
        st.markdown("### Previous Games If You Missed Them!")
        # Get list of all past swing dates
        date_options = [entry['date'] for entry in past_swings]
        
        # Default selected date to the most recent one
        most_recent_date = max(date_options)  # Find the latest date
        selected_date = st.sidebar.radio("Select a Past Swing Date", date_options, index=date_options.index(most_recent_date))
        
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

# Show the swing GIF if selected
if selected == "Home":
    if 'selected_swing' in st.session_state:
        selected_swing = st.session_state.selected_swing
        st.markdown(f'<div style="display: flex; justify-content: center; align-items: center; height: 45vh;">'
                    f'<img src="{selected_swing["gif_url"]}" alt="GIF" style="height: 495px;"></div>', unsafe_allow_html=True)
    else:
        default_url = "https://github.com/apcodes21/Tee_Time/blob/main/image0.gif?raw=true"
        st.markdown(f'<div style="display: flex; justify-content: center; align-items: center; height: 45vh;">'
                    f'<img src="{default_url}" alt="Default GIF" style="height: 495px;"></div>', unsafe_allow_html=True)

# Player guessing functionality
if selected == "Home":
    players = [
        "Jon Rahm", "Sahith Theegala", "Rory McIlroy", "Scottie Scheffler", "Patrick Cantlay", "Collin Morikawa",
        "Jordan Spieth", "Xander Schauffele", "Brooks Koepka", "Justin Thomas", "Cameron Smith",
        "Hideki Matsuyama", "Sam Burns", "Will Zalatoris", "Viktor Hovland", "Tony Finau",
        "Matt Fitzpatrick", "Tom Kim", "Tommy Fleetwood", "Jason Day", "Dustin Johnson",
        "Bubba Watson", "Sungjae Im", "Si Woo Kim", "Brian Harman", "Keegan Bradley",
        "Adam Scott", "Louis Oosthuizen", "Zach Johnson", "Gary Woodland", "Billy Horschel",
        "Cameron Young", "Maverick McNealy", "Max Homa", "Scott Stallings", "Sepp Straka",
        "Mark Hubbard", "K.H. Lee", "Denny McCarthy", "J.T. Poston", "Chris Kirk",
        "Lucas Glover", "Sungjae Im", "Satoshi Kodaira", "Sam Ryder", "Nick Taylor",
        "Stewart Cink", "Ryan Palmer", "Matt Kuchar", "Kevin Kisner", "Bryson DeChambeau",
        "Phil Mickelson", "Tiger Woods", "Lee Hodges", "Jordan Spieth", "Joaquín Niemann",
        "Si Woo Kim", "Bryan Gay", "Charles Howell III", "Robert Streb", "Alex Noren"
    ]
    # Layout for guessing player
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        player_input = st.text_input("", placeholder="Guess the Tour Pro Name")

        # Only show suggestions if the user has typed something
        if player_input:
            # Filter players based on the input text
            filtered_players = [player for player in players if player_input.lower() in player.lower()]
            if filtered_players:
                for player in filtered_players:
                    if st.button(player):  # Create a button for each filtered player
                        selected_date = st.sidebar.radio("Select a Past Swing Date", list(date_to_player_map.keys()))
                        correct_player = date_to_player_map[selected_date]
                        # Check if the guess is correct and provide feedback
                        if player == correct_player:
                            st.success(f"Aced it! {player} is correct!")
                        else:
                            st.error(f"Good guess! But {player} is not correct. Please try again.")
            else:
                st.write("No matching players found.")
