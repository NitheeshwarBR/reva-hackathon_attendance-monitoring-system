import csv
import os
from datetime import *
from datetime import time
from urllib.request import *

import cv2
import face_recognition
import numpy as np
import requests
from django.shortcuts import render

# Create your views here.

def page(request):


    video_capture=cv2.VideoCapture("http://192.168.163.54");
    img1=face_recognition.load_image_file('C:\\Users\\nithe\\OneDrive\\Desktop\\Django-imgprocess\\Imageprocessing\\members\\static\\1.jpg');
    img1_encoding=face_recognition.face_encodings(img1)[0]
    img2=face_recognition.load_image_file('C:\\Users\\nithe\\OneDrive\\Desktop\\Django-imgprocess\\Imageprocessing\\members\\static\\2.jpg');
    img2_encoding=face_recognition.face_encodings(img2)[0]
    auth_face=[
        img1_encoding,
        img2_encoding
    ]
    auth_face_names=[
        "prathik","Zaid"
    ]
    students=auth_face_names.copy()
    face_locations=[]
    face_encodings=[]

    s=True

    now=datetime.now();
    current_date=now.strftime("%Y-%m-%d");

    file=open(current_date+'.csv','w+',newline='');
    lnwriter=csv.writer(file)

    while True:
        _,frame=video_capture.read("http://192.168.163.54/capture");
        small_frame=cv2.resize(frame,(0,0),fx=0.25,fy=0.25);
        rgb_small_frame=small_frame[:,:,::-1];
        if s:
            face_locations=face_recognition.face_locations(rgb_small_frame)
            face_encodings=face_recognition.face_encodings(rgb_small_frame,face_locations)
            face_names=[]
            for face_enc in face_encodings:
                matches=face_recognition.compare_faces(auth_face,face_enc)
                name="";
                face_dist=face_recognition.face_distance(auth_face,face_enc);
                bmi=np.argmin(face_dist);
                if matches[bmi]:
                    name=auth_face_names[bmi]

                face_names.append(name)
                if name in auth_face_names:
                    if name in students:
                        students.remove(name)
                        print(students)
                        current_time=now.strftime("%H-%M-%S");
                        lnwriter.writerow([name,current_time]);

        cv2.imshow("attendance system",frame)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break;


    video_capture.release()
    cv2.destroyAllWindows()
    file.close()
    # if request.method=="POST":
    #     return render(request,"page.html")