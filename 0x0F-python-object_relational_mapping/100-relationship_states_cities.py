#!/usr/bin/python3
""" Script that creates the State “California” with the City “San Francisco”
    from the database hbtn_0e_100_usa """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Get MySQL username, password, and database name from command line arguments
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Database connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create new State and City objects
    new_state = State(name="California")
    new_city = City(name="San Francisco", state=new_state)

    # Add the State and City objects to the session
    session.add(new_state)
    session.add(new_city)

    # Commit changes to the database
    session.commit()

    # Close the session
    session.close()

