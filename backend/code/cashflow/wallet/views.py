from sapp.decorators import WithContext
from sapp.plugins.pyramid.controller import RestfulController

from cashflow import app
from cashflow.auth.drivers import UserReadDriver
from cashflow.wallet.drivers import WalletReadDriver
from cashflow.wallet.drivers import WalletWriteDriver
from cashflow.wallet.schemas import CreateWalletSchema
from cashflow.wallet.schemas import WalletSchema


class WalletListView(RestfulController):
    @WithContext(app, args=['dbsession'])
    def get(self, dbsession):
        schema = WalletSchema()
        driver = WalletReadDriver(dbsession)
        wallets = driver.list_all()
        data = schema.dump(wallets, many=True).data

        return dict(elements=data)


class WalletCreateView(RestfulController):
    @WithContext(app, args=['dbsession'])
    def post(self, dbsession):
        schema = CreateWalletSchema()
        wallet_wd = WalletWriteDriver(dbsession)
        user_rd = UserReadDriver(dbsession)

        data = schema.load(self.request.json).data

        user_uuid = data.pop('user_uuid')
        data['user_id'] = user_rd.get_id_by_uuid(user_uuid)

        wallet = wallet_wd.create(**data)

        return {
            'uuid': wallet.uuid,
        }
