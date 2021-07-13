from django.shortcuts import render
from .models import Image

from datetime import datetime
from .models import Image


from django.contrib.auth import authenticate, login


from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
)

from base64 import b64decode




import json
import requests

import os
import time
def login(request): #หน้า index.html
  
    return render(request, 'login.html')
def good(request): #หน้า good
    if request.method == 'POST':
        print(request.POST)
        # Customer_number = request.POST['Customer_number']
        Circuit = request.POST['subject']
        Accessory = request.POST['topic']
        f_image = request.FILES['image']
        
        
        # Add เปลี่ยนชื่อ รูป

        print(type(f_image))
        print(f_image)
        
        filename = request.FILES['image'].name
        f = os.path.splitext(filename)
        n = f[0]
        ext = f[1]
        nameimageold = filename

        #115KV สายดิน
        if  Circuit == "115KV" and Accessory == "สายดิน":
            Accessory = "GR"
            Case ="GR10"
        if  Circuit == "115KV" and Accessory == "ลูกถ้วย":
            Accessory = "IN"
            Case ="IN10"
        if  Circuit == "115KV" and Accessory == "สายไฟ":
            Accessory = "LI"
            Case ="LI10"
        if  Circuit == "115KV" and Accessory == "สายดิน":
            Accessory = "CO"
            Case ="CO10"
        if  Circuit == "115KV" and Accessory == "สายดิน":
            Accessory = "DS"
            Case ="DS10"




        #33KV สายดิน
        if  Circuit == "33KV" and Accessory == "สายดิน":
            Accessory = "GR"
            Case ="GR30"
        if  Circuit == "33KV" and Accessory == "ลูกถ้วย":
            Accessory = "IN"
            Case ="IN30"
        if  Circuit == "33KV" and Accessory == "สายไฟ":
            Accessory = "LI"
            Case ="LI30"
        if  Circuit == "33KV" and Accessory == "จุดต่อ":
            Accessory = "CO"
            Case ="CO30"
        if  Circuit == "33KV" and Accessory == "ล่อฟ้า":
            Accessory = "LA"
            Case ="DS30"
        if  Circuit == "33KV" and Accessory == "คาปาซิเตอร์":
            Accessory = "CA"
            Case ="CO30"
        if  Circuit == "33KV" and Accessory == "อุปกรณ์ตัดตอน":
            Accessory = "DS"
            Case ="DS30"


         #33KV สายดิน
        if  Circuit == "33KV" and Accessory == "สายดิน":
            Accessory = "GR"
            Case ="GR30"
        if  Circuit == "33KV" and Accessory == "ลูกถ้วย":
            Accessory = "IN"
            Case ="IN30"
        if  Circuit == "33KV" and Accessory == "สายไฟ":
            Accessory = "LI"
            Case ="LI30"
        if  Circuit == "33KV" and Accessory == "จุดต่อ":
            Accessory = "CO"
            Case ="CO30"
        if  Circuit == "33KV" and Accessory == "ล่อฟ้า":
            Accessory = "LA"
            Case ="LA30"
        if  Circuit == "33KV" and Accessory == "คาปาซิเตอร์":
            Accessory = "CA"
            Case ="CA30"
        if  Circuit == "33KV" and Accessory == "อุปกรณ์ตัดตอน":
            Accessory = "DS"
            Case ="DS30"


        #22KV สายดิน
        if  Circuit == "22KV" and Accessory == "สายดิน":
            Accessory = "GR"
            Case ="GR20"
        if  Circuit == "22KV" and Accessory == "ลูกถ้วย":
            Accessory = "IN"
            Case ="IN20"
        if  Circuit == "22KV" and Accessory == "สายไฟ":
            Accessory = "LI"
            Case ="LI20"
        if  Circuit == "22KV" and Accessory == "จุดต่อ":
            Accessory = "CO"
            Case ="CO20"
        if  Circuit == "22KV" and Accessory == "ล่อฟ้า":
            Accessory = "LA"
            Case ="LA20"
        if  Circuit == "22KV" and Accessory == "คาปาซิเตอร์":
            Accessory = "CA"
            Case ="CA22"
        if  Circuit == "22KV" and Accessory == "อุปกรณ์ตัดตอน":
            Accessory = "DS"
            Case ="DS22"


       

        #timedate & time in Python

        timestr = time.strftime("%Y%m%d-%H%M%S")

        
        f_image.name = "{}_{}_{}_{}{}".format(Circuit, Accessory, Case, timestr, ext)
        print(f_image.name)

        
        #past image 
        pathimage = "/media/{}".format(f_image.name) 
        print(pathimage)

        # UP image cload
        uploaded_file = request.FILES['image']
        print(uploaded_file)
        payload=uploaded_file
        headers = {
        'Content-Type': 'image/jpg'
        }
        path_file = f_image.name

        url = "https://objectstorage.ap-tokyo-1.oraclecloud.com/p/dI47BfTpwxXJODPhiO1p2wmYqyL0M-6b4TqRxU1ETcPDVFSjOC9sjXxPi9W-NomC/n/peacloud/b/Aidea/o/" + path_file


        response = requests.request("PUT", url, headers=headers, data=payload)

            
        pathoraclecloud = "https://objectstorage.ap-tokyo-1.oraclecloud.com/p/dI47BfTpwxXJODPhiO1p2wmYqyL0M-6b4TqRxU1ETcPDVFSjOC9sjXxPi9W-NomC/n/peacloud/b/Aidea/o/{}".format(f_image.name)

        nameimagenew = f_image.name
        

        ## save ข้อมูลลง ฐานข้อมูล 
        img = Image(Accessory=Accessory, Case=Case, Circuit=Circuit, nameimageold=nameimageold, nameimagenew=nameimagenew, pathimage=pathimage, pathoraclecloud=pathoraclecloud, image=f_image)
        img.save()
        
        context={'data':{'Accessory':Accessory, 'Case':Case, 'Circuit':Circuit, 'pathimage':pathimage, 'pathoraclecloud':pathoraclecloud, 'image':f_image}}
        ## save ข้อมูลลง ฐานข้อมูล 

    
        return render(request,'home.html', context=context)
    return render(request, 'good.html')

def bad(request): #หน้า good.html
  
    return render(request, 'bad.html')

def bad(request): #หน้า good.html
  
    return render(request, 'bad.html')
def home(request): #หน้า good.html
  
    return render(request, 'home.html')



