from django_enumfield import enum

class Size(enum.Enum):
    """ 
    Sizes choices for coffee
    """

    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    EXTRA_LARGE = 4

    __labels__ = {
        SMALL: 'Small',
        MEDIUM: 'Medium',
        LARGE: 'Large',
        EXTRA_LARGE: 'Extra Large',
    }

    __default__ = SMALL

    @classmethod
    def get_value(cls, member):
        return cls.__labels__[member]
