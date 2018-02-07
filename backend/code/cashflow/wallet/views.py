from sapp.decorators import WithContext
from sapp.plugins.pyramid.controller import RestfulController

from cashflow import app
from cashflow.wallet.drivers import WalletReadDriver
from cashflow.wallet.schemas import WalletSchema


class WalletListView(RestfulController):

    @WithContext(app, args=['dbsession'])
    def get(self, dbsession):
        schema = WalletSchema()
        driver = WalletReadDriver(dbsession)
        wallets = driver.list_all()
        data = schema.dump(wallets, many=True).data

        return dict(elements=data)
