"""
docs.pisz.pl - a project on documenting code, translating documentation and writing coding tutorials in Polish and English.
"""

__version__ = "0.1.0"


class InvalidKindError(Exception):
    """Raised if the kind is invalid."""
    pass


def get_random_tips(kind=None):
    """
    Return a list of random topics as strings.

    :param kind: Optional "kind" of topics.
    :type kind: list[str] or None
    :raise docspiszpl.InvalidKindError: If the kind is invalid.
    :return: The topics list.
    :rtype: list[str]
    """
    return ["ux", "translation", "writing"]
