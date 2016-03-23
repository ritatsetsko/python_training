# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application

@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Firstname", lastname="Lastname", mobile="89178765212", email="test@test.ru"))
    app.logout()


