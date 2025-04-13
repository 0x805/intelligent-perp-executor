from google.protobuf.any_pb2 import Any
from cosmospy_protobuf.utils import Message
import json

def MsgSend(from_address, to_address, amount, denom):
    msg_dict = {
        "@type": "/cosmos.bank.v1beta1.MsgSend",
        "from_address": from_address,
        "to_address": to_address,
        "amount": [{
            "denom": denom,
            "amount": str(amount)
        }]
    }

    any_msg = Any()
    any_msg.type_url = msg_dict["@type"]
    any_msg.value = json.dumps(msg_dict).encode("utf-8")

    return Message(
        type_url=any_msg.type_url,
        value=any_msg.value
    )
