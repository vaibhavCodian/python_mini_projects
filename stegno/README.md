    
    
     ____     __                                        
    /\  _`\  /\ \__                                     
    \ \,\L\_\\ \ ,_\     __      __      ___      ___   
     \/_\__ \ \ \ \/   /'__`\  /'_ `\  /' _ `\   / __`\ 
       /\ \L\ \\ \ \_ /\  __/ /\ \L\ \ /\ \/\ \ /\ \L\ \
       \ `\____\\ \__\\ \____\\ \____ \\ \_\ \_\\ \____/
        \/_____/ \/__/ \/____/ \/___L\ \\/_/\/_/ \/___/ 
                                 /\____/                
                                 \_/__/                 
    

    __________CREATED BY:  
                              __                   
               /  /          /  )     /            
    , ___.  o /__/_  __. , _/   __ __/ o __.  ____ 
    \/(_/|_<_/_)/ /_(_/|_\/(__/(_)(_/_<_(_/|_/ / <_
                                                   
                                                   
*A Basic Console Based Implementaion Of Stegnograpy For Images with Python*

- To Run The Programm first install cryptosteganography by typing following command in Termianal
```shell
pip install cryptosteganography
```
- After Installing The Required Package you can get started by hiding simple text message into an image.
- run the program by:
```shell
python Stegno.py
```
- Select Wether You Want to encode or decode the data into the Image, by typing 'e'(Encode) or 'd'(Decode), respectively by typing it into the terminal
```shell
Select What You Wnat To  Do: 
 1: Encode (e) 
 2: Decode (d) 
 3: Exit (exit) 
 --> 	
```
#### 1. In the Case of ENCODE
- fill in the appropriate data respectively in the terminal

		 --> 	e
		 	 Enter IMG path With Extension (ex: img.png) :img0.jpg	
			 Enter Output Image Name (ex: opImage): output_image_name
		 	 Enter msg: Temprory Message To Be Displaed    
		 	 Enter Stegno Pass: password
		
		Success Fully Save at: output_image_name.png

- Image Will Be Saved In The Same Path as the input image

 #### 2. In the case of Decode
 
	  --> 	d
		 Enter Stegno Pass: password           
		 Enter Stegno File Name (ex: opImage): output_image_name
		________________MESSAGE________________
		  
		  Temprory Message To Be Displaed
		_____________________________________

 #### 3. Finally To Exit The Program:
 - Type exit
		  --> 	exit
		Thanks FOr Using Stegno_____
