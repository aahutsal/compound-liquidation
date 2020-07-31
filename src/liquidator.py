from web3 import Web3
import os
from dotenv import load_dotenv
# OR, explicitly providing path to '.env'
from pathlib import Path  # python3 only
env_path = Path('.') / '.env.local'
load_dotenv(dotenv_path=env_path, verbose=True)


w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
account = os.getenv('MY_WALLET_ADDRESS')
pk = os.getenv('MY_WALLET_PK')



