

def main():
    # create coinbase
    coinbase = Coinbase()
    print(f"{coinbase.get_reward_available()}" + " " + f"{coinbase.get_genesis_date()}")

    # create genesis block
    genesis_block = Block(123, 123)
    print(f"{genesis_block.get_prev_hash()}" + " " + f"{genesis_block.get_transactions()}")


if __name__ == "__t_main__":
    main()