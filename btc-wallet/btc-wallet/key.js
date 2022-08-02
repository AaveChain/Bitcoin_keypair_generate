import generate from 'btc-address-generator'

const addr = generate()


{
  network: 'testnet', // testnet (default), bitcoin, litecoin
  mnemonic: '12 words mnemonic', // mnemonic (default null)
  path: "m/44'/1'/0'" // default testnet detrive path
}

console.log(addr)