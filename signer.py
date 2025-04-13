
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "libs"))

from builder import TransactionBuilder
from cosmospy_protobuf.msgs import MsgSend

def build_signed_tx(from_address, to_address, amount, denom, account_number, sequence, pub_key, priv_key, chain_id="dydx-mainnet-1"):
    builder = TransactionBuilder(
        account_number=account_number,
        sequence=sequence,
        chain_id=chain_id,
        gas=200000,
        fee=50000000000000000,
        memo="",
        public_key=pub_key,
        private_key=priv_key
    )
    
    builder.add_msg(
        MsgSend(
            from_address=from_address,
            to_address=to_address,
            amount=[{"denom": denom, "amount": str(amount)}]
        )
    )
    
    return builder.build_and_sign()
