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
        
        job_officerid = request.POST['Partner']
        vol_name = request.POST['subject1']
        eq_name = request.POST['subject']
        subeq_name = request.POST['topic']
        f_image = request.FILES['image']

        abnor_name = "สภาพปกติ,บิ่นแตก"

        print(type(f_image))
        print(f_image)
        print(vol_name)
        print(abnor_name)

      
        
        
        
        #22KV เสา
        if  vol_name == "22KV" and eq_name == "เสา" and subeq_name == "เสาคอนกรีต" and abnor_name =="สภาพปกติ":
            vol_name = "D"
            eq_name = "PO"
            subeq_name = "0"
            abnor_name ="0A"

        if  vol_name == "22KV" and eq_name == "เสา" and subeq_name == "เสาคอนกรีต" and abnor_name =="บิ่นแตก":
            vol_name = "D"
            eq_name = "PO"
            subeq_name = "0"
            abnor_name ="2A"
        
        if  vol_name == "22KV" and eq_name == "เสา" and subeq_name == "เสาคอนกรีต" and abnor_name =="สภาพปกติ,บิ่นแตก":
            vol_name = "D"
            eq_name = "PO"
            subeq_name = "0"
            abnor_name ="0A"

            filename = request.FILES['image'].name
            f = os.path.splitext(filename)
            n = f[0]
            ext = f[1]
            #timedate & time in Python

            timestr = time.strftime("%Y%m%d-%H%M%S")


            f_image.name = "{}_{}_{}_{}_{}_{}{}".format(job_officerid, vol_name, eq_name, subeq_name, abnor_name, timestr, ext)
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

            job_picture = "https://objectstorage.ap-tokyo-1.oraclecloud.com/p/dI47BfTpwxXJODPhiO1p2wmYqyL0M-6b4TqRxU1ETcPDVFSjOC9sjXxPi9W-NomC/n/peacloud/b/Aidea/o/{}".format(f_image.name)

            nameimageold = filename
            nameimagenew = f_image.name
            ## save ข้อมูลลง ฐานข้อมูล 
            
            img = Image(job_officerid=job_officerid, eq_name=eq_name, subeq_name=subeq_name, abnor_name=abnor_name, vol_name=vol_name, nameimageold=nameimageold, nameimagenew=nameimagenew, pathimage=pathimage, job_picture=job_picture)
            img.save()
            
            context={'data':{' job_officerid':job_officerid, 'eq_name':eq_name, 'subeq_name':subeq_name, 'abnor_name':abnor_name, 'vol_name':vol_name, 'pathimage':pathimage, 'job_picture':job_picture, 'image':f_image}}
            ## save ข้อมูลลง ฐานข้อมูล 

            pathimage = "/media/{}".format(f_image.name) 
            vol_name = "D"
            eq_name = "PO"
            subeq_name = "0"
            abnor_name ="2A"

            img = Image(job_officerid=job_officerid, eq_name=eq_name, subeq_name=subeq_name, abnor_name=abnor_name, vol_name=vol_name, nameimageold=nameimageold, nameimagenew=nameimagenew, pathimage=pathimage, job_picture=job_picture)
            img.save()
            
            context={'data':{' job_officerid':job_officerid, 'eq_name':eq_name, 'subeq_name':subeq_name, 'abnor_name':abnor_name, 'vol_name':vol_name, 'pathimage':pathimage, 'job_picture':job_picture, 'image':f_image}}
            ## save ข้อมูลลง ฐานข้อมูล 
        
        

        # # checklist nodata 
        # if   job_officerid == " ":
        #      job_officerid = "NODATA"
    
        # if  vol_name == " ":
        #     vol_name = "NODATA"

        # if  eq_name == " ":
        #     eq_name = "NODATA"

        # if  subeq_name == " ":
        #     subeq_name = "NODATA"
            
        # if  abnor_name == " ":
        #     abnor_name = "NODATA"

        


        # #timedate & time in Python

        # timestr = time.strftime("%Y%m%d-%H%M%S")


        # f_image.name = "{}_{}_{}_{}_{}_{}{}".format( job_officerid, vol_name, eq_name, subeq_name, abnor_name, timestr, ext)
        # print(f_image.name)


        # #past image
        # pathimage = "/media/{}".format(f_image.name) 
        # print(pathimage)


        # # UP image cload
        # uploaded_file = request.FILES['image']
        # print(uploaded_file)
        # payload=uploaded_file
        # headers = {
        # 'Content-Type': 'image/jpg'
        # }
        # path_file = f_image.name

        # url = "https://objectstorage.ap-tokyo-1.oraclecloud.com/p/dI47BfTpwxXJODPhiO1p2wmYqyL0M-6b4TqRxU1ETcPDVFSjOC9sjXxPi9W-NomC/n/peacloud/b/Aidea/o/" + path_file


        # response = requests.request("PUT", url, headers=headers, data=payload)

        # pathimage = "https://objectstorage.ap-tokyo-1.oraclecloud.com/p/dI47BfTpwxXJODPhiO1p2wmYqyL0M-6b4TqRxU1ETcPDVFSjOC9sjXxPi9W-NomC/n/peacloud/b/Aidea/o/{}".format(f_image.name)

        # nameimageold = filename
        # nameimagenew = f_image.name
        # ## save ข้อมูลลง ฐานข้อมูล 
        
        # img = Image( job_officerid= job_officerid, eq_name=eq_name, subeq_name=subeq_name, abnor_name=abnor_name, vol_name=vol_name, nameimageold=nameimageold, nameimagenew=nameimagenew, pathimage=pathimage, pathimage=pathimage, image=f_image)
        # img.save()
        
        # context={'data':{' job_officerid': job_officerid, 'eq_name':eq_name, 'subeq_name':subeq_name, 'abnor_name':abnor_name, 'vol_name':vol_name, 'pathimage':pathimage, 'pathimage':pathimage, 'image':f_image}}
        # ## save ข้อมูลลง ฐานข้อมูล 


        

    
        
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
    
   
    return render(request, 'login.html')
    


