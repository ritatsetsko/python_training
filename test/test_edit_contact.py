from model.contact import Contact

def test_edit_first_contact(app):
    if app.contact.count()==0:
        app.contact.create_contact(Contact(firstname="TestFirstname", lastname="TestLastname", mobile="89178765212", email="test@test.ru"))
    app.contact.edit_first_contact(Contact(firstname="Firstname1", lastname="Lastname2", mobile="89178765211", email="test3@test.ru"))
