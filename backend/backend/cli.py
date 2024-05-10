from backend.db import Base, get_engine


def setup():
    engine = get_engine()
    Base.metadata.create_all(engine)


def clear():
    engine = get_engine()
    Base.metadata.drop_all(engine)
