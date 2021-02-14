from model.group import Group


def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit(Group(name="Modified group", header="new GROUP header", footer="not just a group"))
    app.session.logout()