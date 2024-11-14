
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
    #replace with other GIFS:
    {"date": "11/07/2024", "gif_url": "https://github.com/apcodes21/Tee_Time/blob/main/golf-xander-schauffele.gif?raw=true"},
    {"date": "10/31/2024", "gif_url": "https://github.com/apcodes21/Tee_Time/blob/main/image2.gif?raw=true"},
    # Add more records as necessary
    ]

# 1. as sidebar menu
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
# st.markdown('<p class="header">Guess the PGA Players swing</p>', unsafe_allow_html=True)
st.markdown('''
    <div style="display: flex; align-items: center; height: 82px;">
        <img src="https://github.com/apcodes21/Tee_Time/blob/main/TT.png?raw=true" alt="PGA Logo" style="height: 82px; margin-right: 0px;">
        <p class="header" style="font-size: 32px; margin: 0;">Guess the PGA Players swing</p>
    </div>
''', unsafe_allow_html=True)


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
            padding: 15px 0;
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
            margin-top: 0px;
            margin-bottom: 0px;
            padding-top: 0px;
        }

        .tab-buttons button {
            background-color: #333;
            color: black;
            padding: 10px 20px;
            border: none;
            margin: 0 0px;
            cursor: pointer;
            font-size: 16px;
        }

        .tab-buttons button:hover {
            background-color: #333;
        }

        /* Full-width content */
        .content {
            width: 100%;
            padding: 0px;
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
            width: 50%;
            max-width: 1000px; /* Limit max width to prevent over-expansion */
            margin-top: 10px;
        }

        /* Make buttons for tabs appear full width and centered */
        .tab-buttons button {
            width: auto;
            margin: 0 -10px;
        }
    </style>
""", unsafe_allow_html=True)

st.subheader("#1: 11/14/2024")

# st.image('TT.png', width = 500)

# Tab Buttons for navigation
tabs = ["Home", "Instructions", "Past Player List", "About"]
selected_tab = "Home"

if selected_tab == "Home":
    # Check if a user has clicked a past swing date, show the corresponding video
    if 'selected_swing' in st.session_state:
        selected_swing = st.session_state.selected_swing
        st.markdown(f'<div style="display: flex; justify-content: center; align-items: center; height: 45vh;">'
                    f'<img src="{selected_swing["gif_url"]}" alt="GIF" style="height: 495px;"></div>', unsafe_allow_html=True)
    else:
        # If no swing is selected, show a default GIF or URL
        default_url = "https://github.com/apcodes21/Tee_Time/blob/main/image0.gif?raw=true"  # Change this to your desired default URL
        st.markdown(f'<div style="display: flex; justify-content: center; align-items: center; height: 45vh;">'
                    f'<img src="{default_url}" alt="Default GIF" style="height: 495px;"></div>', unsafe_allow_html=True)


    # st.subheader("#1: 11/14/2024")
#     '''
#      <h3 style="text-align: center; margin-top: -20px; font-size: 20px;">
#         <span style="margin-right: 15px;">#1:</span>
#         <span>11/14/2024</span>
#     </h3>
#     ''',
#     unsafe_allow_html=True
# )

    # st.markdown(
    # """
    # <style>
    #     .centered-image {
    #         display: block;
    #         margin-left: auto;
    #         margin-right: auto;
    #         width: 50%;  /* You can adjust the percentage to make the image smaller or larger */
    #     }
    # </style>
    # """, unsafe_allow_html=True)
    # st.markdown('''
    #     <div style="display: flex; justify-content: center; align-items: center; height: 45vh;">
    #         <img src="https://github.com/apcodes21/Tee_Time/blob/main/image0.gif?raw=true" alt="GIF" style="height: 495px;">
    #     </div>
    # ''', unsafe_allow_html=True)
    
    # List of players for guessing
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
    "Si Woo Kim", "Bryan Gay", "Charles Howell III", "Robert Streb", "Alex Noren",
    "Tom Hoge", "Jason Kokrak", "Luke List", "Richard Bland", "Gary Woodland",
    "Scott Piercy", "Danny Lee", "Michael Thompson", "Aaron Wise", "Adam Hadwin",
    "Patton Kizzire", "Brian Gay", "Charley Hoffman", "Stewart Cink", "Pat Perez",
    "Dylan Frittelli", "Andrew Putnam", "Joel Dahmen", "Scott Brown", "Kevin Na",
    "Lucas Herbert", "Billy Mayfair", "Jim Furyk", "Bryce Garnett", "Troy Merritt",
    "Kyle Stanley", "Brendan Steele", "Russell Knox", "Kevin Chappell", "Wyndham Clark",
    "J.B. Holmes", "Mark Wilson", "Henrik Norlander", "Austin Cook", "Joel Dahmen",
    "Sam Saunders", "Jesse Mueller", "Adam Long", "Zac Blair", "David Lipsky",
    "Brandon Hagy", "Chad Ramey", "Martin Laird", "Chris Stroud", "Mackenzie Hughes",
    "Cameron Champ", "Ryan Moore", "Matt Jones", "James Hahn", "Harold Varner III",
    "Eric Cole", "Troy Merritt", "Vaughn Taylor", "Chris Baker", "Doug Ghim",
    "D.J. Trahan", "Cameron Percy", "Michael Kim", "Ben Martin", "Stewart Cink",
    "Vince Whaley", "Justin Suh", "Tyler Duncan", "Jared Wolfe", "David Toms",
    "Ryan Armour", "Kurt Kitayama", "Nick Watney", "Peter Malnati", "Brice Garnett",
    "Brian Stuard", "Bertie O'Neill", "Chad Campbell", "Jimmy Walker", "Jason Dufner",
    "Morgan Hoffmann", "Matt Every", "Ricky Barnes", "Craig Stadler", "Curtis Strange",
    "Mark O'Meara", "John Daly", "Tom Watson", "Bernhard Langer", "Fred Couples",
    "Raymond Floyd", "Lee Trevino", "Tom Kite", "Hale Irwin", "Johnny Miller",
    "Jack Nicklaus", "Gary Player", "Arnold Palmer", "Bobby Jones", "Sam Snead",
    "Gene Sarazen", "Ben Hogan", "Walter Hagen", "Julius Boros", "Fuzzy Zoeller",
    "Ken Venturi", "Tom Weiskopf", "David Duval", "Chris DiMarco", "Paul Azinger",
    "Mark Calcavecchia", "Scott Hoch", "Nick Price", "Mark McNulty", "Greg Norman",
    "Jim Furyk", "Phil Mickelson", "Mike Weir", "Bernhard Langer", "Fred Funk"
]

