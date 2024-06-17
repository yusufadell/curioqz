import pytest

from curioqz.users.models import User
from curioqz.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    """

    :param settings: 
    :param tmpdir: 

    """
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user(db) -> User:
    """

    :param db: 

    """
    return UserFactory()
