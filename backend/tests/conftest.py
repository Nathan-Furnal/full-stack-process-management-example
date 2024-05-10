import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, StaticPool
from sqlalchemy.orm import sessionmaker

from backend.db import Base, get_session
from backend.main import app


# https://fastapi.tiangolo.com/advanced/testing-database/
@pytest.fixture
def engine():
    engine = create_engine(
        "sqlite+pysqlite:///:memory:",
        echo=True,
        poolclass=StaticPool,
        connect_args={"check_same_thread": False},
    )
    try:
        Base.metadata.create_all(bind=engine)
        yield engine
    finally:
        Base.metadata.drop_all(bind=engine)


@pytest.fixture
def session_maker(engine):
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture
def session(session_maker):
    try:
        sess = session_maker()
        yield sess
    finally:
        sess.close()


@pytest.fixture
def webclient(session):
    app.dependency_overrides[get_session] = lambda: session
    return TestClient(app)
