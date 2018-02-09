from sapp.decorators import WithContext
from sapp.plugins.pyramid.controller import RestfulController

from cashflow import app
from cashflow.auth.view_mixins import AuthMixin
from cashflow.wallet.drivers import WalletReadDriver
from cashflow.wallet.drivers import WalletWriteDriver
from cashflow.wallet.schemas import CreateWalletSchema
from cashflow.wallet.schemas import WalletSchema


class WalletListView(RestfulController, AuthMixin):
    permission = 'edit'

    @WithContext(app, args=['dbsession'])
    def get(self, dbsession):
        schema = WalletSchema()
        driver = WalletReadDriver(dbsession)
        wallets = driver.list_all()
        data = schema.dump(wallets, many=True).data

        return dict(elements=data)

    @WithContext(app, args=['dbsession'])
    def post(self, dbsession):
        schema = CreateWalletSchema()
        wallet_wd = WalletWriteDriver(dbsession)

        data = schema.load(self.request.json).data
        data['user_id'] = self.get_user().id

        wallet = wallet_wd.create(**data)

        return {
            'uuid': wallet.uuid,
        }
