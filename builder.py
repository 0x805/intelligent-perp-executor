import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "libs"))
from cosmospy_protobuf.tx import SignerInfo, AuthInfo, Fee, TxBody, TxRaw
from cosmospy_protobuf.utils import Message

class TransactionBuilder:
    def __init__(self, account_number, sequence, chain_id, gas, fee, memo, public_key, private_key):
        self.account_number = account_number
        self.sequence = sequence
        self.chain_id = chain_id
        self.gas = gas
        self.fee = fee
        self.memo = memo
        self.public_key = public_key
        self.private_key = private_key
        self.msgs = []

    def add_msg(self, msg: Message):
        self.msgs.append(msg)

    def build_and_sign(self):
        tx_body = TxBody(messages=self.msgs, memo=self.memo)
        signer_info = SignerInfo(public_key=self.public_key, sequence=self.sequence)
        fee_info = Fee(gas=self.gas, amount=self.fee)
        auth_info = AuthInfo(signer_info, fee_info)
        return TxRaw.build_and_sign_tx(
            tx_body, auth_info, self.account_number, self.chain_id, self.private_key
        )
