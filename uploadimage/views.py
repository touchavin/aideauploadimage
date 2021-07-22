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
def aidea(request): #หน้า aidea.html
    if request.method == 'POST':
        print(request.POST)
        Customer_number = request.POST['Partner']
        Circuit = request.POST['subject1']
        Category = request.POST['subject']
        Accessory = request.POST['topic']
        Case = request.POST['chapter']
        f_image = request.FILES['image']
        

        print(type(f_image))
        print(f_image)
        print(Circuit)
        print(Case)

        filename = request.FILES['image'].name
        f = os.path.splitext(filename)
        n = f[0]
        ext = f[1]
        
        #22KV เสา
        if  Circuit == "22KV" and Category == "เสา" and Accessory == "เสาคอนกรีต" and Case =="สภาพปกติ":
            Circuit = "D"
            Category = "PO"
            Accessory = "0"
            Case ="0A"
        

        # checklist nodata 
        if  Customer_number == " ":
            Customer_number = "NODATA"
    
        if  Circuit == " ":
            Circuit = "NODATA"

        if  Category == " ":
            Category = "NODATA"

        if  Accessory == " ":
            Accessory = "NODATA"
            
        if  Case == " ":
            Case = "NODATA"

        


        #timedate & time in Python

        timestr = time.strftime("%Y%m%d-%H%M%S")


        f_image.name = "{}_{}_{}_{}_{}_{}{}".format(Customer_number, Circuit, Category, Accessory, Case, timestr, ext)
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

        nameimageold = filename
        nameimagenew = f_image.name
        ## save ข้อมูลลง ฐานข้อมูล 
       
        img = Image(Customer_number=Customer_number, Accessory=Accessory, Case=Case, Circuit=Circuit, nameimageold=nameimageold, nameimagenew=nameimagenew, pathimage=pathimage, pathoraclecloud=pathoraclecloud, image=f_image)
        img.save()
        
        context={'data':{'Customer_number':Customer_number, 'Accessory':Accessory, 'Case':Case, 'Circuit':Circuit, 'pathimage':pathimage, 'pathoraclecloud':pathoraclecloud, 'image':f_image}}
        ## save ข้อมูลลง ฐานข้อมูล 

    
        
        return render(request,'home.html', context=context)
    return render(request, 'aidea.html')


   
def test(request): #หน้า index.html
    if request.method == 'POST':
        Circuit = request.POST['langOpt[]']
        print(Circuit)
    
       
    
        ## save ข้อมูลลง ฐานข้อมูล 
        img = Image(Circuit=Circuit)
        img.save()
       
    return render(request, 'test.html')

def login(request): #หน้า index.html
    if request.method == 'POST':
        Customer_number = request.POST['Customer_number']
        
        context={'data':{'Customer_number':Customer_number}}
        ## save ข้อมูลลง ฐานข้อมูล 

        return render(request,'home.html', context=context)
    return render(request, 'login.html')
    


