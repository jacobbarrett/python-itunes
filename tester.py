import itunes

# Lookup Achtung Baby album by U2
U2_ACHTUNGBABY_ID = 475390461
album = itunes.lookup(U2_ACHTUNGBABY_ID)

print album.get_url()
print album.get_artwork()

artist = album.get_artist()
tracks = album.get_tracks()

# Lookup song One from Achtung Baby album by U2
U2_ONE_ID = 475391315
track = itunes.lookup(U2_ONE_ID)

artist = track.get_artist()
album = track.get_album()