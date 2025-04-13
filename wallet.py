from bip_utils import (
    Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes,
    Bech32Encoder, Sha256, Ripemd160
)

def get_dydx_wallet(mnemonic: str):
    seed_bytes = Bip39SeedGenerator(mnemonic).Generate()
    bip44_ctx = Bip44.FromSeed(seed_bytes, Bip44Coins.COSMOS)
    acct = bip44_ctx.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0)

    pub_key = acct.PublicKey().RawCompressed().ToBytes()
    priv_key = acct.PrivateKey().Raw().ToBytes()

    # ✅ Manual HASH160
    sha256_hash = Sha256.QuickDigest(pub_key)
    hash160 = Ripemd160.QuickDigest(sha256_hash)

    address = Bech32Encoder.Encode("dydx", hash160)

    return {
        "address": address,
        "public_key": pub_key,
        "private_key": priv_key
    }
