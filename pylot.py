import json
import spotipy
import webbrowser
from dotenv import load_dotenv
load_dotenv()
import os

clientID = os.environ.get('SPOTIPY_CLIENT_ID')
clientSecret = os.environ.get('SPOTIPY_CLIENT_SECRET')
redirectURI = os.environ.get('SPOTIPY_REDIRECT_URI')

oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirectURI) 
token_dict = oauth_object.get_access_token() 
token = token_dict['access_token'] 
spotifyObject = spotipy.Spotify(auth=token) 
user_name = spotifyObject.current_user() 
  
print(json.dumps(user_name, sort_keys=True, indent=4))

while True: 
    print("Welcome to Pylot, " + user_name['display_name']) 
    print("0 - Exit the Terminal") 
    print("1 - Search for a Song") 
    user_input = int(input("Select 0 or 1 to proceed: ")) 
    if user_input == 1: 
        search_song = input("Enter the Song name: ") 
        results = spotifyObject.search(search_song, 1, 0, "track") 
        songs_dict = results['tracks'] 
        song_items = songs_dict['items'] 
        song = song_items[0]['external_urls']['spotify'] 
        webbrowser.open(song)
        print('The song you selected has opened in your browser') 
    elif user_input == 0: 
        print("Thank you for listening!") 
        break
    else: 
        print("Please enter either 0 or 1")