import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

db = create_engine('postgresql://employ.psql')  # database engine object from SQLAlchemy that manages connections to the database
# DATABASE_URL is an environment variable that indicates where the database lives
db.echo=True
conn=db.connect()
# create a 'scoped session' that ensures different users' interactions with the
# database are kept separate

flights = conn.execute(
    "SELECT origin, destination, duration FROM flights").fetchall()  # execute this SQL command and return all of the results
for flight in flights:
    print(
        f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")  # for every flight, print out the flight info
