#boomcpu.py Random Bitcoin&Litecoin Legacy compressed/uncompresses address and Segwit address P2SH.Bitcoin Gold\BitcoinCash\Zcash\Doge\DASH\ETH\ZEN\ZEIT\TENT
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
import random
import threading


print("boomcpu.py Random Bitcoin&Litecoin Legacy compressed/uncompresses address and Segwit address P2SH.Bitcoin Gold\BitcoinCash\Zcash\Doge\DASH\ETH\ZEN\ZEIT\TENT List loading Good Luck..." )

filename ='mixed.txt'

with open(filename) as f:
    line_count = 0
    for line in f:
        line != "\n"
        line_count += 1

with open(filename) as file:
    add = file.read().split()
add = set(add)


print( "\nboomcpu.py---" +  "---------mizogg.co.uk---------" +  "---boomcpu.py"  )

def ETH_Address(un_pubk_bytes):
    return '0x' + keccak(un_pubk_bytes[1:])[-20:].hex()

def HASH160(pubk_bytes):
    return hashlib.new('ripemd160', hashlib.sha256(pubk_bytes).digest() ).digest()

def hash160_to_addrbech32(hash160):
 	return pubkeyhash_to_addr_bech32(hash160, prefix='bc', witver=0, separator='1')
    
print( 'Total Addresses\HASH160\PUBLICKEYS Loaded and Checking : ',str (line_count) )
threadCount = input('Best Run on 1 thread to not block API but you can try more : How many threads to run?:  ')
print("Start search... Pick Range to start (Example Puzzle 64 starting Range 18446744073709551615 ):")
x=int(input("'start range Min 1-115792089237316195423570985008687907852837564279074904382605163141518161494335 -> "))
y=int(input("stop range Max 115792089237316195423570985008687907852837564279074904382605163141518161494336 -> "))
print("Starting search... Please Wait ")
print("==========================================================")

