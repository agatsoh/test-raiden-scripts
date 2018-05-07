import time
import pprint
from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract


def wait_for_receipt(w3, tx_hash, poll_interval):
    while True:
        tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
        if tx_receipt:
            return tx_receipt
        time.sleep(poll_interval)


w3 = Web3(HTTPProvider('http://127.0.0.1:8545'))
rtt_token_address = w3.toChecksumAddress("0x0f114a1e9db192502e7856309cc899952b3db1ed")
rtt_token_abi = [{"constant": True,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":False,"type":"function"},{"constant":False,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":False,"type":"function"},{"constant":False,"inputs":[],"name":"mint","outputs":[],"payable":False,"type":"function"},{"constant":True,"inputs":[],"name":"totalSupply","outputs":[{"name":"supply","type":"uint256"}],"payable":False,"type":"function"},{"constant":False,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":False,"type":"function"},{"constant":True,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":False,"type":"function"},{"constant":True,"inputs":[],"name":"version","outputs":[{"name":"","type":"string"}],"payable":False,"type":"function"},{"constant":True,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":False,"type":"function"},{"constant":True,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":False,"type":"function"},{"constant":False,"inputs":[{"name":"amount","type":"uint256"}],"name":"mint","outputs":[],"payable":False,"type":"function"},{"constant":False,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":False,"type":"function"},{"constant":False,"inputs":[{"name":"amount","type":"uint256"},{"name":"target","type":"address"}],"name":"mintFor","outputs":[],"payable":False,"type":"function"},{"constant":False,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"},{"name":"_extraData","type":"bytes"}],"name":"approveAndCall","outputs":[{"name":"success","type":"bool"}],"payable":False,"type":"function"},{"constant":True,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":False,"type":"function"},{"inputs":[{"name":"_tokenName","type":"string"},{"name":"_tokenSymbol","type":"string"}],"payable":False,"type":"constructor"},{"payable":False,"type":"fallback"},{"anonymous":False,"inputs":[{"indexed":True,"name":"_from","type":"address"},{"indexed":True,"name":"_to","type":"address"},{"indexed":False,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"_owner","type":"address"},{"indexed":True,"name":"_spender","type":"address"},{"indexed": False,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]
rtt_token = w3.eth.contract(address=rtt_token_address, abi=rtt_token_abi)

account = w3.eth.accounts[0]
amount = input("Please enter the amount: ")
print("Amount is :", amount)
amount = int(amount)
if type(amount) == int:
    print("Calling the mint function")
    tx_hash = rtt_token.functions.mint(amount).transact({"from": account})
    receipt = wait_for_receipt(w3, tx_hash, 1)
    print("Transaction receipt mined: \n")
    pprint.pprint(dict(receipt))
    print("Balance of {} is : {}".format(account, rtt_token.functions.balanceOf(account).call()))
else:
    "Please enter the amount as integers"
