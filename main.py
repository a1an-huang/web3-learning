from web3 import Web3
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))

print(f'Connection: {w3.isConnected()}')


# for diff coins
def wei_to_coin(wei_val, coin):
    return w3.fromWei(wei_val, coin)

# coin_addr = input("ETH Address: ")
# coin = input("Type of Coin: ")


coin_addr = '0x4932c0A4C34e4B3703929950db0920B16eC41a1c'
coin = 'ether'
eth_in_wei = w3.eth.get_balance(coin_addr)
eth = wei_to_coin(eth_in_wei, coin)

print(f'Balance: {eth}')
