from datetime import date, timedelta

from sqlalchemy.orm import Session

from backend.models import Attachement, Event, Link, Process
from backend.models.process import ProcessPerformance


def test_can_create_link(engine):
    url = "file://example"
    with Session(engine) as session:
        link = Link(url=url)
        session.add(link)
        session.commit()

        link = session.get(Link, link.id)
        assert link
        assert link.url == url


def test_can_create_attachement(engine):
    filename = "example_file.txt"
    with Session(engine) as session:
        attach = Attachement(filename=filename)
        session.add(attach)
        session.commit()

        attach = session.get(Attachement, attach.id)
        assert attach
        assert attach.filename == filename


def test_can_create_event(engine):
    urls = ["file://example1", "file://example2"]
    filenames = ["example1.txt", "example2.txt"]
    links = []
    attachements = []
    data = {"type": "demo event", "explanation": "Demo explanation"}
    with Session(engine) as session:
        event = Event(**data)
        session.add(event)
        session.commit()
        for u in urls:
            links.append(Link(url=u, event=event))
        session.add_all(links)
        for f in filenames:
            attachements.append(Attachement(filename=f, event=event))
        session.add_all(attachements)
        session.commit()

        event = session.get(Event, event.id)
        assert event
        assert event.type == data["type"]
        assert event.explanation == data["explanation"]
        assert {link.id for link in links} == {link.id for link in event.links}
        assert {att.id for att in attachements} == {att.id for att in event.attachments}


def test_can_create_process(engine):
    data = {
        "business_date": date.today(),
        "working_date": date.today() + timedelta(days=7),
        "service": "Demo service",
        "performance": ProcessPerformance.GREEN,
    }
    with Session(engine) as session:
        process = Process(**data)
        session.add(process)
        session.commit()

        process = session.get(Process, process.id)
        assert process
        assert process.business_date == data["business_date"]
        assert process.working_date == data["working_date"]
        assert process.service == data["service"]
        assert process.performance == data["performance"]
