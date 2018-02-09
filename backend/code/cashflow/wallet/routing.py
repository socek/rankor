def wallet_routing(routing):
    routing.add('cashflow.wallet.views.WalletListView', 'wallet_list',
                '/wallets')
