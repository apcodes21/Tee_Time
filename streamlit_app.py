import streamlit as st

import streamlit as st

# Set page config (for better control over the title and layout)
st.set_page_config(page_title="Professional Webpage", page_icon=":book:", layout="wide")

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
            font-size: 24px;
            color: #333333;
            margin-top: 10px;
            text-align: center;
        }
        .toc {
            font-size: 18px;
            font-weight: bold;
            color: #4CAF50;
            padding: 10px;
            background-color: #f4f4f4;
            border-radius: 8px;
        }
        .toc-item {
            padding-left: 20px;
            margin-bottom: 5px;
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
st.markdown('<p class="header">Welcome to My Professional Webpage</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">An example of a professional header and table of contents</p>', unsafe_allow_html=True)

# Table of Contents Sidebar (Navigation links)
toc = """
    <div class="toc">
        <div class="toc-item"><a href="#section1">1. Introduction</a></div>
        <div class="toc-item"><a href="#section2">2. Features</a></div>
        <div class="toc-item"><a href="#section3">3. Use Cases</a></div>
        <div class="toc-item"><a href="#section4">4. Contact</a></div>
    </div>
"""
st.sidebar.markdown(toc, unsafe_allow_html=True)

# Section 1: Introduction
st.markdown('<a id="section1"></a>', unsafe_allow_html=True)
st.header('1. Introduction')
st.write("This is the introduction section. You can add any content here.")

# Section 2: Features
st.markdown('<a id="section2"></a>', unsafe_allow_html=True)
st.header('2. Features')
st.write("This section describes the features of the webpage.")

# Section 3: Use Cases
st.markdown('<a id="section3"></a>', unsafe_allow_html=True)
st.header('3. Use Cases')
st.write("Here are some example use cases for the application or webpage.")

# Section 4: Contact
st.markdown('<a id="section4"></a>', unsafe_allow_html=True)
st.header('4. Contact')
st.write("You can contact us at: contact@mywebpage.com")



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
st.image('TT.png')

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

if 'player_history' not in st.session_state:
    st.session_state.player_history = []



# Tab Content
if selected_tab == "Home":
    st.subheader("#1: 11/14/2024")
    st.subheader("Welcome to the PGA Player Swing Guessing Game!")
    st.write("""
        Look at the swing GIF and try to guess the player performing the swing. You can select the player's name 
        from the suggestions that appear as you type.
    """)
    # # Display the GIF of the player's swing (replace with an actual player's swing GIF)
    # st.video("https://vimeo.com/1029391107")  # Example GIF URL

    # Vimeo video ID
    player_dict = {
    "name": "Scottie Scheffler",
    "video_id": "1029391107",
    "full_path": "https://player.vimeo.com/video/1029391107"
    }
    
    video_id = "1029391107"  # Replace with your Vimeo video ID
    
    # Embed the Vimeo video with autoplay and loop enabled
    embed_code = f"""
    <iframe src="https://player.vimeo.com/video/{video_id}?autoplay=1&loop=1" width="640" height="360" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
    """
    # Display the embedded video using markdown
    st.markdown(embed_code, unsafe_allow_html=True)

    
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
    
    # Text input box for user to type the player's name
    player_input = st.text_input("Start typing the name of the PGA player & press enter:", placeholder="Guess the Tour Pro")

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
                    correct_player = "Scottie Scheffler"  # Replace this with the actual player for the GIF

                    # Check if the guess is correct and provide feedback
                    if guess == correct_player:
                        st.success(f"Congratulations! {guess} is correct!")
                    else:
                        st.error(f"Oops! {guess} is not correct. Try again.")
        else:
            st.write("No matching players found.")
    else:
        st.write("Player Options:.")



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

st.markdown('</div>', unsafe_allow_html=True)


