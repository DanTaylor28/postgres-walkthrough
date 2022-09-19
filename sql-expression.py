from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing the instructions from our localhost "chinook" database
db = create_engine("postgresql:///chinook")

meta = MetaData(db)

# create variable for "artist" table
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# create varable for "Album" table
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("Artist_table.ArtistId"))
)

# create variable for "Track" table
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

# making the connection
with db.connect() as connection:
    
    # query 1 - select all records from the "artist" table
    # select_query = artist_table.select()

    # query 2 - select only the "Name" column from the "artist" table
    # select_query = artist_table.select().with_only_columns(
    #     [artist_table.c.Name])

    # query 3 - select only queen from "Artist" table
    # select_query = artist_table.select().where(
    # artist_table.c.Name == "Queen")

    # query 4 - select only by "ArtistId" #51 from "Artist" table
    # select_query = artist_table.select().where(artist_table.c.ArtistId == 51)

    # query 5 - select only the albums with "ArtistId" 
    # of 51 on the "album" table
    # select_query = album_table.select().where(album_table.c.ArtistId == 51)

    # query 6 - select all tracks where the "Composer" 
    # is "Queen" from the "Track" table
    # select_query = track_table.select().where(
    #     track_table.c.Composer == "Queen")

    results = connection.execute(select_query)
    for result in results:
        print(result)