def bad(request): #หน้า bad
    if request.method == 'POST':
        print(request.POST)
        job_officerid = request.POST['Partner']
        Circuit = request.POST['subject1']
        subeq_name = request.POST['topic']
        abnor_name = request.POST['chapter']
        f_image = request.FILES['image']
        
        
        print(type(f_image))
        print(f_image)
        print(Circuit)
        print(abnor_name)

        filename = request.FILES['image'].name
        f = os.path.splitext(filename)
        n = f[0]
        ext = f[1]
        
       
    

        #115KV สายดิน
        if  Circuit == "115KV" and subeq_name == "สายดิน" and abnor_name =="ขาด":
            subeq_name = "GR"
            abnor_name ="11"
        if  Circuit == "115KV" and subeq_name == "สายดิน" and abnor_name =="หย่อน":
            subeq_name = "GR"
            abnor_name ="12"
        if  Circuit == "115KV" and subeq_name == "สายดิน" and abnor_name =="เป็นสนิม":
            subeq_name = "GR"
            abnor_name ="13"
        if  Circuit == "115KV" and subeq_name == "สายดิน" and abnor_name =="จุดสนิม":
            subeq_name = "GR"
            abnor_name ="14"
        
        #115KV ลูกถ้วย
        if  Circuit == "115KV" and subeq_name == "ลูกถ้วย" and abnor_name =="แตก/บิ่น":
            subeq_name = "IN"
            abnor_name ="11"
        if  Circuit == "115KV" and subeq_name == "ลูกถ้วย" and abnor_name =="แฟลช":
            subeq_name = "IN"
            abnor_name ="12"
        if  Circuit == "115KV" and subeq_name == "ลูกถ้วย" and abnor_name =="แตกลาย":
            subeq_name = "IN"
            abnor_name ="13"
        if  Circuit == "115KV" and subeq_name == "ลูกถ้วย" and abnor_name =="เปลี่ยนสี":
            subeq_name = "IN"
            abnor_name ="14"
        if  Circuit == "115KV" and subeq_name == "ลูกถ้วย" and abnor_name =="คราปสกปรก":
            subeq_name = "IN"
            abnor_name ="15"

        #115KV สายไฟ
        if  Circuit == "115KV" and subeq_name == "สายไฟ" and abnor_name =="สายแตก":
            subeq_name = "LI"
            abnor_name ="11"
        if  Circuit == "115KV" and subeq_name == "สายไฟ" and abnor_name =="คลายตัว":
            subeq_name = "LI"
            abnor_name ="12"
        if  Circuit == "115KV" and subeq_name == "สายไฟ" and abnor_name =="อุปกรณ์จับสายชำรุด":
            subeq_name = "LI"
            abnor_name ="13"

        #115KV จุดต่อ            
        if  Circuit == "115KV" and subeq_name == "จุดต่อ" and abnor_name =="เปลี่ยนสี/เป็นสนิม":
            subeq_name = "CO"
            abnor_name ="11"
        if  Circuit == "115KV" and subeq_name == "จุดต่อ" and abnor_name =="มีรอยอาร์ด":
            subeq_name = "CO"
            abnor_name ="12"
        if  Circuit == "115KV" and subeq_name == "จุดต่อ" and abnor_name =="บิดงอเสียรูป":
            subeq_name = "CO"
            abnor_name ="13"

        #115KV อุปกรณ์ตัดตอน  
        if  Circuit == "115KV" and subeq_name == "อุปกรณ์ตัดตอน" and abnor_name =="บิ่น":
            subeq_name = "DS"
            abnor_name ="11"
        if  Circuit == "115KV" and subeq_name == "อุปกรณ์ตัดตอน" and abnor_name =="แตก":
            subeq_name = "DS"
            abnor_name ="12"
        if  Circuit == "115KV" and subeq_name == "อุปกรณ์ตัดตอน" and abnor_name =="มีรอยอาร์ค":
            subeq_name = "DS"
            abnor_name ="13"



        #33KV สายดิน
        if  Circuit == "33KV" and subeq_name == "สายดิน" and abnor_name =="ขาด":
            subeq_name = "GR"
            abnor_name ="31"
        if  Circuit == "33KV" and subeq_name == "สายดิน" and abnor_name =="หย่อน":
            subeq_name = "GR"
            abnor_name ="32"
        if  Circuit == "33KV" and subeq_name == "สายดิน" and abnor_name =="เป็นสนิม":
            subeq_name = "GR"
            abnor_name ="33"
        if  Circuit == "33KV" and subeq_name == "สายดิน" and abnor_name =="จุดต่อหลวม":
            subeq_name = "GR"
            abnor_name ="34"


        #33KV ลูกถ้วย
        if  Circuit == "33KV" and subeq_name == "ลูกถ้วย" and abnor_name =="แตก/บิ่น":
            subeq_name = "IN"
            abnor_name ="31"
        if  Circuit == "33KV" and subeq_name == "ลูกถ้วย" and abnor_name =="แฟลช":
            subeq_name = "IN"
            abnor_name ="32"
        if  Circuit == "33KV" and subeq_name == "ลูกถ้วย" and abnor_name =="แตกลาย":
            subeq_name = "IN"
            abnor_name ="33"
        if  Circuit == "33KV" and subeq_name == "ลูกถ้วย" and abnor_name =="เปลี่ยนสี":
            subeq_name = "IN"
            abnor_name ="34"
        if  Circuit == "33KV" and subeq_name == "ลูกถ้วย" and abnor_name =="คราปสกปรก":
            subeq_name = "IN"
            abnor_name ="35"
        
        #33KV สายไฟ
        if  Circuit == "33KV" and subeq_name == "สายไฟ" and abnor_name =="สายแตก":
            subeq_name = "LI"
            abnor_name ="31"
        if  Circuit == "33KV" and subeq_name == "สายไฟ" and abnor_name =="คลายตัว":
            subeq_name = "LI"
            abnor_name ="32"
        if  Circuit == "33KV" and subeq_name == "สายไฟ" and abnor_name =="อุปกรณ์จับสายชำรุด":
            subeq_name = "LI"
            abnor_name ="33"

        #33KV จุดต่อ
        if  Circuit == "33KV" and subeq_name == "จุดต่อ" and abnor_name =="เปลี่ยนสี/เป็นสนิม":
            subeq_name = "CO"
            abnor_name ="31"
        if  Circuit == "33KV" and subeq_name == "จุดต่อ" and abnor_name =="มีรอยอาร์ด":
            subeq_name = "CO"
            abnor_name ="32"
        if  Circuit == "33KV" and subeq_name == "จุดต่อ" and abnor_name =="บิดงอเสียรูป":
            subeq_name = "CO"
            abnor_name ="33"


         #33KV ล่อฟ้า
        if  Circuit == "33KV" and subeq_name == "ล่อฟ้า" and abnor_name =="บิ่นแตก/แตก/ฉีก":
            subeq_name = "LA"
            abnor_name ="31"
        if  Circuit == "33KV" and subeq_name == "ล่อฟ้า" and abnor_name =="มีรอยอาร์ค":
            subeq_name = "LA"
            abnor_name ="32"
        if  Circuit == "33KV" and subeq_name == "ล่อฟ้า" and abnor_name =="ผิวสกปรก":
            subeq_name = "LA"
            abnor_name ="33"
        if  Circuit == "33KV" and subeq_name == "ล่อฟ้า" and abnor_name =="เปลี่ยนสี":
            subeq_name = "LA"
            abnor_name ="34"

         #33KV คาปาซิเตอร์
        if  Circuit == "33KV" and subeq_name == "คาปาซิเตอร์" and abnor_name =="บิ่น/แตก":
            subeq_name = "CA"
            abnor_name ="31"
        if  Circuit == "33KV" and subeq_name == "คาปาซิเตอร์" and abnor_name =="มีรอยอาร์ค":
            subeq_name = "CA"
            abnor_name ="32"
        if  Circuit == "33KV" and subeq_name == "คาปาซิเตอร์" and abnor_name =="ผิวสกปรก":
            subeq_name = "CA"
            abnor_name ="33"


        #22 KV สายดิน
        if  Circuit == "22KV" and subeq_name == "สายดิน" and abnor_name =="ขาด":
            subeq_name = "GR"
            abnor_name ="31"
        if  Circuit == "22KV" and subeq_name == "สายดิน" and abnor_name =="หย่อน":
            subeq_name = "GR"
            abnor_name ="32"
        if  Circuit == "22KV" and subeq_name == "สายดิน" and abnor_name =="เป็นสนิม":
            subeq_name = "GR"
            abnor_name ="33"
        if  Circuit == "22KV" and subeq_name == "สายดิน" and abnor_name =="จุดต่อหลวม":
            subeq_name = "GR"
            abnor_name ="34"


        #22 KV ลูกถ้วย
        if  Circuit == "22KV" and subeq_name == "ลูกถ้วย" and abnor_name =="แตก/บิ่น":
            subeq_name = "IN"
            abnor_name ="31"
        if  Circuit == "22KV" and subeq_name == "ลูกถ้วย" and abnor_name =="แฟลช":
            subeq_name = "IN"
            abnor_name ="32"
        if  Circuit == "22KV" and subeq_name == "ลูกถ้วย" and abnor_name =="แตกลาย":
            subeq_name = "IN"
            abnor_name ="33"
        if  Circuit == "22KV" and subeq_name == "ลูกถ้วย" and abnor_name =="เปลี่ยนสี":
            subeq_name = "IN"
            abnor_name ="34"
        if  Circuit == "22KV" and subeq_name == "ลูกถ้วย" and abnor_name =="คราปสกปรก":
            subeq_name = "IN"
            abnor_name ="35"
        
        #22 KV สายไฟ
        if  Circuit == "22KV" and subeq_name == "สายไฟ" and abnor_name =="สายแตก":
            subeq_name = "LI"
            abnor_name ="31"
        if  Circuit == "22KV" and subeq_name == "สายไฟ" and abnor_name =="คลายตัว":
            subeq_name = "LI"
            abnor_name ="32"
        if  Circuit == "22KV" and subeq_name == "สายไฟ" and abnor_name =="อุปกรณ์จับสายชำรุด":
            subeq_name = "LI"
            abnor_name ="33"

        #22 KV จุดต่อ
        if  Circuit == "22KV" and subeq_name == "จุดต่อ" and abnor_name =="เปลี่ยนสี/เป็นสนิม":
            subeq_name = "CO"
            abnor_name ="31"
        if  Circuit == "22KV" and subeq_name == "จุดต่อ" and abnor_name =="มีรอยอาร์ด":
            subeq_name = "CO"
            abnor_name ="32"
        if  Circuit == "22KV" and subeq_name == "จุดต่อ" and abnor_name =="บิดงอเสียรูป":
            subeq_name = "CO"
            abnor_name ="33"


         #22 KV ล่อฟ้า
        if  Circuit == "22KV" and subeq_name == "ล่อฟ้า" and abnor_name =="บิ่นแตก/แตก/ฉีก":
            subeq_name = "LA"
            abnor_name ="31"
        if  Circuit == "22KV" and subeq_name == "ล่อฟ้า" and abnor_name =="มีรอยอาร์ค":
            subeq_name = "LA"
            abnor_name ="32"
        if  Circuit == "22KV" and subeq_name == "ล่อฟ้า" and abnor_name =="ผิวสกปรก":
            subeq_name = "LA"
            abnor_name ="33"
        if  Circuit == "22KV" and subeq_name == "ล่อฟ้า" and abnor_name =="เปลี่ยนสี":
            subeq_name = "LA"
            abnor_name ="34"

         #22 KV คาปาซิเตอร์
        if  Circuit == "22KV" and subeq_name == "คาปาซิเตอร์" and abnor_name =="บิ่น/แตก":
            subeq_name = "CA"
            abnor_name ="31"
        if  Circuit == "22KV" and subeq_name == "คาปาซิเตอร์" and abnor_name =="มีรอยอาร์ค":
            subeq_name = "CA"
            abnor_name ="32"
        if  Circuit == "22KV" and subeq_name == "คาปาซิเตอร์" and abnor_name =="ผิวสกปรก":
            subeq_name = "CA"
            abnor_name ="33"


        # checklist nodata 
        if  Circuit == " ":
            Circuit = "NODATA"

        if  subeq_name == " ":
            subeq_name = "NODATA"
            
        if  abnor_name == " ":
            abnor_name = "NODATA"

        if   job_officerid == " ":
             job_officerid = "NODATA"



        #timedate & time in Python

        timestr = time.strftime("%Y%m%d-%H%M%S")


        f_image.name = "{}_{}_{}_{}_{}{}".format( job_officerid, Circuit, subeq_name, abnor_name, timestr, ext)
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

        pathimage = "https://objectstorage.ap-tokyo-1.oraclecloud.com/p/dI47BfTpwxXJODPhiO1p2wmYqyL0M-6b4TqRxU1ETcPDVFSjOC9sjXxPi9W-NomC/n/peacloud/b/Aidea/o/{}".format(f_image.name)

        nameimageold = filename
        nameimagenew = f_image.name
        ## save ข้อมูลลง ฐานข้อมูล 
       
        img = Image( job_officerid= job_officerid, subeq_name=subeq_name, abnor_name=abnor_name, Circuit=Circuit, nameimageold=nameimageold, nameimagenew=nameimagenew, pathimage=pathimage, image=f_image)
        img.save()
        
        context={'data':{' job_officerid': job_officerid, 'subeq_name':subeq_name, 'abnor_name':abnor_name, 'Circuit':Circuit, 'pathimage':pathimage, 'pathimage':pathimage, 'image':f_image}}
        ## save ข้อมูลลง ฐานข้อมูล 

    
        
        return render(request,'home.html', context=context)
    return render(request, 'bad.html')


