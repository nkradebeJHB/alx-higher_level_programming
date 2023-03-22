#!/usr/bin/python3
"""
===================================================
A script that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa.
===================================================
"""

if __name__ == "__main__":
    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost:3306/{}'
                .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    the_ession = sessionmaker(bind=engine)
    session = the_session()
    state = session.query(State).\
        filter(State.name == argv[4])
    if state:
        print("{}".format(state[0].id)).order_by(State.id).all()
    else:
        print("Not found")
    session.close()
