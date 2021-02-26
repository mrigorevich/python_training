from model.contact import Contact


def test_add_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.edit_first(Contact(firstname="Ivan", middlename="Vasilyevich", lastname="Ryurikovich", nickname="Grozny", title="Tsar", company="Russia", address="Palaty", mobile="+71234567", email="tsar@kremlin.ru"))
