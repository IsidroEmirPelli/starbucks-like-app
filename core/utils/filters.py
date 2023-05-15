from ..models import UserProfile
from ..common import Role


def get_users_from_filters(filters):
    """example of filter
    "filters": {
        "property1": null,
        "property2": null
    },
    """
    if filters is None:
        # if filters is None we return all users exept admins and employees
        return UserProfile.objects.filter(
            is_admin=False, role=Role.CLIENT or Role.MARKETING
        )
    return UserProfile.objects.filter(**filters)
