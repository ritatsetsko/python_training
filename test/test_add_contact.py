# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact(firstname="Firstname", lastname="Lastname", mobile="89178765212", email="test@test.ru"))
    app.session.logout()


