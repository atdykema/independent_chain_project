import src.wallet as w
import src.coinbase as cb
import src.block as b
import src.main as m
import src.command_line as cl



def main():
    # create coinbase
    coinbase = cb.Coinbase()
    print(f"{coinbase.get_reward_available()}" + " " + f"{coinbase.get_genesis_date()}")

    # create genesis block
    genesis_block = b.Block(123, 123)
    print(f"{genesis_block.get_prev_hash()}" + " " + f"{genesis_block.get_txs()}")

    # create series of wallets
    m.wallets.append(cl.touch_wallet())
    m.wallets.append(cl.touch_wallet())
    m.wallets.append(cl.touch_wallet())
    m.wallets.append(cl.touch_wallet())




if __name__ == "__main__":
    main()
