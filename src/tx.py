
# TODO: get gas limit

# TODO: get nonce

class Tx:
    def __init__(self, sending_address, receiving_address, unit_exchanged):
        # self.nonce = function that searches blockchain for number of transactions per address by sending_address
        # self.gas_limit = gas_limit
        self.sending_address = sending_address
        self.receiving_address = receiving_address
        self.unit_exchanged = unit_exchanged
        # v,r,s stuff
