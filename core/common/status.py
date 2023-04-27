from django_enumfield import enum

class Status(enum.Enum):
    """
    Status choices for user profile
    """

    ACTIVE = 1
    INACTIVE = 2
    BANNED = 3

    __labels__ = {
        ACTIVE: 'Active',
        INACTIVE: 'Inactive',
        BANNED: 'Banned',
    }

    __default__ = ACTIVE

    @classmethod
    def get_value(cls, member):
        return cls.__labels__[member]