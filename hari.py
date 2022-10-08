import cv2
import mysql.connector
import face_recognition
import random
class takingphoto:
  def __init__(self):
      self.name = input('enter your name')
      self.rollno = int(input("enter ur roll no"))
      self.image = None
  def takephoto(self):
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if cv2.waitKey(1) == ord('q'):
            break
        face1 = face_recognition.face_locations(frame)
        for x,y,w,h in face1:
            frame = cv2.rectangle(frame,(x,y),(w,h),(0,255,0),1)
        cv2.imshow('frame', frame)
    cap.release()
    cv2.destroyAllWindows()
    cam_port = 0
    img3: object = frame
    face1 = face_recognition.face_locations(img3)

    
    if len(face1) != 0:
        faceLoc = face1[0]
        self.image = img3
        return 0
    else:
        return self.takephoto()
mydb = mysql.connector.connect(host="localhost",user="root",passwd="harilal190",database="students")
mycursor = mydb.cursor()
def insert(rollno,name,photo):
    a = "insert into  mystudents(roll,name,imagead) values(%s,'%s','%s');"%(str(rollno),name,photo)
    mycursor.execute(a)
    try:
        mydb.commit()
    except:
        print("please enter diffrent roll no")
filename = random.randint(0,999999999999999999)
c = '%s.png'%str(filename)
hari = takingphoto()
hari.takephoto()
cv2.imwrite(c,hari.image)
insert(hari.rollno,hari.name,c)