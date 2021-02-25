from model.group import Group


def check_group_count(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))


def test_edit_group_name(app):
    check_group_count(app)
    app.group.edit_first_group(Group(name="Modified group"))


def test_edit_group_header(app):
    check_group_count(app)
    app.group.edit_first_group(Group(header="new GROUP header"))
