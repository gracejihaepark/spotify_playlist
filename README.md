# Spotify Playlist
Create Spotify playlists similar to Spotify radio, but with multiple artist inputs

## Goals
- Use Spotify's Web API, Spotipy, to create playlists with songs similar to more than one artist input
  - Spotify radio only allows you to search one entity to find a station with artists/songs similar to that input; wanted to create playlists that incorporated similar/recommended songs of more than one artist

## Method
1. Artist IDs are the most important in searching for similar/recommended artists/songs
  - Each searched artist outputs a complex dictionary of dictionaries and lists that need to be parsed in order to get the artist's ID
  ```
  # search artist(s) and get their ID(s)
  artist_id = []
  for artist in artists:
      search_artist = sp.search(q=artist, type='artist')
      artist_id.append(search_artist['artists']['items'][0]['id'])
  ```
  (An example of how I needed to parse these heavily nested dictionaries and lists.)

2. With the artist IDs now, the recommended module can be used to find recommended songs for the artist
  - Here, we need to now retrieve the song track IDs so that we can put the songs into the playlist that's being made

3. Recommended tracks for each artist did not make the playlist diverse enough, so took the top 20 most related artists for each artist that was initially searched
  - Again, the IDs for these related artists are needed to find any relevant songs

4. With these related artists' IDs, took their top tracks to add on to the playlist

5. Randomized the list of songs and created playlist with songs and artists similar to the artists that were input
  - If you input a hip hop artist, indie artist, and classical musician, the playlist would essentially be the three artists' radios put together in one playlist

## Why
There were many times that I wished I could combine the different genres of music that I liked into one playlist without having to manually create my own playlists. I love the radio feature in Spotify, as it really creates a station with songs that are related to the artist I search, so I wanted to create a mix between the radio and playlist features.

## Trial and Error
The biggest problem was the number of songs in these created playlists--there were too many. After testing the system on friends, I received feedback to narrow the playlist to around 30-75 songs.
- I thought songs related to the initially searched artists were important, so I pulled 10 recommended songs for each input artist
- Songs of related artists made the playlist a little more diverse, so I included 5 songs for each
- Example: If three artists were searched to create a playlist, the new playlist would have 30(10 + 10 + 10) recommended songs and 15(5 + 5 + 5) related artists' songs for a total of 45 songs
