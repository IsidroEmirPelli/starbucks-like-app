from .mercado_pago import create_payment
from .filters import get_users_from_filters
from .emails_service import send_email, send_campain_email


class BasePermissionsViewSet:
    def get_permissions(self):
        try:
            return [
                permission()
                for permission in self.permission_classes_by_action[self.action]
            ]
        except KeyError:
            return [permission() for permission in self.permission_classes]
