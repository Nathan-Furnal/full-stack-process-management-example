from functools import lru_cache
from pathlib import Path

from sqlalchemy import create_engine, Engine, event
from sqlalchemy.orm import DeclarativeBase

DB_PATH = Path(__file__).parent.parent.parent / "data" / "process_management.db"


class Base(DeclarativeBase):
    pass


@lru_cache
def get_engine():
    engine = create_engine(f"sqlite+pysqlite:///{DB_PATH}")
    return engine


# https://docs.sqlalchemy.org/en/20/dialects/sqlite.html#foreign-key-support
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.execute("PRAGMA journal_mode=wal")
    cursor.execute("PRAGMA synchronous=normal")
    cursor.execute("PRAGMA journal_size_limit=6144000")
    cursor.close()
