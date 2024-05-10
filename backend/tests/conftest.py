import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, StaticPool

from backend.db import Base, get_engine
from backend.main import app


# https://fastapi.tiangolo.com/advanced/testing-database/
@pytest.fixture(scope="session")
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
def webclient(engine):
    app.dependency_overrides[get_engine] = lambda: engine
    return TestClient(app)
