from base64 import decode
from lib2to3.pytree import convert
import cv2
import numpy as np
import face_recognition
from PIL import Image
import base64


def facerecognize(img,img3):
    img = covertstringtophoto(img)
    img3 = covertstringtophoto(img3)
    face1 = face_recognition.face_locations(img)
    faceLoc = face1[0]
    faceemb = face_recognition.face_encodings(img)[0]
    a = face_recognition.face_locations(img3)
    testemb = face_recognition.face_encodings(img3)[0]
    results = face_recognition.compare_faces([faceemb],testemb)
    return(results[0])
def covertstringtophoto(string):
    decode_data = base64.b64decode(string)
    np_data = np.fromstring(decode_data,np.uint8)
    img = cv2.imdecode(np_data,cv2.IMREAD_UNCHANGED)
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    return img_gray 
def my_function(filepath):
    data = open(filepath, "r")
    return str(data)
hari = ""
kala = ""
with open("C:\\Users\\ilove\\OneDrive\\Desktop\\pythonProject3\\592208469122375653.png", "rb") as img_file:
    hari = base64.b64encode(img_file.read()) 
with open("C:\\Users\\ilove\\OneDrive\\Desktop\\pythonProject3\\184861966085580944.png", "rb") as img_file:
    kala = base64.b64encode(img_file.read()) 

print(facerecognize(hari,kala))


