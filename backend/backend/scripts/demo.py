import random
from datetime import date, timedelta

from sqlalchemy.orm import InstrumentedAttribute, Session

from backend.db import get_session
from backend.models import Attachement, Event, Link, Process
from backend.models.process import ProcessPerformance


def sample(pop, k):
    return random.sample(pop, k)


def rnd_items(session: Session, db_attr: InstrumentedAttribute, filters: list):
    table = db_attr.parent
    return session.query(table).filter(db_attr.in_(filters)).all()


def next_business_day(d: date):
    if d.weekday() in (4, 5, 6):  # Friday-Sunday
        return d + timedelta(days=(7 - d.weekday()))  # Next monday
    return d + timedelta(days=1)  # Next day


def create_links(session=next(get_session())):
    links = []
    urls = [
        "http://example.com",
        "https://google.com",
        "https://demo.test",
        "https://demo.acme.test",
        "https://random.be",
        "https://fruityloopy.fr",
        "https://another.one.test",
        "https://you.shall.pass.net",
        "https://grab.a.beer",
        "https://rising.sun.house",
    ]
    for u in urls:
        links.append(Link(url=u))
    session.add_all(links)
    session.commit()
    return urls


def create_attachments(session=next(get_session())):
    attachements = []
    filenames = [
        "example.txt",
        "random.zip",
        "herebedragons.txt",
        "demo.txt.zip",
        "report2.pdf",
        "nothingelsematters.py",
        "makeitrain.xlsx",
        "read_this.docx",
        "court_of_the_crimson_king.rb",
        "IAMBlue.rgb",
    ]
    for f in filenames:
        attachements.append(Attachement(filename=f))
    session.add_all(attachements)
    session.commit()
    return filenames


def create_events(session=next(get_session())):
    urls = create_links(session)
    filenames = create_attachments(session)
    lurl = Link.url
    afname = Attachement.filename

    events = []
    infos = [
        {
            "type": "random",
            "explanation": "This is a demo event",
            "links": rnd_items(session, lurl, sample(urls, 4)),
            "attachments": rnd_items(session, afname, sample(filenames, 4)),
        },
        {
            "type": "example",
            "explanation": "This is created for example purposes",
            "links": rnd_items(session, lurl, sample(urls, 4)),
            "attachments": rnd_items(session, afname, sample(filenames, 4)),
        },
        {
            "type": "normal",
            "explanation": "This is another demo",
            "links": rnd_items(session, lurl, sample(urls, 4)),
            "attachments": rnd_items(session, afname, sample(filenames, 4)),
        },
        {
            "type": "example",
            "explanation": "Secret?",
            "links": rnd_items(session, lurl, sample(urls, 4)),
            "attachments": rnd_items(session, afname, sample(filenames, 4)),
        },
        {
            "type": "normal",
            "explanation": "This is an official statement",
            "links": rnd_items(session, lurl, sample(urls, 4)),
            "attachments": rnd_items(session, afname, sample(filenames, 4)),
        },
    ]
    for info in infos:
        events.append(Event(**info))
    session.add_all(events)
    session.commit()
    return [e.id for e in events]


def create_processes(session=next(get_session())):
    wd = date.today()
    bd = next_business_day(wd)
    event_ids = create_events(session)
    infos = [
        {
            "service": "Example service",
            "performance": random.choice(list(ProcessPerformance)),
            "events": session.query(Event).filter(Event.id.in_(event_ids[:2])).all(),
        },
        {
            "service": "New service",
            "performance": random.choice(list(ProcessPerformance)),
            "events": session.query(Event).filter(Event.id.in_(event_ids[2:])).all(),
        },
        {
            "service": "Old service",
            "performance": random.choice(list(ProcessPerformance)),
        },
    ]
    processes = []
    for info in infos:
        info |= {"business_date": bd, "working_date": wd}
        processes.append(Process(**info))
    session.add_all(processes)
    session.commit()

    return [p.id for p in processes]
