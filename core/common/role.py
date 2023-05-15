from django_enumfield import enum


class Role(enum.Enum):
    """
    Role choices for user profile
    """

    CLIENT = 1
    EMPLOYEE = 2
    MARKETING = 3

    __labels__ = {
        CLIENT: "Client",
        EMPLOYEE: "Employee",
        MARKETING: "Marketing",
    }

    __default__ = CLIENT

    @classmethod
    def get_value(cls, member):
        return cls.__labels__[member]
