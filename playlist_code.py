import sys
import spotipy
import spotipy.util as util
import config
import json
import pandas as pd
import random


scope = 'playlist-modify-public'
token = util.prompt_for_user_token(config.user_me,
                           scope,
                           client_id=config.client_id,
                           client_secret=config.client_secret,
                           redirect_uri=config.redirect_uri)
sp = spotipy.Spotify(auth=token)


# list of artists (up to five)
artists = ['', '', '', '', ''] # examples of up to five

# search artist and get their id(s)
artist_id = []
for artist in artists:
    search_artist = sp.search(q=artist, type='artist')
    artist_id.append(search_artist['artists']['items'][0]['id'])


# recommended tracks ids for searched artists
recommended_track_ids = []
track_limit = (len(artist_id) * 10)
tracks = sp.recommendations(seed_artists=artist_id, limit=track_limit)
for i in range (0, len(tracks['tracks'])):
    recommended_track_ids.append(tracks['tracks'][i]['id'])



# 20 related artists ids for each searched artist
related_artist_ids = []
related_artist_ids.extend(artist_id)
for id in artist_id:
    related_artists = sp.artist_related_artists(id)
    for dict in related_artists['artists']:
        related_artist_ids.append(dict['id'])


# related artists' top tracks
related_artists_tracks = []
for i in range (0, len(related_artist_ids)):
    related_artists_tracks.append(sp.artist_top_tracks(related_artist_ids[i])['tracks'])


# related artists' top tracks' ids
related_artist_track_ids = []
for items in related_artists_tracks:
    for dict in items:
        related_artist_track_ids.append(dict['id'])

len(related_artist_track_ids)
unique_tracks = list(set(related_artist_track_ids))
len(unique_tracks)
# random.shuffle(unique_tracks)

related_track_ids = unique_tracks[:(len(artist_id) * 5)]




# create playlist
trial_playlist = sp.user_playlist_create(config.user_me, "wip", description='recommended tracks')
# add tracks to playlist
sp.user_playlist_add_tracks(config.user_me, trial_playlist['id'], recommended_track_ids)
sp.user_playlist_add_tracks(config.user_me, trial_playlist['id'], related_track_ids)
