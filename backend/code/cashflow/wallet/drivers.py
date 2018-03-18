from rankor.application.drivers import ReadDriver
from rankor.application.drivers import WriteDriver
from rankor.wallet.models import Wallet
from rankor.auth.models import User


class WalletReadDriver(ReadDriver):
    model = Wallet

    def _list_all(self):
        return self.query()

    def _list_for_user(self, user=None, user_id=None, user_uuid=None):
        count = sum(not not element for element in [user, user_id, user_uuid])
        if count != 1:
            raise ValueError('you can only use one argument at a time')

        query = self._list_all().join(User)

        if user:
            return query.filter(self.model.user == user)

        if user_id:
            return query.filter(User.id == user_id)

        return query.filter(User.uuid == user_uuid)

    def list_for_user(self, user=None, user_id=None, user_uuid=None):
        return self._list_for_user(user, user_id, user_uuid).all()


class WalletWriteDriver(WriteDriver):
    model = Wallet
