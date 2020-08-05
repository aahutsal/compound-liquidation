from web3 import Web3
import os
import json
from dotenv import load_dotenv
import requests

import urllib.request
from urllib.request import build_opener
from http.cookiejar import CookieJar

from termcolor import colored

# OR, explicitly providing path to '.env'
from pathlib import Path  # python3 only
env_path = Path('.') / '.env.local'
load_dotenv(dotenv_path=env_path, verbose=True)

def getAccountLiquidity(addy):
    caddress = w3.toChecksumAddress(addy)
    result = contract.functions.getAccountLiquidity(caddress).call()
    if result[0] != 0:
        return "There is an error Whoops"
    elif result[1] != 0:
        return colored("SAFU", 'green')
    elif result[2] != 0:
        return colored("NOT SAFU", 'red', attrs=['bold'])

def token_symbol(tokenname):
        if tokenname == "0x6c8c6b02e7b2be14d4fa6022dfd6d75921d90e4e":
            return "BAT"
        if tokenoname == "0xf5dce57282a584d2746faf1593d3121fcac444dc":
            return "DAI"
        if tokenname == "0x4ddc2d193948926d02f9b1fe9e1daa0718270ed5":
            return "Ξ"
        if tokenname == "0x158079ee67fce2f58472a96584a73c7ab9ac95c1":
            return "REP"
        if tokenname == "0x39aa39c021dfbae8fac545936693ac917d5e7563":
            return "USDC"
        if tokenname == "0xb3319f5d18bc0d84dd1b4825dcde5d5f7266d407":
            return "ZRX"
        if tokenname == "0xc11b1268c1a384e55c48c2391d8d480264a3a7f4":
            return "wBTC"

session = requests.Session()
def get_accounts(filter={"page_size":20}):
    url = "https://api.compound.finance/api/v2/account"
    first_page = session.get(url, params=filter, headers={'Content-type':'application/json','Accept':"application/json"}).json()
    yield first_page
    num_pages = first_page['pagination_summary']['total_pages']

    for page in range(2, num_pages + 1):
        next_page = session.get(url, params=filter.update({'page_number': page})).json()
        yield next_page

filter={'page_number':1, 'max_health[value]': "1.0"}

all = []


for accounts in get_accounts(filter=filter):
    all.append(accounts)


# Prior to starting
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
address = os.getenv('MY_WALLET_ADDRESS')
pk = os.getenv('MY_WALLET_PK')

# Main Net Contract for cETH (the supply process is different for cERC20 tokens)
contractAddress = '0x4ddc2d193948926d02f9b1fe9e1daa0718270ed5';
abi_url = "https://raw.githubusercontent.com/compound-finance/compound-protocol/master/networks/mainnet-abi.json"
abi = requests.get(abi_url)

compoundCEthContract = w3.eth.contract(abi=abi.json()["c{}".format('USDT')], address=Web3.toChecksumAddress(contractAddress))
mintData = {'from': address,
                                             'gasLmimit': w3.toHex(15000),
                                             'gasPrice': w3.toHex(20000000000),
                                             'value': w3.toHex(w3.toWei('1', 'ether'))}
#await compoundCEthContract.functions.mint().call()

with open('./keys.txt', 'r') as myfile:
    keys=json.load(myfile)

if w3.isConnected() == True:
    print("The bot is connected to the ethereum network")
#    time.sleep(1)
else:
    print("The bot can't connect to the eth network")
    quit()

unitroller = keys["unitroller"]

abisite= keys["abi"]
with urllib.request.urlopen(abisite) as url:
    abi = json.loads(url.read())
unitrollerContract = w3.eth.contract(address=unitroller, abi=abi)
# compoundCEthContract.functions.liquidateBorrow().call()

