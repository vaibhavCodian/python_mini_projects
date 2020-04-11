from cryptosteganography import CryptoSteganography

print("""

 (                                         
 )\ )      )                               
(()/(   ( /(     (    (  (                 
 /(_))  )\())   ))\   )\))(    (       (   
(_))   (_))/   /((_) ((_))\    )\ )    )\  
/ __|  | |_   (_))    (()(_)  _(_/(   ((_) 
\__ \  |  _|  / -_)  / _` |  | ' \)) / _ \ 
|___/   \__|  \___|  \__, |  |_||_|  \___/ 
                     |___/                                                              

____________________________________________CREATED BY:  ┬  ┬┌─┐┬┌┐ ┬ ┬┌─┐┬  ┬╔═╗┌─┐┌┬┐┬┌─┐┌┐┌
                                                         └┐┌┘├─┤│├┴┐├─┤├─┤└┐┌┘║  │ │ │││├─┤│││
                                                          └┘ ┴ ┴┴└─┘┴ ┴┴ ┴ └┘ ╚═╝└─┘─┴┘┴┴ ┴┘└┘
                                                                                                                                                    
                 
""")

def encode():
    img_path = input("\t Enter IMG path With Extension (ex: img.png) :")
    op_path = input("\t Enter Output Image Name (ex: opImage): ") + ".png"
    msg = input("\t Enter msg: ")
    pswd = input("\t Enter Stegno Pass: ")
    steg = CryptoSteganography(pswd)
    steg.hide(img_path, op_path, msg)
    print("Success Fully Save at: "+ op_path + "\n")
    return main()

def decode():
    pswd = input("\t Enter Stegno Pass: ")
    ip_path = input("\t Enter Stegno File Name (ex: opImage): ") + ".png" 
    steg = CryptoSteganography(pswd)
    msg = steg.retrieve(ip_path)
    print("_________________MESSAGE________________\n")
    print("\t ", msg)
    print("\n________________________________________\n")
    return main()

def ip_handle(task):
    if task.lower() == 'exit':
        print("Thanks FOr Using Stegno_____")
        
    elif task[0].lower() == 'd':
        decode()
    elif task[0].lower() == 'e':
        encode()
    else:
        print("Unrecognized Command ")
        return main()

def main():
    task = input("Select What You Wnat To  Do: \n 1: Encode (e) \n 2: Decode (d) \n 3: Exit (exit) \n --> \t")
    ip_handle(task)
    
        
    
if __name__ == "__main__":
    main()




