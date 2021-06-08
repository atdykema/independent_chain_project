import src.coinbase as cb
import src.block as b
import src.wallet as w
import src.command_line as cl
import src.mining as mine
import multiprocessing as mp


# initialize wallet list
wallets = []

# initiate genesis block
genesis_block = b.Block(0x0000000000000000000000000000000000000000000000000000000000000000)

# at this point, initiating a genesis block seems to be the best way to start the
# chain and have the linked list work
most_recent_block = genesis_block

# initiate coinbase
coinbase = cb.Coinbase()

# initiate mining
mining = mp.Process(target=mine.start_mining)


def main():
    # start command line
    status = cl.start_command_line()


if __name__ == "__main__":
    main()
