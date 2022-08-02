import ecdsa
import hashlib
import binascii
import base58
from mnemonic import Mnemonic
from byte import NetworkByteTestnet


#ECDSA used for generate Private Key 
ecdsaPrivateKey = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
print("ECDSA Private Key: ", ecdsaPrivateKey.to_string().hex())



#ECDSA used for generate Public Key that depends on a Private Key 
ecdsaPublicKey = '04' +  ecdsaPrivateKey.get_verifying_key().to_string().hex()
print("ECDSA Public Key: ", ecdsaPublicKey)


#apply SHA256 to ECDSA Public Key
hash256FromECDSAPublicKey = hashlib.sha256(binascii.unhexlify(ecdsaPublicKey)).hexdigest()
print("SHA256(ECDSA Public Key): ", hash256FromECDSAPublicKey)


#apply RIDEMP160 to value and get value as 20 byytes
ridemp160FromHash256 = hashlib.new('ripemd160', binascii.unhexlify(hash256FromECDSAPublicKey))
print("RIDEMP160(SHA256(ECDSA Public Key)): ", ridemp160FromHash256.hexdigest())


#prepend 00 as Network Byte to value
prependNetworkByte = '00' + ridemp160FromHash256.hexdigest()
print("Prepend Network Byte to RIDEMP160(SHA256(ECDSA Public Key)): ", prependNetworkByte)

prependNetworkByte= NetworkByteTestnet()



#apply double SHA256 value to Checksum
hash = NetworkByteTestnet()

#hash = prependNetworkByte
for x in range(1,3):
    hash = hashlib.sha256(binascii.unhexlify(hash)).hexdigest()
    print("\t|___>SHA256 #", x, " : ", hash)


#get 4 bytes
cheksum = hash[:8]
print("Checksum(first 4 bytes): ", cheksum)  

#append Checksum value
appendChecksum = prependNetworkByte + cheksum
print("Append Checksum to RIDEMP160(SHA256(ECDSA Public Key)): ", appendChecksum)


#applied Base58 Encoding
bitcoinAddress = base58.b58encode(binascii.unhexlify(appendChecksum))
print("Bitcoin Address: ", bitcoinAddress.decode('utf8'))