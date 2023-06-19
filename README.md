# Billboard-hot-100-project
A Python code that helps you scrape the top 100 Billboard songs of any year and create a new Spotify playlist using Spotify API.

The Python code utilizes web scraping techniques to extract the top 100 Billboard songs of a specific year from a website. It accesses the necessary HTML elements containing the song information such as the song name, artist, and rank. This data is then processed and formatted accordingly.

To create a new Spotify playlist, the code interacts with the Spotify API. It authenticates the user using their Spotify credentials and obtains an access token. With the access token, the code can search for each song on Spotify, retrieve their respective track IDs, and add them to a new playlist.

The code ensures that the playlist is unique by checking if the songs already exist in the user's library or playlist before adding them. This prevents duplicates and maintains a clean playlist.

By combining web scraping techniques and the power of the Spotify API, this Python code enables users to effortlessly gather the top 100 Billboard songs of any year and create a curated Spotify playlist with their favorite hits.
