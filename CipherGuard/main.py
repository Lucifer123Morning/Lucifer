import pyAesCrypt

password = input('enter the password to encrypt the file')

# encrypt
pyAesCrypt.encryptFile('', 'data.txt.aes', password)

# dectypt
pyAesCrypt.encryptFile('data.txt.aes', 'dataout.txt', password)