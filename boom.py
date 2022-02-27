#boom.py Random Bitcoin&Litecoin Legacy compressed/uncompresses address and Segwit address P2SH.Bitcoin Gold\BitcoinCash\Zcash\Doge\DASH\ETH\ZEN\ZEIT\TENT
# Look for address or HASH160 PUBLIC KEY
#One of the best and most versatile crypto scanner. Looks for 28 different addresses, HASH160 or PUBLICKEY from a txt file. Cloud not have made this without Iceland's original.
#Made by mizogg.co.uk
# Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD
import bit
from bit import *
from bit.format import bytes_to_wif
import hashlib
from bitcoinlib.encoding import pubkeyhash_to_addr_bech32, addr_bech32_to_pubkeyhash, change_base
from eth_hash.auto import keccak
import atexit
from time import time
from datetime import timedelta, datetime
import random

colour_cyan = '\033[36m'
colour_reset = '\033[0;0;39m'
colour_red = '\033[31m'
colour_green='\033[0;32m'
colour_yellow='\033[0;33m'
colour_purple='\033[0;35m'
colour_blue='\033[0;34m'

def seconds_to_str(elapsed=None):
    if elapsed is None:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    else:
        return str(timedelta(seconds=elapsed))


def log(txt, elapsed=None):
    print('\n ' + colour_cyan + '  [TIMING]> [' + seconds_to_str() + '] ----> ' + txt + '\n' + colour_reset)
    if elapsed:
        print("\n " + colour_red + " [TIMING]> Elapsed time ==> " + elapsed + "\n" + colour_reset)


def end_log():
    end = time()
    elapsed = end-start
    log("End Program", seconds_to_str(elapsed))


start = time()
atexit.register(end_log)
log("Start Program")

print(colour_yellow +"boom.py Random Bitcoin&Litecoin Legacy compressed/uncompresses address and Segwit address P2SH.Bitcoin Gold\BitcoinCash\Zcash\Doge\DASH\ETH\ZEN\ZEIT\TENT List loading Good Luck..." + colour_reset)

filename ='btc.txt'

with open(filename) as f:
    line_count = 0
    for line in f:
        line != "\n"
        line_count += 1

with open(filename) as file:
    add = file.read().split()
add = set(add)


print(colour_cyan + "\nboom.py---" + colour_red + "---------mizogg.co.uk---------" + colour_cyan + "---boom.py"  + colour_reset)

def ETH_Address(un_pubk_bytes):
    return '0x' + keccak(un_pubk_bytes[1:])[-20:].hex()

def HASH160(pubk_bytes):
    return hashlib.new('ripemd160', hashlib.sha256(pubk_bytes).digest() ).digest()

def hash160_to_addrbech32(hash160):
 	return pubkeyhash_to_addr_bech32(hash160, prefix='bc', witver=0, separator='1')
    
print(colour_purple + 'Total Addresses\HASH160\PUBLICKEYS Loaded and Checking : ',str (line_count) + colour_reset)
print(colour_yellow+ "Start search... Pick Range"+ colour_reset)
x=int(input("'start range Min 1-115792089237316195423570985008687907852837564279074904382605163141518161494335 -> "))
y=int(input("stop range Max 115792089237316195423570985008687907852837564279074904382605163141518161494336 -> "))

