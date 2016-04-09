from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count()==0:
        app.contact.create_contact(Contact(firstname="TestFirstname", lastname="TestLastname", mobile="89178765212", email="test@test.ru"))
    app.contact.delete_first_contact()
