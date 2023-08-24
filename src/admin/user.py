from src.admin.base import SecureModelView


class UserView(SecureModelView):
    can_create = False
    can_delete = False
    can_edit = False
    can_export = True
    column_exclude_list = ["_password"]
    column_labels = {"username":"სახელი", "birthday":"დაბადების თარიღი", "email": "ელ-ფოსტა", "gender":"სქესი", "confirmed": "დადასტურებულია"}
    column_searchable_list = ["username"]
    column_filter = ["confirmed"]