
import requests
import json

def broadcast_tx(tx_bytes: bytes, rpc_url: str):
    broadcast_url = f"{rpc_url}/cosmos/tx/v1beta1/txs"
    headers = {"Content-Type": "application/json"}
    payload = {
        "tx_bytes": tx_bytes.hex(),
        "mode": "BROADCAST_MODE_SYNC"
    }
    res = requests.post(broadcast_url, headers=headers, data=json.dumps(payload))
    return res.json()
