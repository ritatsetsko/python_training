from model.contact import Contact

def test_edit_first_contact(app):
    app.session.login( username = "admin", password = "secret")
    app.contact.edit_first_contact(Contact(firstname="Firstname1", lastname="Lastname2", mobile="89178765211", email="test3@test.ru"))
    app.session.logout()