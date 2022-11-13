import csv
import os
from datetime import *
from datetime import time
import urllib.request
import cv2
import face_recognition
import numpy as np
import requests
from django.shortcuts import render
from django.http import HttpResponseRedirect


# Create your views here.

def page(request):
        while True:
                video_capture=cv2.VideoCapture("http://192.168.163.54/capture");

                img1=face_recognition.load_image_file('C:\\Users\\nithe\\OneDrive\\Desktop\\Django-imgprocess\\Imageprocessing\\members\\static\\1.jpg');
                img1_encoding=face_recognition.face_encodings(img1)[0]

                img2=face_recognition.load_image_file('C:\\Users\\nithe\\OneDrive\\Desktop\\Django-imgprocess\\Imageprocessing\\members\\static\\2.jpg');
                img2_encoding=face_recognition.face_encodings(img2)[0]

                img3=face_recognition.load_image_file('C:\\Users\\nithe\\OneDrive\\Desktop\\Django-imgprocess\\Imageprocessing\\members\\static\\3.jpg');
                img3_encoding=face_recognition.face_encodings(img3)[0]

                img4=face_recognition.load_image_file('C:\\Users\\nithe\\OneDrive\\Desktop\\Django-imgprocess\\Imageprocessing\\members\\static\\4.jpg');
                img4_encoding=face_recognition.face_encodings(img4)[0]
                
                auth_face=[
                    img1_encoding,
                    img2_encoding,
                    img3_encoding,
                    img4_encoding
                ]
                auth_face_names=[
                    "Pratik k",
                    "Abdullah Zaid",
                    "Nitheeshwar",
                    "Pavan B N"
                ]
                students=auth_face_names.copy()
                face_locations=[]
                face_encodings=[]

                s=True

                now=datetime.now();
                current_date=now.strftime("%Y-%m-%d");

                file=open(current_date+'.csv','w+',newline='');
                lnwriter=csv.writer(file)
                imgResponse=urllib.request.urlopen('http://192.168.163.54/capture')
                imgNp= np.array(bytearray(imgResponse.read()),dtype=np.uint8)
                cv2.waitKey(5000);
                _,frame=video_capture.read();
                    # small_frame=cv2.resize(frame,(0,0),fx=0.25,fy=0.25);
                    # rgb_small_frame=small_frame[:,:,::];
                if s:
                        face_locations=face_recognition.face_locations(frame)
                        face_encodings=face_recognition.face_encodings(frame,face_locations)
                        face_names=[]
                        for face_enc in face_encodings:
                            matches=face_recognition.compare_faces(auth_face,face_enc)
                            name="";
                            face_dist=face_recognition.face_distance(auth_face,face_enc);
                            bmi=np.argmin(face_dist)
                            if matches[bmi]:
                                name=auth_face_names[bmi]

                            face_names.append(name)
                            if name in auth_face_names:
                                if name in students:
                                    students.remove(name)
                                    print(students)
                                    current_time=now.strftime("%H-%M-%S")
                                    lnwriter.writerow([name,current_time])
                            

                        cv2.imshow("attendance system",frame)
                        if cv2.waitKey(1) & 0xFF==ord('q'):
                            break;  
                
                
                
        video_capture.release()
        cv2.destroyAllWindows()
        # return render(request,"C:\\Users\\nithe\\OneDrive\\Desktop\\Django-imgprocess\\Imageprocessing\\members\\templates\\page.html",{'abslist':students})
        file.close()
        
def home(request):
    return render(request,"C:\\Users\\nithe\\OneDrive\\Desktop\\Django-imgprocess\\Imageprocessing\\members\\templates\page.html")
