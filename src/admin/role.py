
from src.admin.base import SecureModelView


class SecureModelView(SecureModelView):
    can_edit = True
    can_delete = True
    can_create = True
    create_modal = True
    edit_modal = True
    can_export = True