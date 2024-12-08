from musiclibrary import MusicLibrary, TrackArrayList, Track
from arraylist import ArrayList
from playlist import Playlist
from datetime import timedelta
import json
musiclib = 'database\\musiclibrary.json'
playlists = 'database\\playlists.json'

def read(db):
    path = ''
    if db=='musiclibrary': 
        path = musiclib
    elif db == 'playlists':
        path = playlists
    with open(path, 'r') as f:
        jsondata = json.loads(f.read())
    return jsondata

def parsemusiclib(data:dict):
    ml = MusicLibrary()
    for t in data:
        track = Track(t['title'],t['artist'], timedelta(seconds=t['duration']))
        ml.insert(track)
    return ml

def parseplaylists(data:dict):
    pl = ArrayList()
    for playlist in data:
        temp = Playlist(playlist['title'])
        for t in playlist['tracks']:
            track = Track(t['title'],t['artist'],timedelta(seconds=t['duration']))
            temp.insert(track)
        pl.insert(temp)
    return pl

def load(db:str):
    if db=='musiclibrary': 
        data = read(db)
        return parsemusiclib(data)
    elif db == 'playlists':
        data = read(db)
        return parseplaylists(data)

def dumptrack(t:Track):
    track = {}
    track['title'] = t.getTitle()
    track['artist'] = t.getArtist()
    track['duration'] = t.getDuration().total_seconds()
    return track

def dumpmusiclib(musiclib:MusicLibrary):
    l = []
    for track in musiclib.get_list():
        l.append(dumptrack(track))
    return l

def dumpplaylist(playlist:Playlist):
    pl = {}
    pl['title'] = playlist.title()
    pl['tracks'] = []
    for track in playlist.get_list():
        pl['tracks'].append(dumptrack(track))
    return pl

def dumpplaylists(arr:TrackArrayList):
    l = []
    for playlist in arr.get_list():
        temp = {}
        temp['title'] = playlist.title()
        temp['tracks'] = []
        for track in playlist.get_list():
            temp['tracks'].append(dumptrack(track))
        l.append(temp)
    return l
def save(db, type=''):
    if type == 'musiclibrary':
        with open(musiclib, 'w') as f:
            s = json.dumps(dumpmusiclib(db))
            f.write(s)
    elif type == 'playlists':
        with open(playlists, 'w') as f:
            s = json.dumps(dumpplaylists(db))
            f.write(s)