def seek():
    count=0
    totalkey=0
    total=0  
    while True:
        ran= random.randint(x,y)
        pk = Key.from_int(ran)
        key = Key.from_int(ran)
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
        count+=1*int(threadCount)
        totalkey+=3*int(threadCount)
        total+=28*int(threadCount)
        if caddr in add or uaddr in add or paddr in add or bcaddr in add or lcaddr in add or luaddr in add or lpaddr in add or lbpaddr in add or btgcaddr in add or btguaddr in add or btgpaddr in add or btgbpaddr in add or btczcaddr in add or btczuaddr in add or tentcaddr in add or tentuaddr in add or dogecaddr in add or dogeuaddr in add or dashcaddr in add or dashuaddr in add or smartcaddr in add or smartuaddr in add or zcashcaddr in add or zcashuaddr in add or zencaddr in add or zenuaddr in add or zeitcaddr in add or zeituaddr in add or eaddr in add or caddr160 in add or uaddr160 in add or caddrpub in add or uaddrpub in add or crmd in add or urmd in add: 
            print( "Matching Key ==== Found!!!\n PrivateKey: "  + privatekey +'\n')
            print( "\nboomcpu.py---" +  "---------mizogg.co.uk---------" +  "---boomcpu.py"   +'\n')
            print( 'Total Addresses\HASH160\PUBLICKEYS Loaded and Checking : ' , line_count)
            print( '=========================== Address ==================================' )
            print( 'Bitcoin BTC          (compressed)            : '  + caddr)
            print( 'Bitcoin BTC          (uncompressed)          : '  + uaddr)
            print( 'Bitcoin BTC          (P2SH)                  : '  + paddr)
            print( 'Bitcoin BTC          (bech32 p2wpkh)         : '  + bcaddr)
            print( 'Litecoin LTC         (compressed)            : '  + lcaddr)
            print( 'Litecoin LTC         (uncompressed)          : '  + luaddr)
            print( 'Litecoin LTC         (P2SH)                  : '  + lpaddr)
            print( 'Litecoin LTC         (bech32 p2wpkh)         : '  + lbpaddr)
            print( 'Bitcoin GOLD BTG     (compressed)            : '  + btgcaddr)
            print( 'Bitcoin GOLD BTG     (uncompressed)          : '  + btguaddr)
            print( 'Bitcoin GOLD BTG     (P2SH)                  : '  + btgpaddr)
            print( 'Bitcoin GOLD BTG     (bech32 p2wpkh)         : '  + btgbpaddr)
            print( 'BITCOINZ BTCZ        (compressed)            : '  + btczcaddr)
            print( 'BITCOINZ BTCZ        (uncompressed)          : '  + btczuaddr)
            print( 'TENT coin TENT       (compressed)            : '  + tentcaddr)
            print( 'TENT coin TENT       (uncompressed)          : '  + tentuaddr)
            print( 'Doge Coin DOGE       (compressed)            : '  + dogecaddr)
            print( 'Doge Coin DOGE       (uncompressed)          : '  + dogeuaddr)
            print( 'Dash Coin DASH       (compressed)            : '  + dashcaddr)
            print( 'Dash Coin DASH       (uncompressed)          : '  + dashuaddr)
            print( 'SmartCoin SMC        (compressed)            : '  + smartcaddr)
            print( 'SmartCoin SMC        (uncompressed)          : '  + smartuaddr)
            print( 'Zcash ZCASH          (compressed)            : '  + zcashcaddr)
            print( 'Zcash  ZCASH         (uncompressed)          : '  + zcashuaddr)
            print( 'Horizen ZEN          (compressed)            : '  + zencaddr)
            print( 'Horizen ZEN          (uncompressed)          : '  + zenuaddr)
            print( 'Zeitcoin ZEIT        (compressed)            : '  + zeitcaddr)
            print( 'Zeitcoin ZEIT        (uncompressed)          : '  + zeituaddr)
            print( 'Ethereum  ETH                                : '  + eaddr)
            print( '=========================== Hash 160 =================================' )
            print( 'compressed   Hash 160   : '  , crmd.hex())
            print( 'uncompressed  Hash 160  : '  , urmd.hex())
            print( '=========================== Private Keys =============================' )
            print('BTC Private Key (compressed WIF)    : '  +cwif)
            print('BTC  Private Key(Uncompressed WIF)  : '  + uwif)
            print('Private key HEX                     : '  + privatekey)
            print( '=========================== Public Keys ==============================' )
            print('compressed  Public Key    : '  , cpub.hex())
            print('uncompressed  Public Key  : '  , upub.hex())
            f=open(u"winner.txt","a")
            f.write('\nboomcpu.py made by mizogg.co.uk donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD')
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
            #print( "\nboomcpu.py---" +  "---------mizogg.co.uk---------" +  "---boomcpu.py"  )
            #print( 'Total Addresses\HASH160\PUBLICKEYS Loaded and Checking : ' , line_count)
            #print( '=========================== Address ==================================' )
            #print( 'Bitcoin BTC          (compressed)            : '  + caddr)
            #print( 'Bitcoin BTC          (uncompressed)          : '  + uaddr)
            #print( 'Bitcoin BTC          (P2SH)                  : '  + paddr)
            #print( 'Bitcoin BTC          (bech32 p2wpkh)         : '  + bcaddr)
            #print( 'Litecoin LTC         (compressed)            : '  + lcaddr)
            #print( 'Litecoin LTC         (uncompressed)          : '  + luaddr)
            #print( 'Litecoin LTC         (P2SH)                  : '  + lpaddr)
            #print( 'Litecoin LTC         (bech32 p2wpkh)         : '  + lbpaddr)
            #print( 'Bitcoin GOLD BTG     (compressed)            : '  + btgcaddr)
            #print( 'Bitcoin GOLD BTG     (uncompressed)          : '  + btguaddr)
            #print( 'Bitcoin GOLD BTG     (P2SH)                  : '  + btgpaddr)
            #print( 'Bitcoin GOLD BTG     (bech32 p2wpkh)         : '  + btgbpaddr)
            #print( 'BITCOINZ BTCZ        (compressed)            : '  + btczcaddr)
            #print( 'BITCOINZ BTCZ        (uncompressed)          : '  + btczuaddr)
            #print( 'TENT coin TENT       (compressed)            : '  + tentcaddr)
            #print( 'TENT coin TENT       (uncompressed)          : '  + tentuaddr)
            #print( 'Doge Coin DOGE       (compressed)            : '  + dogecaddr)
            #print( 'Doge Coin DOGE       (uncompressed)          : '  + dogeuaddr)
            #print( 'Dash Coin DASH       (compressed)            : '  + dashcaddr)
            #print( 'Dash Coin DASH       (uncompressed)          : '  + dashuaddr)
            #print( 'SmartCoin SMC        (compressed)            : '  + smartcaddr)
            #print( 'SmartCoin SMC        (uncompressed)          : '  + smartuaddr)
            #print( 'Zcash ZCASH          (compressed)            : '  + zcashcaddr)
            #print( 'Zcash  ZCASH         (uncompressed)          : '  + zcashuaddr)
            #print( 'Horizen ZEN          (compressed)            : '  + zencaddr)
            #print( 'Horizen ZEN          (uncompressed)          : '  + zenuaddr)
            #print( 'Zeitcoin ZEIT        (compressed)            : '  + zeitcaddr)
            #print( 'Zeitcoin ZEIT        (uncompressed)          : '  + zeituaddr)
            #print( 'Ethereum  ETH                                : '  + eaddr)
            #print( '=========================== Hash 160 =================================' )
            #print( 'compressed   Hash 160   : '  , crmd.hex())
            #print( 'uncompressed  Hash 160  : '  , urmd.hex())
            #print( '=========================== Private Keys =============================' )
            #print('BTC Private Key (compressed WIF)    : '  +cwif)
            #print('BTC  Private Key(Uncompressed WIF)  : '  + uwif)
            #print('Private key HEX                     : '  + privatekey)
            #print( '=========================== Public Keys ==============================' )
            #print('compressed  Public Key    : '  , cpub.hex())
            #print('uncompressed  Public Key  : '  , upub.hex())
            print ( 'Running Scan : ' + str (count) + '  :  ' +  'Total Private Keys : ' + str(totalkey) + '  :  ' +  'Total Addresses : ' + str (total), end='\r' )
       



threads = []


for i in range(int(threadCount)):
    t = threading.Thread(target=seek)
    threads.append(t)
    t.start()