import random
bits = random.getrandbits(256)
bits_hex = hex(bits)
private_key = bits_hex[2:]
import secrets
bits = secrets.randbits(256)

bits_hex = hex(bits)
private_key = bits_hex[2:]


def __init_pool(self):
    for i in range(self.POOL_SIZE):
        random_byte = secrets.randbits(8)
        self.__seed_byte(random_byte)
    time_int = int(time.time())
    self.__seed_int(time_int)
def __seed_int(self, n):
    self.__seed_byte(n)
    self.__seed_byte(n >> 8)
    self.__seed_byte(n >> 16)
    self.__seed_byte(n >> 24)
def __seed_byte(self, n):
    self.pool[self.pool_pointer] ^= n & 255
    self.pool_pointer += 1
    if self.pool_pointer >= self.POOL_SIZE:
        self.pool_pointer = 0

def seed_input(self, str_input):
    time_int = int(time.time())
    self.__seed_int(time_int)
    for char in str_input:
        char_code = ord(char)
        self.__seed_byte(char_code)

def generate_key(self):
    big_int = self.__generate_big_int()
    big_int = big_int % (self.CURVE_ORDER -1)   #key < curve order
    big_int = big_int + 1 # key > 0
    key = hex(big_int)[2:]
    return key
def __generate_big_int(self):
    if self.prng_state is None:
       seed = int.from_bytes(self.pool, byteorder="big", signed=False)
       random.seed(seed)
       self.prng_state = random.getstate()
       random.setstate(self.prng_state)
       big_int = random.getrandbits(self.KEY_BYTES * 8)
       self.prng_state = random.getstate()
       return big_int

kg = KeyGenerator()
kg.seed_input("Truly random string. I rolled a dice and got 4.")
kg.generate_key()    

