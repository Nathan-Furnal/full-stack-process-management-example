from datetime import date, timedelta

from backend.models import Attachment, Event, Link, Process
from backend.models.process import ProcessPerformance


def test_can_create_link(session):
    url = "file://example"
    link = Link(url=url)
    session.add(link)
    session.commit()

    link = session.get(Link, link.id)
    assert link
    assert link.url == url


def test_can_create_attachment(session):
    filename = "example_file.txt"
    attach = Attachment(filename=filename)
    session.add(attach)
    session.commit()

    attach = session.get(Attachment, attach.id)
    assert attach
    assert attach.filename == filename


def test_can_create_event(session):
    urls = ["file://example1", "file://example2"]
    filenames = ["example1.txt", "example2.txt"]
    links = []
    attachments = []
    data = {"type": "demo event", "explanation": "Demo explanation"}
    event = Event(**data)
    session.add(event)
    session.commit()
    for u in urls:
        links.append(Link(url=u, event=event))
    session.add_all(links)
    for f in filenames:
        attachments.append(Attachment(filename=f, event=event))
    session.add_all(attachments)
    session.commit()

    event = session.get(Event, event.id)
    assert event
    assert event.type == data["type"]
    assert event.explanation == data["explanation"]
    assert {link.id for link in links} == {link.id for link in event.links}
    assert {att.id for att in attachments} == {att.id for att in event.attachments}


def test_can_create_process(session):
    data = {
        "business_date": date.today(),
        "working_date": date.today() + timedelta(days=7),
        "service": "Demo service",
        "performance": ProcessPerformance.GREEN,
    }
    process = Process(**data)
    session.add(process)
    session.commit()

    process = session.get(Process, process.id)
    assert process
    assert process.business_date == data["business_date"]
    assert process.working_date == data["working_date"]
    assert process.service == data["service"]
    assert process.performance == data["performance"]
