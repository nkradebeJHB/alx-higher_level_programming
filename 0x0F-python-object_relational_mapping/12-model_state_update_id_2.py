#!/usr/bin/python3
"""
=========================================================
A script that changes the name of a State object from the
database hbtn_0e_6_usa
=========================================================
"""

from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost:3306/{}'
                .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    the_session = sessionmaker(bind=engine)
    session = the_session()
    state = session.query(State).filter(State.id == 2).all()
    if state:
        state[0].name = "New Mexico"
    session.commit()
    session.close()
