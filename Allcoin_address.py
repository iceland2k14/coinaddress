# -*- coding: utf-8 -*-
"""

@author: iceland
"""

import bit
import hashlib
#import bitcoinlib

from bitcoinlib.encoding import pubkeyhash_to_addr_bech32, addr_bech32_to_pubkeyhash, change_base
from eth_hash.auto import keccak

#==============================================================================

def ETH_Address(un_pubk_bytes):
    return '0x' + keccak(un_pubk_bytes[1:])[-20:].hex()

def HASH160(pubk_bytes):
    return hashlib.new('ripemd160', hashlib.sha256(pubk_bytes).digest() ).digest()

def hash160_to_addrbech32(hash160):
 	return pubkeyhash_to_addr_bech32(hash160, prefix='bc', witver=0, separator='1')
 
    

hexkey = 'e4d784ac'
pk = bit.Key.from_hex(hexkey)

upub = pk._pk.public_key.format(compressed=False)
cpub = pk._pk.public_key.format(compressed=True)
crmd = HASH160(cpub)
urmd = HASH160(upub)

print('=========================== Public Keys ==============================')
print('compressed      :', cpub.hex())
print('uncompressed    :', upub.hex())
print('=========================== Hash 160 =================================')
print('compressed      :', crmd.hex())
print('uncompressed    :', urmd.hex())
print('=========================== Address ==================================')
print('BTC     (compressed)     :', bit.base58.b58encode_check(b'\x00' + crmd))
print('BTC     (uncompressed)   :', bit.base58.b58encode_check(b'\x00' + urmd))
print('BTC     (P2SH)           :', bit.base58.b58encode_check(b'\x05' + HASH160(b'\x00\x14' + crmd)))
print('BTC     (bech32 p2wpkh)  :', pubkeyhash_to_addr_bech32(crmd, prefix='bc', witver=0, separator='1'))

print('LTC     (compressed)     :', bit.base58.b58encode_check(b'\x30' + crmd))
print('LTC     (uncompressed)   :', bit.base58.b58encode_check(b'\x30' + urmd))
print('LTC     (P2SH)           :', bit.base58.b58encode_check(b'\x32' + HASH160(b'\x00\x14' + crmd)))
print('LTC     (bech32 p2wpkh)  :', pubkeyhash_to_addr_bech32(crmd, prefix='ltc', witver=0, separator='1'))

print('BTG     (compressed)     :', bit.base58.b58encode_check(b'\x26' + crmd))
print('BTG     (uncompressed)   :', bit.base58.b58encode_check(b'\x26' + urmd))
print('BTG     (P2SH)           :', bit.base58.b58encode_check(b'\x17' + HASH160(b'\x00\x14' + crmd)))
print('BTG     (bech32 p2wpkh)  :', pubkeyhash_to_addr_bech32(crmd, prefix='btg', witver=0, separator='1'))

print('BSV     (compressed)     :', bit.base58.b58encode_check(b'\x00' + crmd))
print('BSV     (uncompressed)   :', bit.base58.b58encode_check(b'\x00' + urmd))

print('BTCZ    (compressed)     :', bit.base58.b58encode_check(b'\x1c\xb8' + crmd))
print('BTCZ    (uncompressed)   :', bit.base58.b58encode_check(b'\x1c\xb8' + urmd))

print('TENT    (compressed)     :', bit.base58.b58encode_check(b'\x1c\x28' + crmd))
print('TENT    (uncompressed)   :', bit.base58.b58encode_check(b'\x1c\x28' + urmd))

print('DOGE    (compressed)     :', bit.base58.b58encode_check(b'\x1e' + crmd))
print('DOGE    (uncompressed)   :', bit.base58.b58encode_check(b'\x1e' + urmd))

print('DASH    (compressed)     :', bit.base58.b58encode_check(b'\x4c' + crmd))
print('DASH    (uncompressed)   :', bit.base58.b58encode_check(b'\x4c' + urmd))

print('SMART   (compressed)     :', bit.base58.b58encode_check(b'\x3f' + crmd))
print('SMART   (uncompressed)   :', bit.base58.b58encode_check(b'\x3f' + urmd))

print('ZCASH   (compressed)     :', bit.base58.b58encode_check(b'\x1c\xb8' + crmd))
print('ZCASH   (uncompressed)   :', bit.base58.b58encode_check(b'\x1c\xb8' + urmd))

print('ZCL     (compressed)     :', bit.base58.b58encode_check(b'\x1c\xb8' + crmd))
print('ZCL     (uncompressed)   :', bit.base58.b58encode_check(b'\x1c\xb8' + urmd))

print('ZERO    (compressed)     :', bit.base58.b58encode_check(b'\x1c\xb8' + crmd))
print('ZERO    (uncompressed)   :', bit.base58.b58encode_check(b'\x1c\xb8' + urmd))

print('ZEN     (compressed)     :', bit.base58.b58encode_check(b'\x20\x89' + crmd))
print('ZEN     (uncompressed)   :', bit.base58.b58encode_check(b'\x20\x89' + urmd))

print('ZEIT    (compressed)     :', bit.base58.b58encode_check(b'\x33' + crmd))
print('ZEIT    (uncompressed)   :', bit.base58.b58encode_check(b'\x33' + urmd))

print('Ethereum                 :', ETH_Address(upub))

#print('{0: <8}{1: >18}{2}{3}'.format('BTC','(compressed)','  : ', bit.base58.b58encode_check(b'\x00' + crmd)))
# =============================================================================
# print('BTC (compressed)     :',bitcoinlib.keys.Address(cpub.hex(),encoding='base58').address)
# print('BTC (uncompressed)   :',bitcoinlib.keys.Address(upub.hex(),encoding='base58').address)
# print('BTC (P2SH)           :',bitcoinlib.keys.Address(cpub.hex(),encoding='base58',witness_type='p2sh-segwit').address)
# print('BTC (bech32 p2wpkh)  :',bitcoinlib.keys.Address(cpub.hex(),encoding='bech32',script_type='p2wpkh').address)
# print('BTC (bech32 p2wsh)   :',bitcoinlib.keys.Address(cpub.hex(),encoding='bech32',script_type='p2wsh').address)
# print('LTC (compressed)     :',bitcoinlib.keys.Address(cpub.hex(),encoding='base58', network='litecoin').address)
# print('LTC (uncompressed)   :',bitcoinlib.keys.Address(upub.hex(),encoding='base58', network='litecoin').address)
# print('LTC (P2SH)           :',bitcoinlib.keys.Address(cpub.hex(),encoding='base58', network='litecoin',witness_type='p2sh-segwit').address)
# print('LTC (bech32)         :',bitcoinlib.keys.Address(cpub.hex(),encoding='bech32', network='litecoin').address)
# print('DOGE (compressed)    :',bitcoinlib.keys.Address(cpub.hex(),encoding='base58', network='dogecoin').address)
# print('DOGE (uncompressed)  :',bitcoinlib.keys.Address(upub.hex(),encoding='base58', network='dogecoin').address)
# =============================================================================