st.markdown("""
    <style>
    .stTextInput input {
        background-color: #272626;  /* Adjust this color to match your background */
        color: white;             /* Make the text color same as the background */
    }
    .stTextInput input::placeholder {
        color: white;             /* Make placeholder text blend as well */
    }
    
    /* Add spacing between buttons */
    .stButton>button {
        margin-top: 5px;  /* Adjust this value to increase vertical spacing between buttons */
        width: 100%;
        padding: 10px;  /* Adjust padding as needed */
    }
    
    # /* Optional: Ensure button container has some spacing too */
    # .stButton {
    #     margin-bottom: 5px;
    # }
    
    </style>
    """, unsafe_allow_html=True)
if selected_tab == "Home":
    # Create a container for the input box to control width
    col1, col2, col3 = st.columns([1, 1, 1])  # Adjust the column ratios to control the width
    
    with col2:
        player_input = st.text_input("", placeholder="Guess the Tour Pro Name")
    
        # # Only show suggestions if the user has typed something
        # if player_input:
        #     # Filter players based on the input text
        #     filtered_players = [player for player in players if player_input.lower() in player.lower()]
        
        #     # If there are matching players, display them as clickable buttons
        #     if filtered_players:
        #         for player in filtered_players:
        #             if st.button(player):  # Create a button for each filtered player
        #                 # If a suggestion is clicked, store the player's name as the guess
        #                 guess = player
        #                 # Correct player for the swing (you can change this dynamically based on the GIF)
        #                 correct_player = "Scottie Scheffler"  # Replace this with the actual player for the GIF
        
        #                 # Check if the guess is correct and provide feedback
        #                 if guess == correct_player:
        #                     st.success(f"Aced it! {guess} is correct!")
        #                 else:
        #                     st.error(f"Good guess! But {guess} is not correct. Please try again.")
        #     else:
        #         st.write("No matching players found.")
        # else:
        #     st.write("Player Options:.")
        # Check for pressing "Enter" and clear input
        
        if player_input:
            filtered_players = [player for player in players if player_input.lower() in player.lower()]
            st.session_state.player_guess = player_input
            
            if filtered_players:
                for player in filtered_players:
                    if st.button(player):
                        # Check if the guess is correct
                        if player == correct_player:
                            st.success(f"Correct! {player} is the player!")
                        else:
                            st.error(f"Wrong guess! {player} is not the player. Try again!")
                        st.session_state.player_guess = ''
            else:
                st.write("No matching players found.")
        else:
            st.write("Start typing the player's name to get suggestions.")
    
    st.markdown('</div>', unsafe_allow_html=True)