def bad(request): #หน้า bad
    if request.method == 'POST':
        print(request.POST)
        Customer_number = request.POST['Partner']
        Circuit = request.POST['subject1']
        Accessory = request.POST['topic']
        Case = request.POST['chapter']
        f_image = request.FILES['image']
        
        
        print(type(f_image))
        print(f_image)
        print(Circuit)
        print(Case)

        filename = request.FILES['image'].name
        f = os.path.splitext(filename)
        n = f[0]
        ext = f[1]
        
       
    

        #115KV สายดิน
        if  Circuit == "115KV" and Accessory == "สายดิน" and Case =="ขาด":
            Accessory = "GR"
            Case ="11"
        if  Circuit == "115KV" and Accessory == "สายดิน" and Case =="หย่อน":
            Accessory = "GR"
            Case ="12"
        if  Circuit == "115KV" and Accessory == "สายดิน" and Case =="เป็นสนิม":
            Accessory = "GR"
            Case ="13"
        if  Circuit == "115KV" and Accessory == "สายดิน" and Case =="จุดสนิม":
            Accessory = "GR"
            Case ="14"
        
        #115KV ลูกถ้วย
        if  Circuit == "115KV" and Accessory == "ลูกถ้วย" and Case =="แตก/บิ่น":
            Accessory = "IN"
            Case ="11"
        if  Circuit == "115KV" and Accessory == "ลูกถ้วย" and Case =="แฟลช":
            Accessory = "IN"
            Case ="12"
        if  Circuit == "115KV" and Accessory == "ลูกถ้วย" and Case =="แตกลาย":
            Accessory = "IN"
            Case ="13"
        if  Circuit == "115KV" and Accessory == "ลูกถ้วย" and Case =="เปลี่ยนสี":
            Accessory = "IN"
            Case ="14"
        if  Circuit == "115KV" and Accessory == "ลูกถ้วย" and Case =="คราปสกปรก":
            Accessory = "IN"
            Case ="15"

        #115KV สายไฟ
        if  Circuit == "115KV" and Accessory == "สายไฟ" and Case =="สายแตก":
            Accessory = "LI"
            Case ="11"
        if  Circuit == "115KV" and Accessory == "สายไฟ" and Case =="คลายตัว":
            Accessory = "LI"
            Case ="12"
        if  Circuit == "115KV" and Accessory == "สายไฟ" and Case =="อุปกรณ์จับสายชำรุด":
            Accessory = "LI"
            Case ="13"

        #115KV จุดต่อ            
        if  Circuit == "115KV" and Accessory == "จุดต่อ" and Case =="เปลี่ยนสี/เป็นสนิม":
            Accessory = "CO"
            Case ="11"
        if  Circuit == "115KV" and Accessory == "จุดต่อ" and Case =="มีรอยอาร์ด":
            Accessory = "CO"
            Case ="12"
        if  Circuit == "115KV" and Accessory == "จุดต่อ" and Case =="บิดงอเสียรูป":
            Accessory = "CO"
            Case ="13"

        #115KV อุปกรณ์ตัดตอน  
        if  Circuit == "115KV" and Accessory == "อุปกรณ์ตัดตอน" and Case =="บิ่น":
            Accessory = "DS"
            Case ="11"
        if  Circuit == "115KV" and Accessory == "อุปกรณ์ตัดตอน" and Case =="แตก":
            Accessory = "DS"
            Case ="12"
        if  Circuit == "115KV" and Accessory == "อุปกรณ์ตัดตอน" and Case =="มีรอยอาร์ค":
            Accessory = "DS"
            Case ="13"



        #33KV สายดิน
        if  Circuit == "33KV" and Accessory == "สายดิน" and Case =="ขาด":
            Accessory = "GR"
            Case ="31"
        if  Circuit == "33KV" and Accessory == "สายดิน" and Case =="หย่อน":
            Accessory = "GR"
            Case ="32"
        if  Circuit == "33KV" and Accessory == "สายดิน" and Case =="เป็นสนิม":
            Accessory = "GR"
            Case ="33"
        if  Circuit == "33KV" and Accessory == "สายดิน" and Case =="จุดต่อหลวม":
            Accessory = "GR"
            Case ="34"


        #33KV ลูกถ้วย
        if  Circuit == "33KV" and Accessory == "ลูกถ้วย" and Case =="แตก/บิ่น":
            Accessory = "IN"
            Case ="31"
        if  Circuit == "33KV" and Accessory == "ลูกถ้วย" and Case =="แฟลช":
            Accessory = "IN"
            Case ="32"
        if  Circuit == "33KV" and Accessory == "ลูกถ้วย" and Case =="แตกลาย":
            Accessory = "IN"
            Case ="33"
        if  Circuit == "33KV" and Accessory == "ลูกถ้วย" and Case =="เปลี่ยนสี":
            Accessory = "IN"
            Case ="34"
        if  Circuit == "33KV" and Accessory == "ลูกถ้วย" and Case =="คราปสกปรก":
            Accessory = "IN"
            Case ="35"
        
        #33KV สายไฟ
        if  Circuit == "33KV" and Accessory == "สายไฟ" and Case =="สายแตก":
            Accessory = "LI"
            Case ="31"
        if  Circuit == "33KV" and Accessory == "สายไฟ" and Case =="คลายตัว":
            Accessory = "LI"
            Case ="32"
        if  Circuit == "33KV" and Accessory == "สายไฟ" and Case =="อุปกรณ์จับสายชำรุด":
            Accessory = "LI"
            Case ="33"

        #33KV จุดต่อ
        if  Circuit == "33KV" and Accessory == "จุดต่อ" and Case =="เปลี่ยนสี/เป็นสนิม":
            Accessory = "CO"
            Case ="31"
        if  Circuit == "33KV" and Accessory == "จุดต่อ" and Case =="มีรอยอาร์ด":
            Accessory = "CO"
            Case ="32"
        if  Circuit == "33KV" and Accessory == "จุดต่อ" and Case =="บิดงอเสียรูป":
            Accessory = "CO"
            Case ="33"


         #33KV ล่อฟ้า
        if  Circuit == "33KV" and Accessory == "ล่อฟ้า" and Case =="บิ่นแตก/แตก/ฉีก":
            Accessory = "LA"
            Case ="31"
        if  Circuit == "33KV" and Accessory == "ล่อฟ้า" and Case =="มีรอยอาร์ค":
            Accessory = "LA"
            Case ="32"
        if  Circuit == "33KV" and Accessory == "ล่อฟ้า" and Case =="ผิวสกปรก":
            Accessory = "LA"
            Case ="33"
        if  Circuit == "33KV" and Accessory == "ล่อฟ้า" and Case =="เปลี่ยนสี":
            Accessory = "LA"
            Case ="34"

         #33KV คาปาซิเตอร์
        if  Circuit == "33KV" and Accessory == "คาปาซิเตอร์" and Case =="บิ่น/แตก":
            Accessory = "CA"
            Case ="31"
        if  Circuit == "33KV" and Accessory == "คาปาซิเตอร์" and Case =="มีรอยอาร์ค":
            Accessory = "CA"
            Case ="32"
        if  Circuit == "33KV" and Accessory == "คาปาซิเตอร์" and Case =="ผิวสกปรก":
            Accessory = "CA"
            Case ="33"


        #22 KV สายดิน
        if  Circuit == "22KV" and Accessory == "สายดิน" and Case =="ขาด":
            Accessory = "GR"
            Case ="31"
        if  Circuit == "22KV" and Accessory == "สายดิน" and Case =="หย่อน":
            Accessory = "GR"
            Case ="32"
        if  Circuit == "22KV" and Accessory == "สายดิน" and Case =="เป็นสนิม":
            Accessory = "GR"
            Case ="33"
        if  Circuit == "22KV" and Accessory == "สายดิน" and Case =="จุดต่อหลวม":
            Accessory = "GR"
            Case ="34"


        #22 KV ลูกถ้วย
        if  Circuit == "22KV" and Accessory == "ลูกถ้วย" and Case =="แตก/บิ่น":
            Accessory = "IN"
            Case ="31"
        if  Circuit == "22KV" and Accessory == "ลูกถ้วย" and Case =="แฟลช":
            Accessory = "IN"
            Case ="32"
        if  Circuit == "22KV" and Accessory == "ลูกถ้วย" and Case =="แตกลาย":
            Accessory = "IN"
            Case ="33"
        if  Circuit == "22KV" and Accessory == "ลูกถ้วย" and Case =="เปลี่ยนสี":
            Accessory = "IN"
            Case ="34"
        if  Circuit == "22KV" and Accessory == "ลูกถ้วย" and Case =="คราปสกปรก":
            Accessory = "IN"
            Case ="35"
        
        #22 KV สายไฟ
        if  Circuit == "22KV" and Accessory == "สายไฟ" and Case =="สายแตก":
            Accessory = "LI"
            Case ="31"
        if  Circuit == "22KV" and Accessory == "สายไฟ" and Case =="คลายตัว":
            Accessory = "LI"
            Case ="32"
        if  Circuit == "22KV" and Accessory == "สายไฟ" and Case =="อุปกรณ์จับสายชำรุด":
            Accessory = "LI"
            Case ="33"

        #22 KV จุดต่อ
        if  Circuit == "22KV" and Accessory == "จุดต่อ" and Case =="เปลี่ยนสี/เป็นสนิม":
            Accessory = "CO"
            Case ="31"
        if  Circuit == "22KV" and Accessory == "จุดต่อ" and Case =="มีรอยอาร์ด":
            Accessory = "CO"
            Case ="32"
        if  Circuit == "22KV" and Accessory == "จุดต่อ" and Case =="บิดงอเสียรูป":
            Accessory = "CO"
            Case ="33"


         #22 KV ล่อฟ้า
        if  Circuit == "22KV" and Accessory == "ล่อฟ้า" and Case =="บิ่นแตก/แตก/ฉีก":
            Accessory = "LA"
            Case ="31"
        if  Circuit == "22KV" and Accessory == "ล่อฟ้า" and Case =="มีรอยอาร์ค":
            Accessory = "LA"
            Case ="32"
        if  Circuit == "22KV" and Accessory == "ล่อฟ้า" and Case =="ผิวสกปรก":
            Accessory = "LA"
            Case ="33"
        if  Circuit == "22KV" and Accessory == "ล่อฟ้า" and Case =="เปลี่ยนสี":
            Accessory = "LA"
            Case ="34"

         #22 KV คาปาซิเตอร์
        if  Circuit == "22KV" and Accessory == "คาปาซิเตอร์" and Case =="บิ่น/แตก":
            Accessory = "CA"
            Case ="31"
        if  Circuit == "22KV" and Accessory == "คาปาซิเตอร์" and Case =="มีรอยอาร์ค":
            Accessory = "CA"
            Case ="32"
        if  Circuit == "22KV" and Accessory == "คาปาซิเตอร์" and Case =="ผิวสกปรก":
            Accessory = "CA"
            Case ="33"


        # checklist nodata 
        if  Circuit == " ":
            Circuit = "NODATA"

        if  Accessory == " ":
            Accessory = "NODATA"
            
        if  Case == " ":
            Case = "NODATA"

        if  Customer_number == " ":
            Customer_number = "NODATA"



        #timedate & time in Python

        timestr = time.strftime("%Y%m%d-%H%M%S")


        f_image.name = "{}_{}_{}_{}_{}{}".format(Customer_number, Circuit, Accessory, Case, timestr, ext)
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

        nameimageold = filename
        nameimagenew = f_image.name
        ## save ข้อมูลลง ฐานข้อมูล 
       
        img = Image(Customer_number=Customer_number, Accessory=Accessory, Case=Case, Circuit=Circuit, nameimageold=nameimageold, nameimagenew=nameimagenew, pathimage=pathimage, pathoraclecloud=pathoraclecloud, image=f_image)
        img.save()
        
        context={'data':{'Customer_number':Customer_number, 'Accessory':Accessory, 'Case':Case, 'Circuit':Circuit, 'pathimage':pathimage, 'pathoraclecloud':pathoraclecloud, 'image':f_image}}
        ## save ข้อมูลลง ฐานข้อมูล 

    
        
        return render(request,'home.html', context=context)
    return render(request, 'bad.html')


