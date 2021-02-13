# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Ivan", middlename="Vasilyevich", lastname="Ryurikovich", nickname="Grozny", title="Tsar", company="Russia", address="Palaty"))
    app.session.logout()
