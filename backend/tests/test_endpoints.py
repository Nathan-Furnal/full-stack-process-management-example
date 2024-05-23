from datetime import date, timedelta

import pytest
from sqlalchemy.orm import make_transient

from backend.models import Process
from backend.models.process import ProcessPerformance


@pytest.fixture
def dummy_process(session):
    data = {
        "business_date": date.today(),
        "working_date": date.today() + timedelta(days=7),
        "service": "Demo service",
        "performance": ProcessPerformance.GREEN,
    }
    process = Process(**data)
    session.add(process)
    session.commit()

    session.refresh(process)
    session.expunge(process)

    make_transient(process)

    return process


def test_get_process_by_id(webclient, dummy_process):
    res = webclient.get(f"/processes/{dummy_process.id}")
    assert res.status_code == 200, res.text

    data = res.json()

    assert data["id"] == dummy_process.id
    assert data["business_date"] == str(dummy_process.business_date)
    assert data["working_date"] == str(dummy_process.working_date)
    assert data["service"] == dummy_process.service
    assert data["performance"] == dummy_process.performance.value
    assert data["events"] == dummy_process.events


def test_get_all_processes(webclient, dummy_process):
    res = webclient.get("/processes/")
    assert res.status_code == 200, res.text

    data = res.json()
    assert len(data) == 1
    assert data[0]["id"] == dummy_process.id


def test_create_process(webclient, session):
    payload = {
        "business_date": "2024-05-16",
        "working_date": "2024-05-17",
        "service": "Demo service",
        "performance": "GREEN",
        "events": [
            {
                "type": "Example event",
                "explanation": "Explanation for an example event",
                "links": [{"url": "http://example.com"}, {"url": "https://demo.test"}],
                "attachments": [
                    {"filename": "example.txt"},
                    {"filename": "demo.py"},
                    {"filename": "values.csv"},
                ],
            },
            {
                "type": "Another event",
                "explanation": "Explanation for yet another event",
                "links": [{"url": "http://demo.be"}, {"url": "https://fake.test"}],
                "attachments": [
                    {"filename": "fake.data.txt"},
                    {"filename": "msg.tar.gz"},
                    {"filename": "presentation.pptx"},
                ],
            },
        ],
    }
    res = webclient.post("/processes/", json=payload)
    assert res.status_code == 200, res.text
    data = res.json()

    process = session.get(Process, data["id"])
    assert process
    assert process.service == payload["service"]
    assert str(process.working_date) == payload["working_date"]
    assert str(process.business_date) == payload["business_date"]
    assert process.performance.value == payload["performance"]
    assert {e.type for e in process.events} == {e["type"] for e in payload["events"]}
    zipped_comparable_events = zip(  # Make sure events are aligned for comparison
        sorted(process.events, key=lambda e: e.type),
        sorted(payload["events"], key=lambda e: e["type"]),
    )
    # Deep equality
    for db_event, dict_event in zipped_comparable_events:
        assert {link.url for link in db_event.links} == {
            link["url"] for link in dict_event["links"]
        }
        assert {attach.filename for attach in db_event.attachments} == {
            attachment["filename"] for attachment in dict_event["attachments"]
        }


def test_delete_process(webclient, dummy_process, session):
    # Ensure process exists
    res = webclient.get(f"/processes/{dummy_process.id}")
    assert res.status_code == 200, res.text

    data = res.json()

    assert data["id"] == dummy_process.id

    # Delete and check it's not in DB anymore
    res = webclient.delete(f"/processes/{dummy_process.id}")
    assert res.status_code == 200, res.text

    process = session.get(Process, dummy_process.id)
    assert not process
