# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create_contact(Contact(firstname="Firstname", lastname="Lastname", mobile="89178765212", email="test@test.ru"))



