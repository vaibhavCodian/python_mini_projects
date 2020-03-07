from cryptosteganography import CryptoSteganography
import getpass

# crypto_steganography = CryptoSteganography('My secret password key')
# # Save the encrypted file inside the image
# crypto_steganography.hide('img0.jpg', 'op.png', 'My secret message')

# secret = crypto_steganography.retrieve('op.png')

# print(secret)
def encode():
    img_path = input("\t Enter IMG path With Extension (ex: img.png) :")
    op_path = input("\t Enter Output path: ")
    msg = input("\t Enter msg")
    pswd = input("\t Enter Stegno Pass: ")
    steg = CryptoSteganography(pswd)
    steg.hide(img_path, op_path, msg)
    print("Success Fully Save at: "+ op_path + "\n")
    return main()

def decode():
    pswd = input("\t Enter Stegno Pass: ")
    ip_path = input("\t Enter Stegno File Path: ") 
    steg = CryptoSteganography(pswd)
    msg = steg.retrieve(ip_path)
    print("_________________MESSAGE________________")
    print("\t" +msg)
    print
    return main()

def ip_handle(task):
    if task.lower() == 'exit':
        print("Thanks FOr Using Stegno_____")
        
    elif task[0].lower() == 'd':
        decode()
    elif task[0].lower() == 'e':
        print("Thanks FOr Using Stegno_____")
    else:
        print(" Unrecognized Command ")
        return main()

def main():
    task = input("Select What You Wnat To  Do: \n 1: Encode (E) \n 2: Decode (D) \n 3: Exit (ex) \n --> \t")
    ip_handle(task)
    
        
    
if __name__ == "__main__":
    main()




