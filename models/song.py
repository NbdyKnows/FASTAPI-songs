from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta

songs = Table("songs", meta, 
                Column("id", Integer, primary_key=True),
                Column("name", String(255)),
                Column("artist", String(255)),
                Column("album", String(255)),
                Column("year", Integer))

meta.create_all(engine)