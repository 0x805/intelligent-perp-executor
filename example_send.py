
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "libs"))

from wallet import get_dydx_wallet
from signer import build_signed_tx
from broadcast import broadcast_tx
import requests
import json

# ===== CONFIG =====
MNEMONIC = "point keen rare above tumble tobacco comfort pact timber bubble laptop obey symptom critic fame author iron ship frog involve bullet match cushion time"
TO_ADDRESS = "dydx1d8a5lmffn0p55ejyeu3zk0h2k7ugk7jplrpgtf"
DENOM = "adydx"
AMOUNT = 1000000000000000000  # 1 DYDX
RPC_URL = "https://rpc.dydx.bronbro.io"



# ===== Derive Wallet =====
wallet = get_dydx_wallet(MNEMONIC)
from_address = wallet["address"]
print("🔐 Address:", from_address)

# ===== Fetch Account Info =====
acct_url = f"{RPC_URL}/cosmos/auth/v1beta1/accounts/{from_address}"
res = requests.get(acct_url)
if res.status_code != 200:
    raise Exception("❌ Account not found or RPC issue.")

acct_data = res.json()["account"]["base_account"]
account_number = int(acct_data["account_number"])
sequence = int(acct_data["sequence"])
print("✅ Account Number:", account_number, "| Sequence:", sequence)

# ===== Build and Sign Transaction =====
tx = build_signed_tx(
    from_address,
    TO_ADDRESS,
    AMOUNT,
    DENOM,
    account_number,
    sequence,
    wallet["public_key"],
    wallet["private_key"]
)

# ===== Broadcast to Network =====
result = broadcast_tx(tx.SerializeToString(), RPC_URL)
print("📡 TX Result:", json.dumps(result, indent=2))
