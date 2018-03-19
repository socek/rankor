from uuid import UUID

from rankor.application.model import uuid_default


def test_uuid_default():
    """
    Validate if uuid is relly an uuid.
    """
    assert UUID(uuid_default())
