from cashflow.application.drivers import ReadDriver
from cashflow.application.drivers import WriteDriver
from cashflow.wallet.models import Wallet


class WalletReadDriver(ReadDriver):
    model = Wallet


class WalletWriteDriver(WriteDriver):
    model = Wallet
