from uuid import uuid4

from pytest import fixture
from pytest import raises
from sqlalchemy.orm.exc import NoResultFound

from rankor.application.testing import IntegrationFixture
from rankor.auth.drivers import UserQuery


class TestQuery(IntegrationFixture):
    @fixture
    def driver(self, app):
        """
        In order to test base driver, we need to use any driver that inherits
        from normal Query class. UserQuery is good enought.
        """
        return UserQuery(app.dbsession)

    def test_get_by_id_when_not_exists(self, driver):
        """
        .get_by_id should reaise NoResultFound when object with provided id
        does not exists
        """
        with raises(NoResultFound):
            driver.get_by_id(uuid4())

    def test_get_by_id_when_exists(self, driver, user):
        """
        .get_by_id should return proper object, if object with provided id
        exists.
        """
        assert driver.get_by_id(user.id).id == user.id
