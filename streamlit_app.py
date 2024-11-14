import streamlit as st
# Set page config (for better control over the title and layout)
st.set_page_config(page_title="Tee it Up", page_icon=":golf:", layout="wide")

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



# st.image('TT.png', width = 500)

# Tab Buttons for navigation
tabs = ["Home", "Instructions", "Past Player List", "About"]
selected_tab = "Home"

st.markdown("""
<style>
    .stButton>button {
        margin-top: -50px;
        padding: 0px 0px;
        width: 100%;
        height: -10px;
        display: block;
    }
    .button-container {
        display: flex;
        gap: 0;
        justify-content: flex-start;
    }
</style>
""", unsafe_allow_html=True)

# Create a container to hold the buttons
with st.container():
    # Creating 4 columns for each tab button to appear next to each other
    col1, col2, col3, col4 = st.columns(4)  # 4 equal columns
    
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

        elif selected_tab == "Instructions":
            # Center the subheader
            st.markdown("""
            <style>
                /* Full page container to center content */
                .centered-container {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh; /* Full viewport height */
                    text-align: center;
                    flex-direction: column; /* Stack elements vertically */
                }
            </style>
            """, unsafe_allow_html=True)
            st.markdown('<div class="centered-container">', unsafe_allow_html=True)

            # Display the header and instructions inside the centered container
            st.markdown("<h2>How to Play:</h2>", unsafe_allow_html=True)
            st.write("""
                1. Look at the swing GIF displayed above.<br>
                2. Start typing the name of the PGA player you think is performing the swing.<br>
                3. Suggestions will appear based on your input.<br>
                4. Click on a suggestion to make your guess.<br>
                5. After selecting a player, feedback will be provided (correct or incorrect).
                """, unsafe_allow_html=True)
        
        elif selected_tab == "Past Player List":
            st.subheader("Past Player List")
            st.write("""
                Here we will display a list of previous player guesses.
            """)
        
            # Sample player history data for demonstration
            if st.session_state.player_history:
                player_data = [
                    (entry["date"], entry['https://vimeo.com/1029391107'])
                    for entry in st.session_state.player_history
                ]
                
                # Displaying plain URLs (not clickable)
                st.table(player_data)
            else:
                st.write("No player data available.")
        
        elif selected_tab == "About":
            st.subheader("About the Game")
            st.write("""
                This game lets you guess which PGA Tour player is performing a golf swing based on GIFs of their swings.
                It's a fun way to test your knowledge of the PGA players!
            """)
    
    # Main content area (centered)
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    
    if 'player_history' not in st.session_state:
        st.session_state.player_history = []

# Tab Content
if selected_tab == "Home":
    st.markdown(
    '''
     <h3 style="text-align: center; margin-top: -20px; font-size: 20px;">
        <span style="margin-right: 15px;">#1:</span>
        <span>11/14/2024</span>
    </h3>
    ''',
    unsafe_allow_html=True
)
    # # Display the GIF of the player's swing (replace with an actual player's swing GIF)
    # st.video("https://vimeo.com/1029391107")  # Example GIF URL
    
    # st.image("image0.gif")

    st.markdown(
    """
    <style>
        .centered-image {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 50%;  /* You can adjust the percentage to make the image smaller or larger */
        }
    </style>
    """, unsafe_allow_html=True)

#     st.markdown('''
#     <div style="display: flex; align-items: center; height: 90px;">
#         <img src="https://github.com/apcodes21/Tee_Time/blob/main/image0.gif?raw=true" alt="GIF" style="height: 500px; margin-center: 300px;">
#     </div>
# ''', unsafe_allow_html=True)


    st.markdown('''
        <div style="display: flex; justify-content: center; align-items: center; height: 45vh;">
            <img src="https://github.com/apcodes21/Tee_Time/blob/main/image0.gif?raw=true" alt="GIF" style="height: 495px;">
        </div>
    ''', unsafe_allow_html=True)

    # Vimeo video ID
    player_dict = {
    "name": "Scottie Scheffler",
    "video_id": "1029391107",
    "full_path": "https://player.vimeo.com/video/1029391107"
    }
    
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
        else:
            st.write("Player Options:.")
    
    st.markdown('</div>', unsafe_allow_html=True)
