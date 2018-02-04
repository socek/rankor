from sapp.plugins.sqlalchemy.driver import ReadDriver
from sapp.plugins.sqlalchemy.driver import WriteDriver

from cashflow.wallet.models import Wallet


class WalletReadDriver(ReadDriver):
    model = Wallet


class WalletWriteDriver(WriteDriver):
    model = Wallet
