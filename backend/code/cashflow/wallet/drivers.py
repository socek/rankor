from sapp.plugins.sqlalchemy.driver import ReadDriver
from sapp.plugins.sqlalchemy.driver import WriteDriver

from cashflow.wallet.models import Wallet


class WalletReadDriver(ReadDriver):
    model = Wallet

    def get_by_uuid(self, uuid):
        return self.query().filter(self.model.uuid == uuid).one()


class WalletWriteDriver(WriteDriver):
    model = Wallet
