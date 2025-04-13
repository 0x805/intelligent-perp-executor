
from cosmospy_protobuf.utils import Message
from cosmospy_protobuf.crypto import PubKey

class SignerInfo:
    def __init__(self, public_key, sequence):
        self.public_key = public_key
        self.sequence = sequence

class Fee:
    def __init__(self, gas, amount):
        self.gas_limit = gas
        self.amount = [{"denom": "adydx", "amount": str(amount)}]

class AuthInfo:
    def __init__(self, signer_info, fee_info):
        self.signer_infos = [signer_info]
        self.fee = fee_info

class TxBody:
    def __init__(self, messages, memo=""):
        self.messages = messages
        self.memo = memo

class TxRaw:
    @staticmethod
    def build_and_sign_tx(tx_body, auth_info, account_number, chain_id, private_key):
        from cosmospy import Transaction
        tx = Transaction(
            privkey=private_key,
            account_num=account_number,
            sequence=auth_info.signer_infos[0].sequence,
            fee=auth_info.fee.amount[0]["amount"],
            gas=auth_info.fee.gas_limit,
            memo=tx_body.memo,
            chain_id=chain_id,
        )
        tx.set_msg(tx_body.messages[0].value)
        tx.set_pubkey(PubKey(tx.pubkey).to_any())  # ✅ this line too
        tx.sign()
        return tx.get_tx_raw()
