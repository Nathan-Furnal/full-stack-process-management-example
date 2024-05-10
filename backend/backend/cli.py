import argparse

from backend.db import Base, get_engine
from backend.models import Attachement, Event, Link, Process
from backend.scripts.demo import create_processes

# Make models available in the namespace such that Base.metadata finds them
_ = Process, Event, Link, Attachement


def setup():
    engine = get_engine()
    Base.metadata.create_all(engine)


def get_table_names():
    return Base.metadata.tables.keys()


def clear():
    engine = get_engine()
    Base.metadata.drop_all(engine)


def populate():
    return create_processes()


parser = argparse.ArgumentParser(description="Process Manager backend controls")
subparsers = parser.add_subparsers(dest="cmd")

creation_cmd = subparsers.add_parser("createdb", help="Create the DB")
creation_cmd.add_argument(
    "-d",
    "--data",
    action="store_true",
    help="When this flag is used, the DB is populated with demo data",
)

deletion_cmd = subparsers.add_parser("deletedb", help="Delete the DB")


if __name__ == "__main__":
    args = parser.parse_args()
    match args.cmd:
        case "createdb":
            setup()
            print(f"=> Tables: [{', '.join(get_table_names())}] were created.")
            if args.data:
                populate()
                print("=> DB was populated with demo data.")
        case "deletedb":
            clear()
            print("=> All tables were dropped.")
        case _:
            raise ValueError(f"Unknown command {args.cmd}")
