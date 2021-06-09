import src.wallet as w
import src.coinbase as cb
import src.block as b
import src.command_line as cl


def main():
    # create coinbase
    coinbase = cb.Coinbase()
    print(f"{coinbase.reward_available}" + " " + f"{coinbase.genesis_date}")

    # create genesis block
    genesis_block = b.Block(0x0000000000000000000000000000000000000000000000000000000000000000)
    print(f"{genesis_block.prev_hash}" + " " + f"{genesis_block.txs}")

    # create series of wallets
    # m.wallets.append(cl.touch_wallet())
    # m.wallets.append(cl.touch_wallet())
    # m.wallets.append(cl.touch_wallet())
    # m.wallets.append(cl.touch_wallet())

    cl.start_command_line()




if __name__ == "__main__":
    main()
