#!/usr/bin/python3
"""Start link class to table in database """
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb:'
                           '//{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    # Create new state object
    new_state = State(name="Louisiana")
    # Add new state to session, it is now 'pending'
    session.add(new_state)
    # Commit the change to the database
    session.commit()
    # Get the id number of the added state
    state = session.query(State).filter(State.name == "Louisiana").first()
    print(state.id)