count=0
totalkey=0
total=0  
while True:
    pk = Key.from_int(random.randint(x,y))
    key = Key.from_int(random.randint(x,y))
    upub = pk._pk.public_key.format(compressed=False)
    cpub = pk._pk.public_key.format(compressed=True)
    crmd = HASH160(cpub)
    urmd = HASH160(upub)
    caddr160 =crmd.hex() # Hash 160
    uaddr160 =urmd.hex() # Hash 160
    caddrpub = cpub.hex() #Public Keys
    uaddrpub = upub.hex() #Public Keys
    cwif = bytes_to_wif(key.to_bytes(), compressed=True) # compressed WIF
    uwif = bytes_to_wif(key.to_bytes(), compressed=False) # uncompressed WIF
    privatekey = key.to_hex()
    key1 = Key(uwif)
    caddr = key.address #BTC     (compressed)
    uaddr = key1.address #BTC     (uncompressed)
    paddr = key.segwit_address # BTC     (P2SH)
    bcaddr = pubkeyhash_to_addr_bech32(crmd, prefix='bc', witver=0, separator='1') #BTC     (bech32 p2wpkh)
    lcaddr = bit.base58.b58encode_check(b'\x30' + crmd) #LTC     (compressed)
    luaddr = bit.base58.b58encode_check(b'\x00' + urmd) #LTC     (uncompressed)
    lpaddr = bit.base58.b58encode_check(b'\x32' + HASH160(b'\x00\x14' + crmd)) #LTC     (P2SH)
    lbpaddr = pubkeyhash_to_addr_bech32(crmd, prefix='ltc', witver=0, separator='1') #LTC     (bech32 p2wpkh)
    btgcaddr = bit.base58.b58encode_check(b'\x26' + crmd) #BTG     (compressed)
    btguaddr = bit.base58.b58encode_check(b'\x26' + urmd) #BTG     (uncompressed)
    btgpaddr = bit.base58.b58encode_check(b'\x17' + HASH160(b'\x00\x14' + crmd))  #BTG     (P2SH)
    btgbpaddr = pubkeyhash_to_addr_bech32(crmd, prefix='btg', witver=0, separator='1') #BTG     (bech32 p2wpkh)
    btczcaddr = bit.base58.b58encode_check(b'\x1c\xb8' + crmd) #BTCZ    (compressed) 
    btczuaddr = bit.base58.b58encode_check(b'\x1c\xb8' + urmd) #BTCZ    (uncompressed)
    tentcaddr = bit.base58.b58encode_check(b'\x1c\x28' + crmd) #TENT    (compressed)
    tentuaddr = bit.base58.b58encode_check(b'\x1c\x28' + urmd) #TENT    (uncompressed)
    dogecaddr = bit.base58.b58encode_check(b'\x1e' + crmd) #DOGE    (compressed)
    dogeuaddr = bit.base58.b58encode_check(b'\x1e' + urmd) #DOGE    (uncompressed)
    dashcaddr = bit.base58.b58encode_check(b'\x4c' + crmd) #DASH    (compressed)
    dashuaddr = bit.base58.b58encode_check(b'\x4c' + urmd) #DASH    (uncompressed)
    smartcaddr = bit.base58.b58encode_check(b'\x3f' + crmd) #SMC   (compressed)
    smartuaddr = bit.base58.b58encode_check(b'\x3f' + urmd) #SMC   (uncompressed)
    zcashcaddr = bit.base58.b58encode_check(b'\x1c\xb8' + crmd) #ZCash  ZLC  ZERO (compressed)
    zcashuaddr = bit.base58.b58encode_check(b'\x1c\xb8' + urmd) #ZCash  ZLC  ZERO (uncompressed)
    zencaddr = bit.base58.b58encode_check(b'\x20\x89' + crmd) #ZEN     (compressed)
    zenuaddr = bit.base58.b58encode_check(b'\x20\x89' + urmd) #ZEN     (uncompressed) 
    zeitcaddr = bit.base58.b58encode_check(b'\x33' + crmd) #ZEIT    (compressed)
    zeituaddr = bit.base58.b58encode_check(b'\x20\x89' + urmd) #ZEIT    (uncompressed)
    eaddr = ETH_Address(upub)
    count+=1
    totalkey+=3
    total+=28
    if caddr in add or uaddr in add or paddr in add or bcaddr in add or lcaddr in add or luaddr in add or lpaddr in add or lbpaddr in add or btgcaddr in add or btguaddr in add or btgpaddr in add or btgbpaddr in add or btczcaddr in add or btczuaddr in add or tentcaddr in add or tentuaddr in add or dogecaddr in add or dogeuaddr in add or dashcaddr in add or dashuaddr in add or smartcaddr in add or smartuaddr in add or zcashcaddr in add or zcashuaddr in add or zencaddr in add or zenuaddr in add or zeitcaddr in add or zeituaddr in add or eaddr in add or caddr160 in add or uaddr160 in add or caddrpub in add or uaddrpub in add or crmd in add or urmd in add: 
        print(colour_purple + "Matching Key ==== Found!!!\n PrivateKey: " + colour_reset + privatekey)
        f=open(u"winner.txt","a")
        f.write('\nboom.py made by mizogg.co.uk donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD')
        f.write('\n')
        f.write('\nBitcoin BTC          (compressed)            :' + caddr)
        f.write('\nBitcoin BTC          (uncompressed)          :' + uaddr)
        f.write('\nBitcoin BTC          (P2SH)                  :' + paddr)
        f.write('\nBitcoin BTC          (bech32 p2wpkh)         :' + bcaddr)
        f.write('\nLitecoin LTC         (compressed)            :' + lcaddr)
        f.write('\nLitecoin LTC         (uncompressed)          :' + luaddr)
        f.write('\nLitecoin LTC         (P2SH)                  :' + lpaddr)
        f.write('\nLitecoin LTC         (bech32 p2wpkh)         :' + lbpaddr)
        f.write('\nBitcoin GOLD BTG     (compressed)            :' + btgcaddr)
        f.write('\nBitcoin GOLD BTG     (uncompressed)          :' + btguaddr)
        f.write('\nBitcoin GOLD BTG     (P2SH)                  :' + btgpaddr)
        f.write('\nBitcoin GOLD BTG     (bech32 p2wpkh)         :' + btgbpaddr)
        f.write('\nBITCOINZ BTCZ        (compressed)            :' + btczcaddr)
        f.write('\nBITCOINZ BTCZ        (uncompressed)          :' + btczuaddr)
        f.write('\nTENT coin TENT       (compressed)            :' + tentcaddr)
        f.write('\nTENT coin TENT       (uncompressed)          :' + tentuaddr)
        f.write('\nDoge Coin DOGE       (compressed)            :' + dogecaddr)
        f.write('\nDoge Coin DOGE       (uncompressed)          :' + dogeuaddr)
        f.write('\nDash Coin DASH       (compressed)            :' + dashcaddr)
        f.write('\nDash Coin DASH       (uncompressed)          :' + dashuaddr)
        f.write('\nSmartCoin SMC        (compressed)            :' + smartcaddr)
        f.write('\nSmartCoin SMC        (uncompressed)          :' + smartuaddr)
        f.write('\nZcash ZCASH          (compressed)            :' + zcashcaddr)
        f.write('\nZcash  ZCASH         (uncompressed)          :' + zcashuaddr)
        f.write('\nHorizen ZEN          (compressed)            :' + zencaddr)
        f.write('\nHorizen ZEN          (uncompressed)          :' + zenuaddr)
        f.write('\nZeitcoin ZEIT        (compressed)            :' + zeitcaddr)
        f.write('\nZeitcoin ZEIT        (uncompressed)          :' + zeituaddr)
        f.write('\nEthereum  ETH                                :' + eaddr)
        f.write('\n=========================== Hash 160 =================================')
        f.write('\ncompressed   Hash 160   : '+ caddr160)
        f.write('\nuncompressed  Hash 160  : '+ uaddr160)
        f.write('\n=========================== Private Keys =============================')
        f.write('\nBTC Private Key (compressed WIF)    : ' + cwif)
        f.write('\nBTC  Private Key(Uncompressed WIF)  : ' + uwif)
        f.write('\nPrivate key HEX                     : ' + privatekey)
        f.write('\n=========================== Public Keys ==============================')
        f.write('\ncompressed  Public Key    : ' + caddrpub)
        f.write('\nuncompressed  Public Key  : ' + uaddrpub)
        f.write('\n')
    else:
        print(colour_cyan + "\nboom.py---" + colour_red + "---------mizogg.co.uk---------" + colour_cyan + "---boom.py"  + colour_reset)
        print(colour_green + 'Total Addresses\HASH160\PUBLICKEYS Loaded and Checking : ' + colour_reset, line_count)
        print(colour_cyan + '=========================== Address ==================================' + colour_reset)
        print(colour_yellow + 'Bitcoin BTC          (compressed)            : ' + colour_reset + caddr)
        print(colour_yellow + 'Bitcoin BTC          (uncompressed)          : ' + colour_reset + uaddr)
        print(colour_yellow + 'Bitcoin BTC          (P2SH)                  : ' + colour_reset + paddr)
        print(colour_yellow + 'Bitcoin BTC          (bech32 p2wpkh)         : ' + colour_reset + bcaddr)
        print(colour_yellow + 'Litecoin LTC         (compressed)            : ' + colour_reset + lcaddr)
        print(colour_yellow + 'Litecoin LTC         (uncompressed)          : ' + colour_reset + luaddr)
        print(colour_yellow + 'Litecoin LTC         (P2SH)                  : ' + colour_reset + lpaddr)
        print(colour_yellow + 'Litecoin LTC         (bech32 p2wpkh)         : ' + colour_reset + lbpaddr)
        print(colour_yellow + 'Bitcoin GOLD BTG     (compressed)            : ' + colour_reset + btgcaddr)
        print(colour_yellow + 'Bitcoin GOLD BTG     (uncompressed)          : ' + colour_reset + btguaddr)
        print(colour_yellow + 'Bitcoin GOLD BTG     (P2SH)                  : ' + colour_reset + btgpaddr)
        print(colour_yellow + 'Bitcoin GOLD BTG     (bech32 p2wpkh)         : ' + colour_reset + btgbpaddr)
        print(colour_yellow + 'BITCOINZ BTCZ        (compressed)            : ' + colour_reset + btczcaddr)
        print(colour_yellow + 'BITCOINZ BTCZ        (uncompressed)          : ' + colour_reset + btczuaddr)
        print(colour_yellow + 'TENT coin TENT       (compressed)            : ' + colour_reset + tentcaddr)
        print(colour_yellow + 'TENT coin TENT       (uncompressed)          : ' + colour_reset + tentuaddr)
        print(colour_yellow + 'Doge Coin DOGE       (compressed)            : ' + colour_reset + dogecaddr)
        print(colour_yellow + 'Doge Coin DOGE       (uncompressed)          : ' + colour_reset + dogeuaddr)
        print(colour_yellow + 'Dash Coin DASH       (compressed)            : ' + colour_reset + dashcaddr)
        print(colour_yellow + 'Dash Coin DASH       (uncompressed)          : ' + colour_reset + dashuaddr)
        print(colour_yellow + 'SmartCoin SMC        (compressed)            : ' + colour_reset + smartcaddr)
        print(colour_yellow + 'SmartCoin SMC        (uncompressed)          : ' + colour_reset + smartuaddr)
        print(colour_yellow + 'Zcash ZCASH          (compressed)            : ' + colour_reset + zcashcaddr)
        print(colour_yellow + 'Zcash  ZCASH         (uncompressed)          : ' + colour_reset + zcashuaddr)
        print(colour_yellow + 'Horizen ZEN          (compressed)            : ' + colour_reset + zencaddr)
        print(colour_yellow + 'Horizen ZEN          (uncompressed)          : ' + colour_reset + zenuaddr)
        print(colour_yellow + 'Zeitcoin ZEIT        (compressed)            : ' + colour_reset + zeitcaddr)
        print(colour_yellow + 'Zeitcoin ZEIT        (uncompressed)          : ' + colour_reset + zeituaddr)
        print(colour_yellow + 'Ethereum  ETH                                : ' + colour_reset + eaddr)
        print(colour_cyan + '=========================== Hash 160 =================================' + colour_reset)
        print(colour_yellow + 'compressed   Hash 160   : ' + colour_reset , crmd.hex())
        print(colour_yellow + 'uncompressed  Hash 160  : ' + colour_reset , urmd.hex())
        print(colour_red + '=========================== Private Keys =============================' + colour_reset)
        print(colour_green +'BTC Private Key (compressed WIF)    : ' + colour_reset +cwif)
        print(colour_green +'BTC  Private Key(Uncompressed WIF)  : ' + colour_reset + uwif)
        print(colour_purple +'Private key HEX                     : ' + colour_reset + privatekey)
        print(colour_cyan + '=========================== Public Keys ==============================' + colour_reset)
        print(colour_blue + 'compressed  Public Key    : ' + colour_reset , cpub.hex())
        print(colour_blue + 'uncompressed  Public Key  : ' + colour_reset , upub.hex())
        print ( 'Running Scan : ' + str (count) + '  :  ' + colour_cyan + 'Total Private Keys : ' + str(totalkey) + '  :  ' + colour_red + 'Total Addresses : ' + str (total) + ' : ' + colour_cyan + seconds_to_str() + colour_reset)