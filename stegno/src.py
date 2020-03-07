from cryptosteganography import CryptoSteganography

crypto_steganography = CryptoSteganography('My secret password key')

# Save the encrypted file inside the image
crypto_steganography.hide('img0.jpg', 'op.png', 'My secret message')

secret = crypto_steganography.retrieve('op.png')

print(secret)
# My secret message