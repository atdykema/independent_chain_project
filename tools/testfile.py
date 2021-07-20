from src.command_line import touch_wallet, touch_address, get_wallets, get_addresses


def test_attributes(wallets):
    touch_wallet(wallets, 'd0')
    touch_wallet(wallets, 'd1')
    touch_wallet(wallets, 'test')
    touch_address(wallets, 'd1')
    touch_address(wallets, 'd0')
    print("--Wallets--")
    get_wallets(wallets)
    print("--Addresses--")
    get_addresses(wallets)