from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count()==0:
        app.contact.create_contact(Contact(firstname="TestFirstname", lastname="TestLastname", mobile="89178765212", email="test@test.ru"))
    old_contacts=app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts=app.contact.get_contact_list()
    assert len(old_contacts)-1==len(new_contacts)