def good(request): #หน้า bad
    if request.method == 'POST':
        print(request.POST)
        Circuit = request.POST['subject']
        subeq_name = request.POST['topic']
        f_image = request.FILES['image']

        
        print(type(f_image))
        print(f_image)

        filename = request.FILES['image'].name
        f = os.path.splitext(filename)
        n = f[0]
        ext = f[1]
        
        


        
        abnor_name ="" 
       #115KV สายดิน
        if  Circuit == "115KV" and subeq_name == "สายดิน" and abnor_name =="":
            subeq_name = "GR"
            abnor_name ="GR10"
        if  Circuit == "115KV" and subeq_name == "ลูกถ้วย" and abnor_name =="":
            subeq_name = "IN"
            abnor_name ="IN10"
        if  Circuit == "115KV" and subeq_name == "สายไฟ" and abnor_name =="":
            subeq_name = "LI"
            abnor_name ="LI10"
        if  Circuit == "115KV" and subeq_name == "สายดิน" and abnor_name =="":
            subeq_name = "CO"
            abnor_name ="CO10"
        if  Circuit == "115KV" and subeq_name == "สายดิน" and abnor_name =="":
            subeq_name = "DS"
            abnor_name ="DS10"




        #33KV สายดิน
        if  Circuit == "33KV" and subeq_name == "สายดิน" and abnor_name =="":
            subeq_name = "GR"
            abnor_name ="GR30"
        if  Circuit == "33KV" and subeq_name == "ลูกถ้วย" and abnor_name =="":
            subeq_name = "IN"
            abnor_name ="IN30"
        if  Circuit == "33KV" and subeq_name == "สายไฟ" and abnor_name =="":
            subeq_name = "LI"
            abnor_name ="LI30"
        if  Circuit == "33KV" and subeq_name == "จุดต่อ" and abnor_name =="":
            subeq_name = "CO"
            abnor_name ="CO30"
        if  Circuit == "33KV" and subeq_name == "ล่อฟ้า" and abnor_name =="":
            subeq_name = "LA"
            abnor_name ="DS30"
        if  Circuit == "33KV" and subeq_name == "คาปาซิเตอร์" and abnor_name =="":
            subeq_name = "CA"
            abnor_name ="CO30"
        if  Circuit == "33KV" and subeq_name == "อุปกรณ์ตัดตอน" and abnor_name =="":
            subeq_name = "DS"
            abnor_name ="DS30"


         #33KV สายดิน
        if  Circuit == "33KV" and subeq_name == "สายดิน" and abnor_name =="":
            subeq_name = "GR"
            abnor_name ="GR30"
        if  Circuit == "33KV" and subeq_name == "ลูกถ้วย" and abnor_name =="":
            subeq_name = "IN"
            abnor_name ="IN30"
        if  Circuit == "33KV" and subeq_name == "สายไฟ" and abnor_name =="":
            subeq_name = "LI"
            abnor_name ="LI30"
        if  Circuit == "33KV" and subeq_name == "จุดต่อ" and abnor_name =="":
            subeq_name = "CO"
            abnor_name ="CO30"
        if  Circuit == "33KV" and subeq_name == "ล่อฟ้า" and abnor_name =="":
            subeq_name = "LA"
            abnor_name ="LA30"
        if  Circuit == "33KV" and subeq_name == "คาปาซิเตอร์" and abnor_name =="":
            subeq_name = "CA"
            abnor_name ="CA30"
        if  Circuit == "33KV" and subeq_name == "อุปกรณ์ตัดตอน" and abnor_name =="":
            subeq_name = "DS"
            abnor_name ="DS30"


        #22KV สายดิน
        if  Circuit == "22KV" and subeq_name == "สายดิน" and abnor_name =="":
            subeq_name = "GR"
            abnor_name ="GR20"
        if  Circuit == "22KV" and subeq_name == "ลูกถ้วย" and abnor_name =="":
            subeq_name = "IN"
            abnor_name ="IN20"
        if  Circuit == "22KV" and subeq_name == "สายไฟ" and abnor_name =="":
            subeq_name = "LI"
            abnor_name ="LI20"
        if  Circuit == "22KV" and subeq_name == "จุดต่อ" and abnor_name =="":
            subeq_name = "CO"
            abnor_name ="CO20"
        if  Circuit == "22KV" and subeq_name == "ล่อฟ้า" and abnor_name =="":
            subeq_name = "LA"
            abnor_name ="LA20"
        if  Circuit == "22KV" and subeq_name == "คาปาซิเตอร์" and abnor_name =="":
            subeq_name = "CA"
            abnor_name ="CA22"
        if  Circuit == "22KV" and subeq_name == "อุปกรณ์ตัดตอน" and abnor_name =="":
            subeq_name = "DS"
            abnor_name ="DS22"


        #timedate & time in Python

        timestr = time.strftime("%Y%m%d-%H%M%S")


        f_image.name = "{}_{}_{}_{}{}".format(Circuit, subeq_name, abnor_name, timestr, ext)
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

        pathimage = "https://objectstorage.ap-tokyo-1.oraclecloud.com/p/dI47BfTpwxXJODPhiO1p2wmYqyL0M-6b4TqRxU1ETcPDVFSjOC9sjXxPi9W-NomC/n/peacloud/b/Aidea/o/{}".format(f_image.name)

        nameimageold = filename
        nameimagenew = f_image.name
        ## save ข้อมูลลง ฐานข้อมูล 
       
        img = Image(subeq_name=subeq_name, abnor_name=abnor_name, Circuit=Circuit, nameimageold=nameimageold, nameimagenew=nameimagenew, pathimage=pathimage, job_picture=job_picture, image=f_image)
        img.save()
        
        context={'data':{'subeq_name':subeq_name, 'abnor_name':abnor_name, 'Circuit':Circuit, 'pathimage':pathimage, 'job_picture':job_picture, 'image':f_image}}
        ## save ข้อมูลลง ฐานข้อมูล 

    
        
        return render(request,'home.html', context=context)
    return render(request, 'good.html')

def home(request): #หน้า good.html
  
    return render(request, 'home.html')

def register(request):
    return render(request, 'register.html')



