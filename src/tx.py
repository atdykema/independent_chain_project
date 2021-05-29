import main as m


def check_sending_utxo(wallet):
    if not wallet.get_utxos():
        return False



class Tx:
    def __init__(self, sending_addr, receiving_addr, unit_exchanged):
        self.sending_wallet = sending_addr
        self.receiving_addr = receiving_addr
        self.unit_exchanged = unit_exchanged
