from ..models import UserProfile
from ..common import Role
from issue_tracker.utils import create_issue


def get_users_from_filters(filters):
    """example of filter
    "filters": {
        "property1": null,
        "property2": null
    },
    """
    if filters is None:
        # if filters is None we return all users exept admins and employees
        try:
            return UserProfile.objects.filter(
                is_admin=False, role=Role.CLIENT or Role.MARKETING
            )
        except Exception as e:
            create_issue(
                title="Error al obtener usuarios",
                description="Error al obtener usuarios",
                exception=e,
            )
            raise e
    return UserProfile.objects.filter(**filters)
