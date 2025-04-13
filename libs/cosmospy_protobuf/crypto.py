from google.protobuf.any_pb2 import Any
from google.protobuf.message import Message
from google.protobuf import descriptor_pb2

class PubKey:
    def __init__(self, compressed_pubkey: bytes):
        self.type_url = "cosmos.crypto.secp256k1.PubKey"
        self.value = compressed_pubkey

    def to_any(self) -> Any:
        any_msg = Any()
        any_msg.type_url = self.type_url
        any_msg.value = self.value
        return any_msg
