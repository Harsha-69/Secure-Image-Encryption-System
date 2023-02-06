from cryptography.fernet import Fernet
import pysapphire
from pysapphire.sapphire import encrypt, decrypt
import os


f_path  = "static/uploads/"

i = "WIN_20230203_14_35_52_Pro.jpg"



def encrypt_image(imName):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    with open('key.key','wb') as filekey:
        filekey.write(key)
    with open('key.key','rb') as filekey:
        key = filekey.read()
    with open(f_path+imName,'rb') as file:
        original_file = file.read()
    encrypted = pysapphire.sapphire.encrypt(key,original_file)
    with open(f_path+"EN_"+imName,'wb') as file:
        file.write(encrypted)
    return "EN_"+imName



def decrypt_image(ENim):
    with open('key.key','rb') as filekey:
        key = filekey.read()
    fernet = Fernet(key)
    with open(f_path+ENim,'rb') as file:
        enc_file = file.read()
    decrypted = decrypt(key,enc_file)
    with open(f_path+"DEC_"+ENim,'wb') as file:
        file.write(decrypted)
    return "DEC_"+ENim


if __name__ == "__main__":
    a = encrypt_image(i)
    b = decrypt_image(a)
    print(a,b)



    
