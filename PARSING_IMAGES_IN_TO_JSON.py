#!/usr/bin/env python
# coding: utf-8




#liabraries required
import os 
import json
import base64


# # Reding the Image and writing it in to a json file




path_to_image = "/home/anubhav/grpup.jpg"

#creating an empty dixxt for making a json 
data = {}

#uding open to read the image in binary
with open (path_to_image,'rb') as f:
    image=f.read()
#we have read the image and now we will write it to the dic
#N.B : we need to encode this binary form in to utf-8 string  so that this can be inserted in to the json
data['Image_Encoded_format'] = base64.encodebytes(image).decode("utf-8")

#we gave create our dict now we will use json module to save our json file
#we will create the obj of json dump 
obj = json.dumps(data,indent=4)
#using open we will write the file
with open("/home/anubhav/SHARMAJI/IMG_PROCESS/rett2.json",'w') as q:
    q.write(obj)


# # Reading the json and extracting the image and save it locally 




#it will read the json file that we have created earlier 
with open("/home/anubhav/IMG_PROCESS/rett2.json") as a:
    da = json.load(a)




#now we need to convert the utf-6 string back to binary using decode function in base64
res2=base64.b64decode(da['Image_Encoded_format'])



#Now we have converted the file in to a binary object
#we will write the binary as a jpeg in local file system
with open ("/home/anubhav/SHARMAJI/IMG_PROCESS/binary_jpg.jpg",'wb') as q:
    q.write(res2)