def good(request): #หน้า bad
    if request.method == 'POST':
        print(request.POST)
        Circuit = request.POST['subject']
        Accessory = request.POST['topic']
        f_image = request.FILES['image']

        
        print(type(f_image))
        print(f_image)

        filename = request.FILES['image'].name
        f = os.path.splitext(filename)
        n = f[0]
        ext = f[1]
        
        


        
        Case ="" 
       #115KV สายดิน
        if  Circuit == "115KV" and Accessory == "สายดิน" and Case =="":
            Accessory = "GR"
            Case ="GR10"
        if  Circuit == "115KV" and Accessory == "ลูกถ้วย" and Case =="":
            Accessory = "IN"
            Case ="IN10"
        if  Circuit == "115KV" and Accessory == "สายไฟ" and Case =="":
            Accessory = "LI"
            Case ="LI10"
        if  Circuit == "115KV" and Accessory == "สายดิน" and Case =="":
            Accessory = "CO"
            Case ="CO10"
        if  Circuit == "115KV" and Accessory == "สายดิน" and Case =="":
            Accessory = "DS"
            Case ="DS10"




        #33KV สายดิน
        if  Circuit == "33KV" and Accessory == "สายดิน" and Case =="":
            Accessory = "GR"
            Case ="GR30"
        if  Circuit == "33KV" and Accessory == "ลูกถ้วย" and Case =="":
            Accessory = "IN"
            Case ="IN30"
        if  Circuit == "33KV" and Accessory == "สายไฟ" and Case =="":
            Accessory = "LI"
            Case ="LI30"
        if  Circuit == "33KV" and Accessory == "จุดต่อ" and Case =="":
            Accessory = "CO"
            Case ="CO30"
        if  Circuit == "33KV" and Accessory == "ล่อฟ้า" and Case =="":
            Accessory = "LA"
            Case ="DS30"
        if  Circuit == "33KV" and Accessory == "คาปาซิเตอร์" and Case =="":
            Accessory = "CA"
            Case ="CO30"
        if  Circuit == "33KV" and Accessory == "อุปกรณ์ตัดตอน" and Case =="":
            Accessory = "DS"
            Case ="DS30"


         #33KV สายดิน
        if  Circuit == "33KV" and Accessory == "สายดิน" and Case =="":
            Accessory = "GR"
            Case ="GR30"
        if  Circuit == "33KV" and Accessory == "ลูกถ้วย" and Case =="":
            Accessory = "IN"
            Case ="IN30"
        if  Circuit == "33KV" and Accessory == "สายไฟ" and Case =="":
            Accessory = "LI"
            Case ="LI30"
        if  Circuit == "33KV" and Accessory == "จุดต่อ" and Case =="":
            Accessory = "CO"
            Case ="CO30"
        if  Circuit == "33KV" and Accessory == "ล่อฟ้า" and Case =="":
            Accessory = "LA"
            Case ="LA30"
        if  Circuit == "33KV" and Accessory == "คาปาซิเตอร์" and Case =="":
            Accessory = "CA"
            Case ="CA30"
        if  Circuit == "33KV" and Accessory == "อุปกรณ์ตัดตอน" and Case =="":
            Accessory = "DS"
            Case ="DS30"


        #22KV สายดิน
        if  Circuit == "22KV" and Accessory == "สายดิน" and Case =="":
            Accessory = "GR"
            Case ="GR20"
        if  Circuit == "22KV" and Accessory == "ลูกถ้วย" and Case =="":
            Accessory = "IN"
            Case ="IN20"
        if  Circuit == "22KV" and Accessory == "สายไฟ" and Case =="":
            Accessory = "LI"
            Case ="LI20"
        if  Circuit == "22KV" and Accessory == "จุดต่อ" and Case =="":
            Accessory = "CO"
            Case ="CO20"
        if  Circuit == "22KV" and Accessory == "ล่อฟ้า" and Case =="":
            Accessory = "LA"
            Case ="LA20"
        if  Circuit == "22KV" and Accessory == "คาปาซิเตอร์" and Case =="":
            Accessory = "CA"
            Case ="CA22"
        if  Circuit == "22KV" and Accessory == "อุปกรณ์ตัดตอน" and Case =="":
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

        nameimageold = filename
        nameimagenew = f_image.name
        ## save ข้อมูลลง ฐานข้อมูล 
       
        img = Image(Accessory=Accessory, Case=Case, Circuit=Circuit, nameimageold=nameimageold, nameimagenew=nameimagenew, pathimage=pathimage, pathoraclecloud=pathoraclecloud, image=f_image)
        img.save()
        
        context={'data':{'Accessory':Accessory, 'Case':Case, 'Circuit':Circuit, 'pathimage':pathimage, 'pathoraclecloud':pathoraclecloud, 'image':f_image}}
        ## save ข้อมูลลง ฐานข้อมูล 

    
        
        return render(request,'home.html', context=context)
    return render(request, 'good.html')

def home(request): #หน้า good.html
  
    return render(request, 'home.html')

def register(request):
    return render(request, 'register.html')



