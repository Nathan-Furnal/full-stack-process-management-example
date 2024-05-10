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
