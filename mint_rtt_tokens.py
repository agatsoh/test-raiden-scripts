import time
import pprint
import click
import json
from web3 import Web3, HTTPProvider

w3 = Web3(HTTPProvider('http://127.0.0.1:8545'))
def wait_for_receipt(w3, tx_hash, poll_interval):
    while True:
        tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
        if tx_receipt:
            return tx_receipt
        time.sleep(poll_interval)


def contract_abi(file):
    with open(file, 'r') as f:
        return json.load(f)


def get_contract(rtt_token_address):
    rtt_token_address = w3.toChecksumAddress(rtt_token_address)
    rtt_token_abi = contract_abi('rtt_token.json')
    return w3.eth.contract(address=rtt_token_address, abi=rtt_token_abi)


def get_account():
    addresses = w3.eth.accounts
    if not addresses:
        raise RuntimeError("No Accounts found in the Ethereum Client")

    for i, acc in enumerate(addresses):
        print(i, "\t", acc)
    should_prompt = True

    print("Please unlock your account in the ethereum client to continue")
    while should_prompt:
        idx = click.prompt('Select one of them by index to continue', type=int)

        if 0 <= idx < len(addresses):
            should_prompt = False
        else:
            print('\nError: Provided index "{}" is out of bounds\n'.format(idx))

    return addresses[idx]


@click.command(help="Mint tokens from the RTT smart contract")
@click.option("--token-address", help="Address to which tokens need to be transferred",
              type=str, prompt=True)
@click.option("--amount", help="Amount of tokens to mint", type=int, prompt=True)
def main(token_address, amount):
    msg_sender = get_account()
    rtt_token = get_contract(w3.toChecksumAddress(token_address))
    tx_hash = rtt_token.functions.mint(amount).transact({"from": msg_sender})
    receipt = wait_for_receipt(w3, tx_hash, 1)
    print("Transaction receipt mined: \n")
    pprint.pprint(dict(receipt))
    print("Balance of {} is : {}".format(msg_sender, rtt_token.functions.balanceOf(msg_sender).call()))


if __name__ == '__main__':
    # "0x0f114a1e9db192502e7856309cc899952b3db1ed" rtt token address
    main()