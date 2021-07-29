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
        # รหัสพนักงาน
        job_officerid = request.POST['Partner']
        # ระดับแรงดัน
        vol_name = request.POST['subject1']
        # ชนิดอุปกรณ์
        eq_name = request.POST['subject']
        # ประเภทอุปกรณ์
        subeq_name = request.POST['topic']
        # สาเหตุการชำรุด
        abnor_name = request.POST.getlist('chapter[]')
        abnor_other = request.POST['other']
        f_image = request.FILES['image']

        # abnor_name = ",".join(abnor_name)
        # print(abnor_name)
        # checklist nodata 
        if  job_officerid == "":
            job_officerid = "-"
        
        if  vol_name == " ":
            vol_name = "-"

        if  eq_name == " ":
            eq_name = "-"

        if  subeq_name == " ":
            subeq_name = "-"
                
        if  abnor_name == " ":
            abnor_name = "-"
            
        if  abnor_other == "":
            abnor_other = "-"

        # print('chapter[]')
        for i in abnor_name:
            abnor_name = i
            print(abnor_name)

        # abnor_name = "บิ่น,แตก,บิดงอ,เสียรูป"

            

            print(type(f_image))
            print(f_image)
            print(vol_name)
            print(abnor_name)
            
            # กรณี 1สาเหตุ
            if abnor_name =="สภาพปกติ" or abnor_name =="บิ่น,แตก" or abnor_name =="ฉีกขาด" or abnor_name =="บิดงอ,เสียรูป" or abnor_name =="เป็นสนิม" or abnor_name =="เปลี่ยนสี" or abnor_name =="รอยอาร์ค" or abnor_name =="ผิวสกปรก" or abnor_name =="หลวม,หลุด" or abnor_name =="ก้านเป็นสนิม" or abnor_name =="bolt/nut หลวม,หลุด" or abnor_name =="bolt/nut เปลี่ยนสี,เป็นสนิม" or abnor_name =="bond wire หลุด,ขาด" or abnor_name =="จุดต่อที่OHGW : หลวม,หลุด" or abnor_name =="จุดต่อที่OHGW : เปลี่ยนสี" or abnor_name =="จุดต่อที่OHGW : รอยอาร์ค" or abnor_name =="จุดต่อที่OHGW : เป็นสนิม" or abnor_name =="จุดต่อที่หัวเสา : หลวม,หลุด" or abnor_name =="จุดต่อที่หัวเสา : เปลี่ยนสี" or abnor_name =="จุดต่อที่หัวเสา : รอยอาร์ค" or abnor_name =="จุดต่อที่หัวเสา : เป็นสนิม" or abnor_name =="สายขาด" or abnor_name =="รอยแตก,ขาด" or abnor_name =="หลุดจากลูกถ้วย" or abnor_name =="หลุดจากลูกถ้วย/สเปเซอร์" or abnor_name =="ลูกถ้วยซับพอร์ต : เป็นสนิม" or abnor_name =="ลูกถ้วยซับพอร์ต : หลวม,หลุด" or abnor_name =="ลูกถ้วยซับพอร์ต : บิ่น,แตก" or abnor_name =="ลูกถ้วยซับพอร์ต : เปลี่ยนสี" or abnor_name =="ลูกถ้วยซับพอร์ต : รอยอาร์ค" or abnor_name =="ลูกถ้วยซับพอร์ต : ผิวสกปรก" or abnor_name =="จุดต่อ terminal clamp/หางปลา : หลวม,หลุด" or abnor_name =="จุดต่อ terminal clamp/หางปลา : เป็นสนิม" or abnor_name =="จุดต่อ terminal clamp/หางปลา : รอยอาร์ค" or abnor_name =="ลูกถ้วย : บิ่น,แตก" or abnor_name =="ลูกถ้วย : เปลี่ยนสี" or abnor_name =="ลูกถ้วย : รอยอาร์ค" or abnor_name =="ลูกถ้วย : ผิวสกปรก" or abnor_name =="จุดต่อ terminal clamp : หลวม,หลุด" or abnor_name =="จุดต่อ terminal clamp : เป็นสนิม" or abnor_name =="จุดต่อ terminal clamp : รอยอาร์ค" or abnor_name =="Bracket : เป็นสนิม" or abnor_name =="Bracket : หลวม,หลุด" or abnor_name =="บุชชิ่ง : บิ่น,แตก" or abnor_name =="บุชชิ่ง : เปลี่ยนสี" or abnor_name =="บุชชิ่ง : รอยอาร์ค" or abnor_name =="บุชชิ่ง : ผิวสกปรก" or abnor_name =="บุชชิ่ง :  หลวม,หลุด" or abnor_name =="ตัวถัง : เป็นสนิม" or abnor_name =="ตัวถัง : น้ำมันรั่ว" or abnor_name =="สายลีด : หลวม,หลุด" or abnor_name =="สายต่อลงดิน : รอยอาร์ค" or abnor_name =="สายต่อลงดิน : หลวม,หลุด" or abnor_name =="ครีบ : บิ่น,แตก" or abnor_name =="ครีบ : เปลี่ยนสี" or abnor_name =="ครีบ : รอยอาร์ค" or abnor_name =="ครีบ : ผิวสกปรก" or abnor_name =="ครีบ : ฉีกขาด" or abnor_name =="ชุดแขวนคาปา (Hanger) ชำรุด" or abnor_name =="ชุด interrupt : ชำรุด" or abnor_name =="จุดต่อ terminal : หลวม,หลุด" or abnor_name =="จุดต่อ terminal : เป็นสนิม" or abnor_name =="จุดต่อ terminal : รอยอาร์ค" or abnor_name =="ไม้แป้น : ชำรุด" or abnor_name =="จุดต่อOHGW/OPGW : หลวม,หลุด" or abnor_name =="จุดต่อOHGW/OPGW : เปลี่ยนสี" or abnor_name =="จุดต่อOHGW/OPGW : รอยอาร์ค" or abnor_name =="จุดต่อOHGW/OPGW : เป็นสนิม" or abnor_name =="จุดต่อที่ GROUND PLATE : หลวม,หลุด" or abnor_name =="จุดต่อ terminal clamp/pad : รอยอาร์ค" or abnor_name =="ชุดตัดอาร์ค หนวดกุ้ง : ชำรุด" or abnor_name =="ชุดดับอาร์ค : ชำรุด" or abnor_name =="อื่นๆ":
                    
                # ระดับแรงดัน 22KV,33KV,115KV
                if  vol_name == "22KV":
                    vol_name = "DA"

                if  vol_name == "33KV":
                    vol_name = "DB"

                if  vol_name == "115KV":
                    vol_name = "TA"


                # ประเภทอุปกรณ์
                if  eq_name == "เสา":
                    eq_name = "PO"

                if  eq_name == "ระบบต่อลงดิน OHGW" or eq_name == "ระบบต่อลงดินOHGW/OPGW":
                    eq_name = "GR"

                if  eq_name == "ลูกถ้วยระบบจำหน่าย" or eq_name == "ลูกถ้วยระบบสายส่ง":
                    eq_name = "IN"

                if  eq_name == "สายไฟระบบจำหน่าย และอุปกรณ์จับสาย" or eq_name == "สายไฟระบบสายส่ง และอุปกรณ์จับสาย":
                    eq_name = "CO"

                if  eq_name == "จุดต่อในระบบจำหน่าย" or eq_name == "จุดต่อในระบบสายส่ง":
                    eq_name = "JO"

                if  eq_name == "อุปกรณ์ป้องกันและตัดตอน":
                    eq_name = "SW"

                
                if  eq_name == "กับดักเสิร์จ":
                    eq_name = "AR"

                if  eq_name == "คาปาซิเตอร์":
                    eq_name = "CA"

                if  eq_name == "CT/VT":
                    eq_name = "CV"
            
                print("-----------------------")
                print(vol_name)
                print(eq_name)
                print(subeq_name)
                print("-----------------------")
                # ชนิดอุปกรณ์
                    #ชุดแรงดันที่ รหัสไม่ตรงกัน
                if  vol_name == "DA" and eq_name == "JO" and subeq_name == "t-clamp (แคล้มป์มือเสือ)":
                    subeq_name = "3A"

                if  vol_name == "DB" and eq_name == "JO" and subeq_name == "t-clamp (แคล้มป์มือเสือ)":
                    subeq_name = "3A"

                if  vol_name == "TA" and eq_name == "JO" and subeq_name == "t-clamp (แคล้มป์มือเสือ)":
                    subeq_name = "2A"

                if  vol_name == "DA" and eq_name == "JO" and subeq_name == "หางปลา":
                    subeq_name = "4A"

                if  vol_name == "DB" and eq_name == "JO" and subeq_name == "หางปลา":
                    subeq_name = "4A"

                if  vol_name == "TA" and eq_name == "JO" and subeq_name == "หางปลา":
                    subeq_name = "3A"

                    #ชุดแรงดันที่ รหัสตรงกัน
                if  subeq_name == "เสาคอนกรีต" or subeq_name == "สาย OHGW" or subeq_name == "ลูกถ้วยกระเบื้อง : ชนิด Pin Type" or subeq_name == "สายเปลือย" or subeq_name == "หลอดต่อสาย" or subeq_name == "recloser" or subeq_name == "กับดักเสิร์จกระเบื้อง : สายลีดเข้าหัวกับดักเสิร์จ" or subeq_name == "กับดักเสิร์จกระเบื้อง : สายลีดเข้าหัวกับดักเสิร์จ" or subeq_name == "fix capacitor" or subeq_name == "VT" or subeq_name == "สาย OHGW/OPGW" or subeq_name == "ลูกถ้วยกระเบื้อง" or subeq_name == "circuit switcher":
                    subeq_name = "0A"

                if  subeq_name == "เสาโครงเหล็ก" or subeq_name == "เหล็กรองรับสาย OHGW" or subeq_name == "ลูกถ้วยคอมโพสิท" or subeq_name == "สายหุ้มฉนวน" or subeq_name == "pg clamp" or subeq_name == "load break switch (SF6 )" or subeq_name == "กับดักเสิร์จคอมโพสิท" or subeq_name == "switching capacitor" or subeq_name == "VT" or subeq_name == "เหล็กรองรับสาย OHGW/OPGW" or subeq_name == "preform armorod" or subeq_name =="t-slip":
                    subeq_name = "1A"

                if  subeq_name == "คอนคอนกรีต" or subeq_name == "สาย GROUND" or subeq_name == "ลูกถ้วยแก้วเหนียว" or subeq_name == "tie wire" or subeq_name == "belt clamp,hotline clamp" or subeq_name == "air break switch":
                    subeq_name = "2A"

                if  subeq_name == "จุดต่อระบบต่อลงดิน" or subeq_name == "สเปเซอร์กระเบื้อง" or subeq_name == "disconnecting switch":
                    subeq_name = "3A"

                if  subeq_name == "ลูกถ้วยกระเบื้อง : ชนิด Line Post":
                    subeq_name = "0B"
                
                if  subeq_name == "preform armogrip":
                    subeq_name = "1B"
                
                if  subeq_name == "คอนเหล็ก" or subeq_name == "cover tie wire":
                    subeq_name = "2B"

                if  subeq_name == "ลูกถ้วยกระเบื้อง : ชนิด Pin Post":
                    subeq_name = "0C"

                if  subeq_name == "ลูกถ้วยกระเบื้อง : ชนิด ลูกถ้วยแขวน":
                    subeq_name = "0D"

                if  subeq_name == "snap tie":
                    subeq_name = "2C"

                if  subeq_name == "pin terminal":
                    subeq_name = "5A"

                if  subeq_name == "ดรอปเอ้า ฟิวส์ คัทเอ้าท์":
                    subeq_name = "4A"
                
                if  subeq_name == "preform แยกสาย":
                    subeq_name = "1C"
                
                if  subeq_name == "strain clamp":
                    subeq_name = "1D"

                if  subeq_name == "suspension clamp":
                    subeq_name = "1E"

                # สาเหตุการชำรุด
                if  abnor_name =="สภาพปกติ":
                    abnor_name ="01"

                if  abnor_name =="บิ่น,แตก":
                    abnor_name ="02"

                if  abnor_name =="ฉีกขาด":
                    abnor_name ="03"

                if  abnor_name =="บิดงอ,เสียรูป":
                    abnor_name ="04"
                    
                if  abnor_name =="เป็นสนิม":
                    abnor_name ="05"

                if  abnor_name =="เปลี่ยนสี":
                    abnor_name ="06"

                if  abnor_name =="รอยอาร์ค":
                    abnor_name ="07"

                if  abnor_name =="ผิวสกปรก":
                    abnor_name ="08"

                if  abnor_name =="หลวม,หลุด":
                    abnor_name ="09"

                if  abnor_name =="ก้านเป็นสนิม":
                    abnor_name ="10"

                if  abnor_name =="bolt/nut หลวม,หลุด":
                    abnor_name ="11"

                if  abnor_name =="bolt/nut เปลี่ยนสี,เป็นสนิม":
                    abnor_name ="12"

                if  abnor_name =="bond wire หลุด,ขาด":
                    abnor_name ="13"

                if  abnor_name =="จุดต่อที่OHGW : หลวม,หลุด":
                    abnor_name ="14"

                if  abnor_name =="จุดต่อที่OHGW : เปลี่ยนสี":
                    abnor_name ="15"

                if  abnor_name =="จุดต่อที่OHGW : รอยอาร์ค":
                    abnor_name ="16"

                if  abnor_name =="จุดต่อที่OHGW : เป็นสนิม":
                    abnor_name ="17"

                if  abnor_name =="จุดต่อที่หัวเสา : หลวม,หลุด":
                    abnor_name ="18"

                if  abnor_name =="จุดต่อที่หัวเสา : เปลี่ยนสี":
                    abnor_name ="19"

                if  abnor_name =="จุดต่อที่หัวเสา : รอยอาร์ค":
                    abnor_name ="20"
                    
                if  abnor_name =="จุดต่อที่หัวเสา : เป็นสนิม":
                    abnor_name ="21"

                if  abnor_name =="สายขาด":
                    abnor_name ="22"

                if  abnor_name =="รอยแตก,ขาด":
                    abnor_name ="23"

                if  abnor_name =="หลุดจากลูกถ้วย":
                    abnor_name ="24"

                if  abnor_name =="หลุดจากลูกถ้วย/สเปเซอร์":
                    abnor_name ="25"

                if  abnor_name =="ลูกถ้วยซับพอร์ต : เป็นสนิม":
                    abnor_name ="26"

                if  abnor_name =="ลูกถ้วยซับพอร์ต : หลวม,หลุด":
                    abnor_name ="27"

                if  abnor_name =="ลูกถ้วยซับพอร์ต : บิ่น,แตก":
                    abnor_name ="28"

                if  abnor_name =="ลูกถ้วยซับพอร์ต : เปลี่ยนสี":
                    abnor_name ="29"

                if  abnor_name =="ลูกถ้วยซับพอร์ต : รอยอาร์ค":
                    abnor_name ="30"

                if  abnor_name =="ลูกถ้วยซับพอร์ต : ผิวสกปรก":
                    abnor_name ="31"

                if  abnor_name =="จุดต่อ terminal clamp/หางปลา : หลวม,หลุด":
                    abnor_name ="32"

                if  abnor_name =="จุดต่อ terminal clamp/หางปลา : เป็นสนิม":
                    abnor_name ="33"

                if  abnor_name =="จุดต่อ terminal clamp/หางปลา : รอยอาร์ค":
                    abnor_name ="34"
                    
                if  abnor_name =="ลูกถ้วย : บิ่น,แตก":
                    abnor_name ="35"

                if  abnor_name =="ลูกถ้วย : เปลี่ยนสี":
                    abnor_name ="36"

                if  abnor_name =="ลูกถ้วย : รอยอาร์ค":
                    abnor_name ="37"

                if  abnor_name =="ลูกถ้วย : ผิวสกปรก":
                    abnor_name ="38"

                if  abnor_name =="จุดต่อ terminal clamp : หลวม,หลุด":
                    abnor_name ="39"

                if  abnor_name =="จุดต่อ terminal clamp : เป็นสนิม":
                    abnor_name ="40"

                if  abnor_name =="จุดต่อ terminal clamp : รอยอาร์ค":
                    abnor_name ="41"

                if  abnor_name =="Bracket : เป็นสนิม":
                    abnor_name ="42"

                if  abnor_name =="Bracket : หลวม,หลุด":
                    abnor_name ="43"

                if  abnor_name =="บุชชิ่ง : บิ่น,แตก":
                    abnor_name ="44"

                if  abnor_name =="บุชชิ่ง : เปลี่ยนสี":
                    abnor_name ="45"

                if  abnor_name =="บุชชิ่ง : รอยอาร์ค":
                    abnor_name ="46"

                if  abnor_name =="บุชชิ่ง : ผิวสกปรก":
                    abnor_name ="47"

                if  abnor_name =="บุชชิ่ง :  หลวม,หลุด":
                    abnor_name ="48"
                    
                if  abnor_name =="ตัวถัง : เป็นสนิม":
                    abnor_name ="49"

                if  abnor_name =="ตัวถัง : น้ำมันรั่ว":
                    abnor_name ="50"

                if  abnor_name =="สายลีด : หลวม,หลุด":
                    abnor_name ="51"

                if  abnor_name =="สายต่อลงดิน : รอยอาร์ค":
                    abnor_name ="52"

                if  abnor_name =="สายต่อลงดิน : หลวม,หลุด":
                    abnor_name ="53"

                if  abnor_name =="ครีบ : บิ่น,แตก":
                    abnor_name ="54"

                if  abnor_name =="ครีบ : เปลี่ยนสี":
                    abnor_name ="55"

                if  abnor_name =="ครีบ : รอยอาร์ค":
                    abnor_name ="56"

                if  abnor_name =="ครีบ : ผิวสกปรก":
                    abnor_name ="57"

                if  abnor_name =="ครีบ : ฉีกขาด":
                    abnor_name ="58"

                if  abnor_name =="ชุดแขวนคาปา (Hanger) ชำรุด":
                    abnor_name ="59"

                if  abnor_name =="ชุด interrupt : ชำรุด":
                    abnor_name ="60"

                if  abnor_name =="จุดต่อ terminal : หลวม,หลุด":
                    abnor_name ="61"

                if  abnor_name =="จุดต่อ terminal : เป็นสนิม":
                    abnor_name ="62"
                    
                if  abnor_name =="จุดต่อ terminal : รอยอาร์ค":
                    abnor_name ="63"

                if  abnor_name =="ไม้แป้น : ชำรุด":
                    abnor_name ="64"

                if  abnor_name =="จุดต่อOHGW/OPGW : หลวม,หลุด":
                    abnor_name ="65"

                if  abnor_name =="จุดต่อOHGW/OPGW : เปลี่ยนสี":
                    abnor_name ="66"

                if  abnor_name =="จุดต่อOHGW/OPGW : รอยอาร์ค":
                    abnor_name ="67"

                if  abnor_name =="จุดต่อOHGW/OPGW : เป็นสนิม":
                    abnor_name ="68"

                if  abnor_name =="จุดต่อที่ GROUND PLATE : หลวม,หลุด":
                    abnor_name ="69"

                if  abnor_name =="จุดต่อ terminal clamp/pad : รอยอาร์ค":
                    abnor_name ="70"

                if  abnor_name =="ชุดตัดอาร์ค หนวดกุ้ง : ชำรุด":
                    abnor_name ="71"

                if  abnor_name =="ชุดดับอาร์ค : ชำรุด":
                    abnor_name ="72"

                if  abnor_name =="อื่นๆ":
                    abnor_name ="73"


                # เปลี่ยนชื่อรูปภาพ
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


              

                job_picture = "https://objectstorage.ap-tokyo-1.oraclecloud.com/p/dI47BfTpwxXJODPhiO1p2wmYqyL0M-6b4TqRxU1ETcPDVFSjOC9sjXxPi9W-NomC/n/peacloud/b/Aidea/o/{}".format(f_image.name)

                nameimageold = filename
                nameimagenew = f_image.name
                    ## save ข้อมูลลง ฐานข้อมูล 
                    
                img = Image(job_officerid=job_officerid, eq_name=eq_name, subeq_name=subeq_name, abnor_name=abnor_name, vol_name=vol_name, abnor_other=abnor_other, nameimageold=nameimageold, nameimagenew=nameimagenew, pathimage=pathimage, job_picture=job_picture, image = f_image)
                img.save()

                #path_fileแบบไม่ต้องพิมเอง
                path_file = os.path.join(os.getcwd(), "media", f_image.name)
                print(path_file)

                  # UP image cload
                with open(path_file, 'rb') as payload:
                    headers = {
                    'Content-Type': 'image/jpg'
                    }
                    path_file = f_image.name

                    url = "https://objectstorage.ap-tokyo-1.oraclecloud.com/p/dI47BfTpwxXJODPhiO1p2wmYqyL0M-6b4TqRxU1ETcPDVFSjOC9sjXxPi9W-NomC/n/peacloud/b/Aidea/o/" + path_file


                    response = requests.request("PUT", url, headers=headers, data=payload)
                    print(response.text)
                
                    
                context={'data':{' job_officerid':job_officerid, 'eq_name':eq_name, 'subeq_name':subeq_name, 'abnor_name':abnor_name, 'vol_name':vol_name, 'pathimage':pathimage, 'job_picture':job_picture}}
                ## save ข้อมูลลง ฐานข้อมูล 

    if request.method == 'POST':
        print(request.POST)
        # รหัสพนักงาน
        job_officerid = request.POST['Partner']
        # ระดับแรงดัน
        vol_name = request.POST['subject1']
        # ชนิดอุปกรณ์
        eq_name = request.POST['subject2']
        # ประเภทอุปกรณ์
        subeq_name = request.POST['topic2']
        # สาเหตุการชำรุด
        abnor_name = request.POST.getlist('chapter2[]')
        abnor_other = request.POST['other2']
        f_image = request.FILES['image']

        # abnor_name = ",".join(abnor_name)
        # print(abnor_name)
        # checklist nodata 
        if  job_officerid == "":
            job_officerid = "-"
        
        if  vol_name == " ":
            vol_name = "-"

        if  eq_name == " ":
            eq_name = "-"

        if  subeq_name == " ":
            subeq_name = "-"
                
        if  abnor_name == " ":
            abnor_name = "-"
            
        if  abnor_other == "":
            abnor_other = "-"

        # print('chapter[]')
        for i in abnor_name:
            abnor_name = i
            print(abnor_name)
            

             

        # abnor_name = "บิ่น,แตก,บิดงอ,เสียรูป"

            

            print(type(f_image))
            print(f_image)
            print(vol_name)
            print(abnor_name)
            
            # กรณี 1สาเหตุ
            if abnor_name =="สภาพปกติ" or abnor_name =="บิ่น,แตก" or abnor_name =="ฉีกขาด" or abnor_name =="บิดงอ,เสียรูป" or abnor_name =="เป็นสนิม" or abnor_name =="เปลี่ยนสี" or abnor_name =="รอยอาร์ค" or abnor_name =="ผิวสกปรก" or abnor_name =="หลวม,หลุด" or abnor_name =="ก้านเป็นสนิม" or abnor_name =="bolt/nut หลวม,หลุด" or abnor_name =="bolt/nut เปลี่ยนสี,เป็นสนิม" or abnor_name =="bond wire หลุด,ขาด" or abnor_name =="จุดต่อที่OHGW : หลวม,หลุด" or abnor_name =="จุดต่อที่OHGW : เปลี่ยนสี" or abnor_name =="จุดต่อที่OHGW : รอยอาร์ค" or abnor_name =="จุดต่อที่OHGW : เป็นสนิม" or abnor_name =="จุดต่อที่หัวเสา : หลวม,หลุด" or abnor_name =="จุดต่อที่หัวเสา : เปลี่ยนสี" or abnor_name =="จุดต่อที่หัวเสา : รอยอาร์ค" or abnor_name =="จุดต่อที่หัวเสา : เป็นสนิม" or abnor_name =="สายขาด" or abnor_name =="รอยแตก,ขาด" or abnor_name =="หลุดจากลูกถ้วย" or abnor_name =="หลุดจากลูกถ้วย/สเปเซอร์" or abnor_name =="ลูกถ้วยซับพอร์ต : เป็นสนิม" or abnor_name =="ลูกถ้วยซับพอร์ต : หลวม,หลุด" or abnor_name =="ลูกถ้วยซับพอร์ต : บิ่น,แตก" or abnor_name =="ลูกถ้วยซับพอร์ต : เปลี่ยนสี" or abnor_name =="ลูกถ้วยซับพอร์ต : รอยอาร์ค" or abnor_name =="ลูกถ้วยซับพอร์ต : ผิวสกปรก" or abnor_name =="จุดต่อ terminal clamp/หางปลา : หลวม,หลุด" or abnor_name =="จุดต่อ terminal clamp/หางปลา : เป็นสนิม" or abnor_name =="จุดต่อ terminal clamp/หางปลา : รอยอาร์ค" or abnor_name =="ลูกถ้วย : บิ่น,แตก" or abnor_name =="ลูกถ้วย : เปลี่ยนสี" or abnor_name =="ลูกถ้วย : รอยอาร์ค" or abnor_name =="ลูกถ้วย : ผิวสกปรก" or abnor_name =="จุดต่อ terminal clamp : หลวม,หลุด" or abnor_name =="จุดต่อ terminal clamp : เป็นสนิม" or abnor_name =="จุดต่อ terminal clamp : รอยอาร์ค" or abnor_name =="Bracket : เป็นสนิม" or abnor_name =="Bracket : หลวม,หลุด" or abnor_name =="บุชชิ่ง : บิ่น,แตก" or abnor_name =="บุชชิ่ง : เปลี่ยนสี" or abnor_name =="บุชชิ่ง : รอยอาร์ค" or abnor_name =="บุชชิ่ง : ผิวสกปรก" or abnor_name =="บุชชิ่ง :  หลวม,หลุด" or abnor_name =="ตัวถัง : เป็นสนิม" or abnor_name =="ตัวถัง : น้ำมันรั่ว" or abnor_name =="สายลีด : หลวม,หลุด" or abnor_name =="สายต่อลงดิน : รอยอาร์ค" or abnor_name =="สายต่อลงดิน : หลวม,หลุด" or abnor_name =="ครีบ : บิ่น,แตก" or abnor_name =="ครีบ : เปลี่ยนสี" or abnor_name =="ครีบ : รอยอาร์ค" or abnor_name =="ครีบ : ผิวสกปรก" or abnor_name =="ครีบ : ฉีกขาด" or abnor_name =="ชุดแขวนคาปา (Hanger) ชำรุด" or abnor_name =="ชุด interrupt : ชำรุด" or abnor_name =="จุดต่อ terminal : หลวม,หลุด" or abnor_name =="จุดต่อ terminal : เป็นสนิม" or abnor_name =="จุดต่อ terminal : รอยอาร์ค" or abnor_name =="ไม้แป้น : ชำรุด" or abnor_name =="จุดต่อOHGW/OPGW : หลวม,หลุด" or abnor_name =="จุดต่อOHGW/OPGW : เปลี่ยนสี" or abnor_name =="จุดต่อOHGW/OPGW : รอยอาร์ค" or abnor_name =="จุดต่อOHGW/OPGW : เป็นสนิม" or abnor_name =="จุดต่อที่ GROUND PLATE : หลวม,หลุด" or abnor_name =="จุดต่อ terminal clamp/pad : รอยอาร์ค" or abnor_name =="ชุดตัดอาร์ค หนวดกุ้ง : ชำรุด" or abnor_name =="ชุดดับอาร์ค : ชำรุด" or abnor_name =="อื่นๆ":
                    
                # ระดับแรงดัน 22KV,33KV,115KV
                if  vol_name == "22KV":
                    vol_name = "DA"

                if  vol_name == "33KV":
                    vol_name = "DB"

                if  vol_name == "115KV":
                    vol_name = "TA"


                # ประเภทอุปกรณ์
                if  eq_name == "เสา":
                    eq_name = "PO"

                if  eq_name == "ระบบต่อลงดิน OHGW" or eq_name == "ระบบต่อลงดินOHGW/OPGW":
                    eq_name = "GR"

                if  eq_name == "ลูกถ้วยระบบจำหน่าย" or eq_name == "ลูกถ้วยระบบสายส่ง":
                    eq_name = "IN"

                if  eq_name == "สายไฟระบบจำหน่าย และอุปกรณ์จับสาย" or eq_name == "สายไฟระบบสายส่ง และอุปกรณ์จับสาย":
                    eq_name = "CO"

                if  eq_name == "จุดต่อในระบบจำหน่าย" or eq_name == "จุดต่อในระบบสายส่ง":
                    eq_name = "JO"

                if  eq_name == "อุปกรณ์ป้องกันและตัดตอน":
                    eq_name = "SW"

                
                if  eq_name == "กับดักเสิร์จ":
                    eq_name = "AR"

                if  eq_name == "คาปาซิเตอร์":
                    eq_name = "CA"

                if  eq_name == "CT/VT":
                    eq_name = "CV"
            
                print("-----------------------")
                print(vol_name)
                print(eq_name)
                print(subeq_name)
                print("-----------------------")
                # ชนิดอุปกรณ์
                    #ชุดแรงดันที่ รหัสไม่ตรงกัน
                if  vol_name == "DA" and eq_name == "JO" and subeq_name == "t-clamp (แคล้มป์มือเสือ)":
                    subeq_name = "3A"

                if  vol_name == "DB" and eq_name == "JO" and subeq_name == "t-clamp (แคล้มป์มือเสือ)":
                    subeq_name = "3A"

                if  vol_name == "TA" and eq_name == "JO" and subeq_name == "t-clamp (แคล้มป์มือเสือ)":
                    subeq_name = "2A"

                if  vol_name == "DA" and eq_name == "JO" and subeq_name == "หางปลา":
                    subeq_name = "4A"

                if  vol_name == "DB" and eq_name == "JO" and subeq_name == "หางปลา":
                    subeq_name = "4A"

                if  vol_name == "TA" and eq_name == "JO" and subeq_name == "หางปลา":
                    subeq_name = "3A"

                    #ชุดแรงดันที่ รหัสตรงกัน
                if  subeq_name == "เสาคอนกรีต" or subeq_name == "สาย OHGW" or subeq_name == "ลูกถ้วยกระเบื้อง : ชนิด Pin Type" or subeq_name == "สายเปลือย" or subeq_name == "หลอดต่อสาย" or subeq_name == "recloser" or subeq_name == "กับดักเสิร์จกระเบื้อง : สายลีดเข้าหัวกับดักเสิร์จ" or subeq_name == "กับดักเสิร์จกระเบื้อง : สายลีดเข้าหัวกับดักเสิร์จ" or subeq_name == "fix capacitor" or subeq_name == "VT" or subeq_name == "สาย OHGW/OPGW" or subeq_name == "ลูกถ้วยกระเบื้อง" or subeq_name == "circuit switcher":
                    subeq_name = "0A"

                if  subeq_name == "เสาโครงเหล็ก" or subeq_name == "เหล็กรองรับสาย OHGW" or subeq_name == "ลูกถ้วยคอมโพสิท" or subeq_name == "สายหุ้มฉนวน" or subeq_name == "pg clamp" or subeq_name == "load break switch (SF6 )" or subeq_name == "กับดักเสิร์จคอมโพสิท" or subeq_name == "switching capacitor" or subeq_name == "VT" or subeq_name == "เหล็กรองรับสาย OHGW/OPGW" or subeq_name == "preform armorod" or subeq_name =="t-slip":
                    subeq_name = "1A"

                if  subeq_name == "คอนคอนกรีต" or subeq_name == "สาย GROUND" or subeq_name == "ลูกถ้วยแก้วเหนียว" or subeq_name == "tie wire" or subeq_name == "belt clamp,hotline clamp" or subeq_name == "air break switch":
                    subeq_name = "2A"

                if  subeq_name == "จุดต่อระบบต่อลงดิน" or subeq_name == "สเปเซอร์กระเบื้อง" or subeq_name == "disconnecting switch":
                    subeq_name = "3A"

                if  subeq_name == "ลูกถ้วยกระเบื้อง : ชนิด Line Post":
                    subeq_name = "0B"
                
                if  subeq_name == "preform armogrip":
                    subeq_name = "1B"
                
                if  subeq_name == "คอนเหล็ก" or subeq_name == "cover tie wire":
                    subeq_name = "2B"

                if  subeq_name == "ลูกถ้วยกระเบื้อง : ชนิด Pin Post":
                    subeq_name = "0C"

                if  subeq_name == "ลูกถ้วยกระเบื้อง : ชนิด ลูกถ้วยแขวน":
                    subeq_name = "0D"

                if  subeq_name == "snap tie":
                    subeq_name = "2C"

                if  subeq_name == "pin terminal":
                    subeq_name = "5A"

                if  subeq_name == "ดรอปเอ้า ฟิวส์ คัทเอ้าท์":
                    subeq_name = "4A"
                
                if  subeq_name == "preform แยกสาย":
                    subeq_name = "1C"
                
                if  subeq_name == "strain clamp":
                    subeq_name = "1D"

                if  subeq_name == "suspension clamp":
                    subeq_name = "1E"

                # สาเหตุการชำรุด
                if  abnor_name =="สภาพปกติ":
                    abnor_name ="01"

                if  abnor_name =="บิ่น,แตก":
                    abnor_name ="02"

                if  abnor_name =="ฉีกขาด":
                    abnor_name ="03"

                if  abnor_name =="บิดงอ,เสียรูป":
                    abnor_name ="04"
                    
                if  abnor_name =="เป็นสนิม":
                    abnor_name ="05"

                if  abnor_name =="เปลี่ยนสี":
                    abnor_name ="06"

                if  abnor_name =="รอยอาร์ค":
                    abnor_name ="07"

                if  abnor_name =="ผิวสกปรก":
                    abnor_name ="08"

                if  abnor_name =="หลวม,หลุด":
                    abnor_name ="09"

                if  abnor_name =="ก้านเป็นสนิม":
                    abnor_name ="10"

                if  abnor_name =="bolt/nut หลวม,หลุด":
                    abnor_name ="11"

                if  abnor_name =="bolt/nut เปลี่ยนสี,เป็นสนิม":
                    abnor_name ="12"

                if  abnor_name =="bond wire หลุด,ขาด":
                    abnor_name ="13"

                if  abnor_name =="จุดต่อที่OHGW : หลวม,หลุด":
                    abnor_name ="14"

                if  abnor_name =="จุดต่อที่OHGW : เปลี่ยนสี":
                    abnor_name ="15"

                if  abnor_name =="จุดต่อที่OHGW : รอยอาร์ค":
                    abnor_name ="16"

                if  abnor_name =="จุดต่อที่OHGW : เป็นสนิม":
                    abnor_name ="17"

                if  abnor_name =="จุดต่อที่หัวเสา : หลวม,หลุด":
                    abnor_name ="18"

                if  abnor_name =="จุดต่อที่หัวเสา : เปลี่ยนสี":
                    abnor_name ="19"

                if  abnor_name =="จุดต่อที่หัวเสา : รอยอาร์ค":
                    abnor_name ="20"
                    
                if  abnor_name =="จุดต่อที่หัวเสา : เป็นสนิม":
                    abnor_name ="21"

                if  abnor_name =="สายขาด":
                    abnor_name ="22"

                if  abnor_name =="รอยแตก,ขาด":
                    abnor_name ="23"

                if  abnor_name =="หลุดจากลูกถ้วย":
                    abnor_name ="24"

                if  abnor_name =="หลุดจากลูกถ้วย/สเปเซอร์":
                    abnor_name ="25"

                if  abnor_name =="ลูกถ้วยซับพอร์ต : เป็นสนิม":
                    abnor_name ="26"

                if  abnor_name =="ลูกถ้วยซับพอร์ต : หลวม,หลุด":
                    abnor_name ="27"

                if  abnor_name =="ลูกถ้วยซับพอร์ต : บิ่น,แตก":
                    abnor_name ="28"

                if  abnor_name =="ลูกถ้วยซับพอร์ต : เปลี่ยนสี":
                    abnor_name ="29"

                if  abnor_name =="ลูกถ้วยซับพอร์ต : รอยอาร์ค":
                    abnor_name ="30"

                if  abnor_name =="ลูกถ้วยซับพอร์ต : ผิวสกปรก":
                    abnor_name ="31"

                if  abnor_name =="จุดต่อ terminal clamp/หางปลา : หลวม,หลุด":
                    abnor_name ="32"

                if  abnor_name =="จุดต่อ terminal clamp/หางปลา : เป็นสนิม":
                    abnor_name ="33"

                if  abnor_name =="จุดต่อ terminal clamp/หางปลา : รอยอาร์ค":
                    abnor_name ="34"
                    
                if  abnor_name =="ลูกถ้วย : บิ่น,แตก":
                    abnor_name ="35"

                if  abnor_name =="ลูกถ้วย : เปลี่ยนสี":
                    abnor_name ="36"

                if  abnor_name =="ลูกถ้วย : รอยอาร์ค":
                    abnor_name ="37"

                if  abnor_name =="ลูกถ้วย : ผิวสกปรก":
                    abnor_name ="38"

                if  abnor_name =="จุดต่อ terminal clamp : หลวม,หลุด":
                    abnor_name ="39"

                if  abnor_name =="จุดต่อ terminal clamp : เป็นสนิม":
                    abnor_name ="40"

                if  abnor_name =="จุดต่อ terminal clamp : รอยอาร์ค":
                    abnor_name ="41"

                if  abnor_name =="Bracket : เป็นสนิม":
                    abnor_name ="42"

                if  abnor_name =="Bracket : หลวม,หลุด":
                    abnor_name ="43"

                if  abnor_name =="บุชชิ่ง : บิ่น,แตก":
                    abnor_name ="44"

                if  abnor_name =="บุชชิ่ง : เปลี่ยนสี":
                    abnor_name ="45"

                if  abnor_name =="บุชชิ่ง : รอยอาร์ค":
                    abnor_name ="46"

                if  abnor_name =="บุชชิ่ง : ผิวสกปรก":
                    abnor_name ="47"

                if  abnor_name =="บุชชิ่ง :  หลวม,หลุด":
                    abnor_name ="48"
                    
                if  abnor_name =="ตัวถัง : เป็นสนิม":
                    abnor_name ="49"

                if  abnor_name =="ตัวถัง : น้ำมันรั่ว":
                    abnor_name ="50"

                if  abnor_name =="สายลีด : หลวม,หลุด":
                    abnor_name ="51"

                if  abnor_name =="สายต่อลงดิน : รอยอาร์ค":
                    abnor_name ="52"

                if  abnor_name =="สายต่อลงดิน : หลวม,หลุด":
                    abnor_name ="53"

                if  abnor_name =="ครีบ : บิ่น,แตก":
                    abnor_name ="54"

                if  abnor_name =="ครีบ : เปลี่ยนสี":
                    abnor_name ="55"

                if  abnor_name =="ครีบ : รอยอาร์ค":
                    abnor_name ="56"

                if  abnor_name =="ครีบ : ผิวสกปรก":
                    abnor_name ="57"

                if  abnor_name =="ครีบ : ฉีกขาด":
                    abnor_name ="58"

                if  abnor_name =="ชุดแขวนคาปา (Hanger) ชำรุด":
                    abnor_name ="59"

                if  abnor_name =="ชุด interrupt : ชำรุด":
                    abnor_name ="60"

                if  abnor_name =="จุดต่อ terminal : หลวม,หลุด":
                    abnor_name ="61"

                if  abnor_name =="จุดต่อ terminal : เป็นสนิม":
                    abnor_name ="62"
                    
                if  abnor_name =="จุดต่อ terminal : รอยอาร์ค":
                    abnor_name ="63"

                if  abnor_name =="ไม้แป้น : ชำรุด":
                    abnor_name ="64"

                if  abnor_name =="จุดต่อOHGW/OPGW : หลวม,หลุด":
                    abnor_name ="65"

                if  abnor_name =="จุดต่อOHGW/OPGW : เปลี่ยนสี":
                    abnor_name ="66"

                if  abnor_name =="จุดต่อOHGW/OPGW : รอยอาร์ค":
                    abnor_name ="67"

                if  abnor_name =="จุดต่อOHGW/OPGW : เป็นสนิม":
                    abnor_name ="68"

                if  abnor_name =="จุดต่อที่ GROUND PLATE : หลวม,หลุด":
                    abnor_name ="69"

                if  abnor_name =="จุดต่อ terminal clamp/pad : รอยอาร์ค":
                    abnor_name ="70"

                if  abnor_name =="ชุดตัดอาร์ค หนวดกุ้ง : ชำรุด":
                    abnor_name ="71"

                if  abnor_name =="ชุดดับอาร์ค : ชำรุด":
                    abnor_name ="72"

                if  abnor_name =="อื่นๆ":
                    abnor_name ="73"


                # เปลี่ยนชื่อรูปภาพ
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


              

                job_picture = "https://objectstorage.ap-tokyo-1.oraclecloud.com/p/dI47BfTpwxXJODPhiO1p2wmYqyL0M-6b4TqRxU1ETcPDVFSjOC9sjXxPi9W-NomC/n/peacloud/b/Aidea/o/{}".format(f_image.name)

                nameimageold = filename
                nameimagenew = f_image.name
                    ## save ข้อมูลลง ฐานข้อมูล 
                    
                img = Image(job_officerid=job_officerid, eq_name=eq_name, subeq_name=subeq_name, abnor_name=abnor_name, vol_name=vol_name, abnor_other=abnor_other, nameimageold=nameimageold, nameimagenew=nameimagenew, pathimage=pathimage, job_picture=job_picture, image = f_image)
                img.save()

                #path_fileแบบไม่ต้องพิมเอง
                path_file = os.path.join(os.getcwd(), "media", f_image.name)
                print(path_file)

                  # UP image cload
                with open(path_file, 'rb') as payload:
                    headers = {
                    'Content-Type': 'image/jpg'
                    }
                    path_file = f_image.name

                    url = "https://objectstorage.ap-tokyo-1.oraclecloud.com/p/dI47BfTpwxXJODPhiO1p2wmYqyL0M-6b4TqRxU1ETcPDVFSjOC9sjXxPi9W-NomC/n/peacloud/b/Aidea/o/" + path_file


                    response = requests.request("PUT", url, headers=headers, data=payload)
                    print(response.text)
                
                    
                context={'data':{' job_officerid':job_officerid, 'eq_name':eq_name, 'subeq_name':subeq_name, 'abnor_name':abnor_name, 'vol_name':vol_name, 'pathimage':pathimage, 'job_picture':job_picture}}
                ## save ข้อมูลลง ฐานข้อมูล 

# --------------------------------------------------------------------------------------------------------------------------

#         # อุปกรณ์ที่ 1 หลายสาเหตุ เสา
#         if  vol_name == "22KV" and eq_name == "เสา" and subeq_name == "เสาคอนกรีต" and abnor_name =="บิ่น,แตก,บิดงอ,เสียรูป":
#             vol_name = "DA"
#             eq_name = "PO"
#             subeq_name = "0A"
#             abnor_name ="02"

#             filename = request.FILES['image'].name
#             f = os.path.splitext(filename)
#             n = f[0]
#             ext = f[1]
#             #timedate & time in Python

#             timestr = time.strftime("%Y%m%d-%H%M%S")


#             f_image.name = "{}_{}_{}_{}_{}_{}{}".format(job_officerid, vol_name, eq_name, subeq_name, abnor_name, timestr, ext)
#             print(f_image.name)


#             #past image
#             pathimage = "/media/{}".format(f_image.name) 
#             print(pathimage)


#             # UP image cload
#             uploaded_file = request.FILES['image']
#             print(uploaded_file)
#             payload=uploaded_file
#             headers = {
#             'Content-Type': 'image/jpg'
#             }
#             path_file = f_image.name

#             url = "https://objectstorage.ap-tokyo-1.oraclecloud.com/p/dI47BfTpwxXJODPhiO1p2wmYqyL0M-6b4TqRxU1ETcPDVFSjOC9sjXxPi9W-NomC/n/peacloud/b/Aidea/o/" + path_file


#             response = requests.request("PUT", url, headers=headers, data=payload)

#             job_picture = "https://objectstorage.ap-tokyo-1.oraclecloud.com/p/dI47BfTpwxXJODPhiO1p2wmYqyL0M-6b4TqRxU1ETcPDVFSjOC9sjXxPi9W-NomC/n/peacloud/b/Aidea/o/{}".format(f_image.name)

#             nameimageold = filename
#             nameimagenew = f_image.name
#             ## save ข้อมูลลง ฐานข้อมูล 
                
#             img = Image(job_officerid=job_officerid, eq_name=eq_name, subeq_name=subeq_name, abnor_name=abnor_name, vol_name=vol_name, abnor_other=abnor_other, nameimageold=nameimageold, nameimagenew=nameimagenew, pathimage=pathimage, job_picture=job_picture, image = f_image)
#             img.save()
                
#             context={'data':{' job_officerid':job_officerid, 'eq_name':eq_name, 'subeq_name':subeq_name, 'abnor_name':abnor_name, 'vol_name':vol_name, 'pathimage':pathimage, 'job_picture':job_picture}}
#             ## save ข้อมูลลง ฐานข้อมูล 
            
#             vol_name = "DA"
#             eq_name = "PO"
#             subeq_name = "0A"
#             abnor_name ="04"

#             filename = request.FILES['image'].name
#             f = os.path.splitext(filename)
#             n = f[0]
#             ext = f[1]
#             #timedate & time in Python

#             timestr = time.strftime("%Y%m%d-%H%M%S")


#             f_image.name = "{}_{}_{}_{}_{}_{}{}".format(job_officerid, vol_name, eq_name, subeq_name, abnor_name, timestr, ext)
#             print(f_image.name)


#             #past image
#             pathimage = "/media/{}".format(f_image.name) 
#             print(pathimage)


#             # UP image cload
#             uploaded_file = request.FILES['image']
#             print(uploaded_file)
#             payload=uploaded_file
#             headers = {
#             'Content-Type': 'image/jpg'
#             }
#             path_file = f_image.name

#             url = "https://objectstorage.ap-tokyo-1.oraclecloud.com/p/dI47BfTpwxXJODPhiO1p2wmYqyL0M-6b4TqRxU1ETcPDVFSjOC9sjXxPi9W-NomC/n/peacloud/b/Aidea/o/" + path_file


#             response = requests.request("PUT", url, headers=headers, data=payload)

#             job_picture = "https://objectstorage.ap-tokyo-1.oraclecloud.com/p/dI47BfTpwxXJODPhiO1p2wmYqyL0M-6b4TqRxU1ETcPDVFSjOC9sjXxPi9W-NomC/n/peacloud/b/Aidea/o/{}".format(f_image.name)

#             nameimageold = filename
#             nameimagenew = f_image.name
#             ## save ข้อมูลลง ฐานข้อมูล 
                
#             img = Image(job_officerid=job_officerid, eq_name=eq_name, subeq_name=subeq_name, abnor_name=abnor_name, vol_name=vol_name, abnor_other=abnor_other, nameimageold=nameimageold, nameimagenew=nameimagenew, pathimage=pathimage, job_picture=job_picture, image = f_image)
#             img.save()
                
#             context={'data':{' job_officerid':job_officerid, 'eq_name':eq_name, 'subeq_name':subeq_name, 'abnor_name':abnor_name, 'vol_name':vol_name, 'pathimage':pathimage, 'job_picture':job_picture}}
#             ## save ข้อมูลลง ฐานข้อมูล 
        

#         #2สาเหตุใช้รูปเดียว
#         if  vol_name == "22KV" and eq_name == "เสา" and subeq_name == "เสาคอนกรีต" and abnor_name =="บิ่น,แตก,อื่่นๆ":
#             vol_name = "DA"
#             eq_name = "PO"
#             subeq_name = "0A"
#             abnor_name ="73"
            

#             filename = request.FILES['image'].name
#             f = os.path.splitext(filename)
#             n = f[0]
#             ext = f[1]
#             #timedate & time in Python

#             timestr = time.strftime("%Y%m%d-%H%M%S")


#             f_image.name = "{}_{}_{}_{}_{}_{}{}".format(job_officerid, vol_name, eq_name, subeq_name, abnor_name, timestr, ext)
#             print(f_image.name)


#             #past image
#             pathimage = "/media/{}".format(f_image.name) 
#             print(pathimage)


#             # UP image cload
#             uploaded_file = request.FILES['image']
#             print(uploaded_file)
#             payload=uploaded_file
#             headers = {
#             'Content-Type': 'image/jpg'
#             }
#             path_file = f_image.name

#             url = "https://objectstorage.ap-tokyo-1.oraclecloud.com/p/dI47BfTpwxXJODPhiO1p2wmYqyL0M-6b4TqRxU1ETcPDVFSjOC9sjXxPi9W-NomC/n/peacloud/b/Aidea/o/" + path_file


#             response = requests.request("PUT", url, headers=headers, data=payload)

#             job_picture = "https://objectstorage.ap-tokyo-1.oraclecloud.com/p/dI47BfTpwxXJODPhiO1p2wmYqyL0M-6b4TqRxU1ETcPDVFSjOC9sjXxPi9W-NomC/n/peacloud/b/Aidea/o/{}".format(f_image.name)

#             nameimageold = filename
#             nameimagenew = f_image.name
#                 ## save ข้อมูลลง ฐานข้อมูล 
                
#             img = Image(job_officerid=job_officerid, eq_name=eq_name, subeq_name=subeq_name, abnor_name=abnor_name, vol_name=vol_name, abnor_other=abnor_other, nameimageold=nameimageold, nameimagenew=nameimagenew, pathimage=pathimage, job_picture=job_picture)
#             img.save()
                
#             context={'data':{' job_officerid':job_officerid, 'eq_name':eq_name, 'subeq_name':subeq_name, 'abnor_name':abnor_name, 'vol_name':vol_name, 'pathimage':pathimage, 'job_picture':job_picture}}
#             ## save ข้อมูลลง ฐานข้อมูล 

#             pathimage = "/media/{}".format(f_image.name) 
#             vol_name = "DA"
#             eq_name = "PO"
#             subeq_name = "0A"
#             abnor_name ="02"
#             abnor_other = "-"

#             img = Image(job_officerid=job_officerid, eq_name=eq_name, subeq_name=subeq_name, abnor_name=abnor_name, vol_name=vol_name, abnor_other=abnor_other, nameimageold=nameimageold, nameimagenew=nameimagenew, pathimage=pathimage, job_picture=job_picture)
#             img.save()
                
#             context={'data':{' job_officerid':job_officerid, 'eq_name':eq_name, 'subeq_name':subeq_name, 'abnor_name':abnor_name, 'vol_name':vol_name, 'pathimage':pathimage, 'job_picture':job_picture}}
#             ## save ข้อมูลลง ฐานข้อมูล 




#         if  vol_name == "22KV" and eq_name == "เสา" and subeq_name == "เสาคอนกรีต" and abnor_name =="บิดงอ,เสียรูป,อื่่นๆ":
#             vol_name = "DA"
#             eq_name = "PO"
#             subeq_name = "0A"
#             abnor_name ="73"
            

#             filename = request.FILES['image'].name
#             f = os.path.splitext(filename)
#             n = f[0]
#             ext = f[1]
#             #timedate & time in Python

#             timestr = time.strftime("%Y%m%d-%H%M%S")


#             f_image.name = "{}_{}_{}_{}_{}_{}{}".format(job_officerid, vol_name, eq_name, subeq_name, abnor_name, timestr, ext)
#             print(f_image.name)


#             #past image
#             pathimage = "/media/{}".format(f_image.name) 
#             print(pathimage)


#             # UP image cload
#             uploaded_file = request.FILES['image']
#             print(uploaded_file)
#             payload=uploaded_file
#             headers = {
#             'Content-Type': 'image/jpg'
#             }
#             path_file = f_image.name

#             url = "https://objectstorage.ap-tokyo-1.oraclecloud.com/p/dI47BfTpwxXJODPhiO1p2wmYqyL0M-6b4TqRxU1ETcPDVFSjOC9sjXxPi9W-NomC/n/peacloud/b/Aidea/o/" + path_file


#             response = requests.request("PUT", url, headers=headers, data=payload)

#             job_picture = "https://objectstorage.ap-tokyo-1.oraclecloud.com/p/dI47BfTpwxXJODPhiO1p2wmYqyL0M-6b4TqRxU1ETcPDVFSjOC9sjXxPi9W-NomC/n/peacloud/b/Aidea/o/{}".format(f_image.name)

#             nameimageold = filename
#             nameimagenew = f_image.name
#                 ## save ข้อมูลลง ฐานข้อมูล 
                
#             img = Image(job_officerid=job_officerid, eq_name=eq_name, subeq_name=subeq_name, abnor_name=abnor_name, vol_name=vol_name, abnor_other=abnor_other, nameimageold=nameimageold, nameimagenew=nameimagenew, pathimage=pathimage, job_picture=job_picture)
#             img.save()
                
#             context={'data':{' job_officerid':job_officerid, 'eq_name':eq_name, 'subeq_name':subeq_name, 'abnor_name':abnor_name, 'vol_name':vol_name, 'pathimage':pathimage, 'job_picture':job_picture}}
#             ## save ข้อมูลลง ฐานข้อมูล 

#             pathimage = "/media/{}".format(f_image.name) 
#             vol_name = "DA"
#             eq_name = "PO"
#             subeq_name = "0A"
#             abnor_name ="04"
#             abnor_other = "-"

#             img = Image(job_officerid=job_officerid, eq_name=eq_name, subeq_name=subeq_name, abnor_name=abnor_name, vol_name=vol_name, abnor_other=abnor_other, nameimageold=nameimageold, nameimagenew=nameimagenew, pathimage=pathimage, job_picture=job_picture)
#             img.save()
                
#             context={'data':{' job_officerid':job_officerid, 'eq_name':eq_name, 'subeq_name':subeq_name, 'abnor_name':abnor_name, 'vol_name':vol_name, 'pathimage':pathimage, 'job_picture':job_picture}}
#             ## save ข้อมูลลง ฐานข้อมูล 



# # ----------------------------------------------------------------

# # อุปกรณ์ที่ 1 หลายสาเหตุ เสาโครงเหล็ก
#         if  vol_name == "22KV" and eq_name == "เสา" and subeq_name == "เสาโครงเหล็ก" and abnor_name =="บิ่น,แตก,บิดงอ,เสียรูป":
#             vol_name = "DA"
#             eq_name = "PO"
#             subeq_name = "1A"
#             abnor_name ="02"

#             filename = request.FILES['image'].name
#             f = os.path.splitext(filename)
#             n = f[0]
#             ext = f[1]
#             #timedate & time in Python

#             timestr = time.strftime("%Y%m%d-%H%M%S")


#             f_image.name = "{}_{}_{}_{}_{}_{}{}".format(job_officerid, vol_name, eq_name, subeq_name, abnor_name, timestr, ext)
#             print(f_image.name)


#             #past image
#             pathimage = "/media/{}".format(f_image.name) 
#             print(pathimage)


#             # UP image cload
#             uploaded_file = request.FILES['image']
#             print(uploaded_file)
#             payload=uploaded_file
#             headers = {
#             'Content-Type': 'image/jpg'
#             }
#             path_file = f_image.name

#             url = "https://objectstorage.ap-tokyo-1.oraclecloud.com/p/dI47BfTpwxXJODPhiO1p2wmYqyL0M-6b4TqRxU1ETcPDVFSjOC9sjXxPi9W-NomC/n/peacloud/b/Aidea/o/" + path_file


#             response = requests.request("PUT", url, headers=headers, data=payload)

#             job_picture = "https://objectstorage.ap-tokyo-1.oraclecloud.com/p/dI47BfTpwxXJODPhiO1p2wmYqyL0M-6b4TqRxU1ETcPDVFSjOC9sjXxPi9W-NomC/n/peacloud/b/Aidea/o/{}".format(f_image.name)

#             nameimageold = filename
#             nameimagenew = f_image.name
#             ## save ข้อมูลลง ฐานข้อมูล 
                
#             img = Image(job_officerid=job_officerid, eq_name=eq_name, subeq_name=subeq_name, abnor_name=abnor_name, vol_name=vol_name, abnor_other=abnor_other, nameimageold=nameimageold, nameimagenew=nameimagenew, pathimage=pathimage, job_picture=job_picture)
#             img.save()
                
#             context={'data':{' job_officerid':job_officerid, 'eq_name':eq_name, 'subeq_name':subeq_name, 'abnor_name':abnor_name, 'vol_name':vol_name, 'pathimage':pathimage, 'job_picture':job_picture}}
#             ## save ข้อมูลลง ฐานข้อมูล 

#             pathimage = "/media/{}".format(f_image.name) 
#             vol_name = "DA"
#             eq_name = "PO"
#             subeq_name = "1A"
#             abnor_name ="04"

#             img = Image(job_officerid=job_officerid, eq_name=eq_name, subeq_name=subeq_name, abnor_name=abnor_name, vol_name=vol_name, abnor_other=abnor_other, nameimageold=nameimageold, nameimagenew=nameimagenew, pathimage=pathimage, job_picture=job_picture)
#             img.save()
                
#             context={'data':{' job_officerid':job_officerid, 'eq_name':eq_name, 'subeq_name':subeq_name, 'abnor_name':abnor_name, 'vol_name':vol_name, 'pathimage':pathimage, 'job_picture':job_picture}}
#                 ## save ข้อมูลลง ฐานข้อมูล 
            
        
#         if  vol_name == "22KV" and eq_name == "เสา" and subeq_name == "เสาโครงเหล็ก" and abnor_name =="บิ่น,แตก,อื่่นๆ":
#             vol_name = "DA"
#             eq_name = "PO"
#             subeq_name = "1A"
#             abnor_name ="73"
            

#             filename = request.FILES['image'].name
#             f = os.path.splitext(filename)
#             n = f[0]
#             ext = f[1]
#             #timedate & time in Python

#             timestr = time.strftime("%Y%m%d-%H%M%S")


#             f_image.name = "{}_{}_{}_{}_{}_{}{}".format(job_officerid, vol_name, eq_name, subeq_name, abnor_name, timestr, ext)
#             print(f_image.name)


#             #past image
#             pathimage = "/media/{}".format(f_image.name) 
#             print(pathimage)


#             # UP image cload
#             uploaded_file = request.FILES['image']
#             print(uploaded_file)
#             payload=uploaded_file
#             headers = {
#             'Content-Type': 'image/jpg'
#             }
#             path_file = f_image.name

#             url = "https://objectstorage.ap-tokyo-1.oraclecloud.com/p/dI47BfTpwxXJODPhiO1p2wmYqyL0M-6b4TqRxU1ETcPDVFSjOC9sjXxPi9W-NomC/n/peacloud/b/Aidea/o/" + path_file


#             response = requests.request("PUT", url, headers=headers, data=payload)

#             job_picture = "https://objectstorage.ap-tokyo-1.oraclecloud.com/p/dI47BfTpwxXJODPhiO1p2wmYqyL0M-6b4TqRxU1ETcPDVFSjOC9sjXxPi9W-NomC/n/peacloud/b/Aidea/o/{}".format(f_image.name)

#             nameimageold = filename
#             nameimagenew = f_image.name
#                 ## save ข้อมูลลง ฐานข้อมูล 
                
#             img = Image(job_officerid=job_officerid, eq_name=eq_name, subeq_name=subeq_name, abnor_name=abnor_name, vol_name=vol_name, abnor_other=abnor_other, nameimageold=nameimageold, nameimagenew=nameimagenew, pathimage=pathimage, job_picture=job_picture)
#             img.save()
                
#             context={'data':{' job_officerid':job_officerid, 'eq_name':eq_name, 'subeq_name':subeq_name, 'abnor_name':abnor_name, 'vol_name':vol_name, 'pathimage':pathimage, 'job_picture':job_picture}}
#             ## save ข้อมูลลง ฐานข้อมูล 

#             pathimage = "/media/{}".format(f_image.name) 
#             vol_name = "DA"
#             eq_name = "PO"
#             subeq_name = "1A"
#             abnor_name ="02"
#             abnor_other = "-"

#             img = Image(job_officerid=job_officerid, eq_name=eq_name, subeq_name=subeq_name, abnor_name=abnor_name, vol_name=vol_name, abnor_other=abnor_other, nameimageold=nameimageold, nameimagenew=nameimagenew, pathimage=pathimage, job_picture=job_picture)
#             img.save()
                
#             context={'data':{' job_officerid':job_officerid, 'eq_name':eq_name, 'subeq_name':subeq_name, 'abnor_name':abnor_name, 'vol_name':vol_name, 'pathimage':pathimage, 'job_picture':job_picture}}
#             ## save ข้อมูลลง ฐานข้อมูล 


#         if  vol_name == "22KV" and eq_name == "เสา" and subeq_name == "เสาโครงเหล็ก" and abnor_name =="บิดงอ,เสียรูป,อื่่นๆ":
#             vol_name = "DA"
#             eq_name = "PO"
#             subeq_name = "1A"
#             abnor_name ="73"
            

#             filename = request.FILES['image'].name
#             f = os.path.splitext(filename)
#             n = f[0]
#             ext = f[1]
#             #timedate & time in Python

#             timestr = time.strftime("%Y%m%d-%H%M%S")


#             f_image.name = "{}_{}_{}_{}_{}_{}{}".format(job_officerid, vol_name, eq_name, subeq_name, abnor_name, timestr, ext)
#             print(f_image.name)


#             #past image
#             pathimage = "/media/{}".format(f_image.name) 
#             print(pathimage)


#             # UP image cload
#             uploaded_file = request.FILES['image']
#             print(uploaded_file)
#             payload=uploaded_file
#             headers = {
#             'Content-Type': 'image/jpg'
#             }
#             path_file = f_image.name

#             url = "https://objectstorage.ap-tokyo-1.oraclecloud.com/p/dI47BfTpwxXJODPhiO1p2wmYqyL0M-6b4TqRxU1ETcPDVFSjOC9sjXxPi9W-NomC/n/peacloud/b/Aidea/o/" + path_file


#             response = requests.request("PUT", url, headers=headers, data=payload)

#             job_picture = "https://objectstorage.ap-tokyo-1.oraclecloud.com/p/dI47BfTpwxXJODPhiO1p2wmYqyL0M-6b4TqRxU1ETcPDVFSjOC9sjXxPi9W-NomC/n/peacloud/b/Aidea/o/{}".format(f_image.name)

#             nameimageold = filename
#             nameimagenew = f_image.name
#                 ## save ข้อมูลลง ฐานข้อมูล 
                
#             img = Image(job_officerid=job_officerid, eq_name=eq_name, subeq_name=subeq_name, abnor_name=abnor_name, vol_name=vol_name, abnor_other=abnor_other, nameimageold=nameimageold, nameimagenew=nameimagenew, pathimage=pathimage, job_picture=job_picture)
#             img.save()
                
#             context={'data':{' job_officerid':job_officerid, 'eq_name':eq_name, 'subeq_name':subeq_name, 'abnor_name':abnor_name, 'vol_name':vol_name, 'pathimage':pathimage, 'job_picture':job_picture}}
#             ## save ข้อมูลลง ฐานข้อมูล 

#             pathimage = "/media/{}".format(f_image.name) 
#             vol_name = "DA"
#             eq_name = "PO"
#             subeq_name = "1A"
#             abnor_name ="04"
#             abnor_other = "-"

#             img = Image(job_officerid=job_officerid, eq_name=eq_name, subeq_name=subeq_name, abnor_name=abnor_name, vol_name=vol_name, abnor_other=abnor_other, nameimageold=nameimageold, nameimagenew=nameimagenew, pathimage=pathimage, job_picture=job_picture)
#             img.save()
                
#             context={'data':{' job_officerid':job_officerid, 'eq_name':eq_name, 'subeq_name':subeq_name, 'abnor_name':abnor_name, 'vol_name':vol_name, 'pathimage':pathimage, 'job_picture':job_picture}}
#             ## save ข้อมูลลง ฐานข้อมูล 



# # ----------------------------------------------------------------

# # อุปกรณ์ที่ 1 หลายสาเหตุ คอนคอนกรีต
#         if  vol_name == "22KV" and eq_name == "เสา" and subeq_name == "คอนคอนกรีต" and abnor_name =="บิ่น,แตก,บิดงอ,เสียรูป":
#             vol_name = "DA"
#             eq_name = "PO"
#             subeq_name = "2A"
#             abnor_name ="02"

#             filename = request.FILES['image'].name
#             f = os.path.splitext(filename)
#             n = f[0]
#             ext = f[1]
#             #timedate & time in Python

#             timestr = time.strftime("%Y%m%d-%H%M%S")


#             f_image.name = "{}_{}_{}_{}_{}_{}{}".format(job_officerid, vol_name, eq_name, subeq_name, abnor_name, timestr, ext)
#             print(f_image.name)


#             #past image
#             pathimage = "/media/{}".format(f_image.name) 
#             print(pathimage)


#             # UP image cload
#             uploaded_file = request.FILES['image']
#             print(uploaded_file)
#             payload=uploaded_file
#             headers = {
#             'Content-Type': 'image/jpg'
#             }
#             path_file = f_image.name

#             url = "https://objectstorage.ap-tokyo-1.oraclecloud.com/p/dI47BfTpwxXJODPhiO1p2wmYqyL0M-6b4TqRxU1ETcPDVFSjOC9sjXxPi9W-NomC/n/peacloud/b/Aidea/o/" + path_file


#             response = requests.request("PUT", url, headers=headers, data=payload)

#             job_picture = "https://objectstorage.ap-tokyo-1.oraclecloud.com/p/dI47BfTpwxXJODPhiO1p2wmYqyL0M-6b4TqRxU1ETcPDVFSjOC9sjXxPi9W-NomC/n/peacloud/b/Aidea/o/{}".format(f_image.name)

#             nameimageold = filename
#             nameimagenew = f_image.name
#             ## save ข้อมูลลง ฐานข้อมูล 
                
#             img = Image(job_officerid=job_officerid, eq_name=eq_name, subeq_name=subeq_name, abnor_name=abnor_name, vol_name=vol_name, abnor_other=abnor_other, nameimageold=nameimageold, nameimagenew=nameimagenew, pathimage=pathimage, job_picture=job_picture)
#             img.save()
                
#             context={'data':{' job_officerid':job_officerid, 'eq_name':eq_name, 'subeq_name':subeq_name, 'abnor_name':abnor_name, 'vol_name':vol_name, 'pathimage':pathimage, 'job_picture':job_picture}}
#             ## save ข้อมูลลง ฐานข้อมูล 

#             pathimage = "/media/{}".format(f_image.name) 
#             vol_name = "DA"
#             eq_name = "PO"
#             subeq_name = "2A"
#             abnor_name ="04"

#             img = Image(job_officerid=job_officerid, eq_name=eq_name, subeq_name=subeq_name, abnor_name=abnor_name, vol_name=vol_name, abnor_other=abnor_other, nameimageold=nameimageold, nameimagenew=nameimagenew, pathimage=pathimage, job_picture=job_picture)
#             img.save()
                
#             context={'data':{' job_officerid':job_officerid, 'eq_name':eq_name, 'subeq_name':subeq_name, 'abnor_name':abnor_name, 'vol_name':vol_name, 'pathimage':pathimage, 'job_picture':job_picture}}
#                 ## save ข้อมูลลง ฐานข้อมูล 

#         if  vol_name == "22KV" and eq_name == "เสา" and subeq_name == "คอนคอนกรีต" and abnor_name =="บิ่น,แตก,bolt/nut หลวม,หลุด":
#             vol_name = "DA"
#             eq_name = "PO"
#             subeq_name = "2A"
#             abnor_name ="02"

#             filename = request.FILES['image'].name
#             f = os.path.splitext(filename)
#             n = f[0]
#             ext = f[1]
#             #timedate & time in Python

#             timestr = time.strftime("%Y%m%d-%H%M%S")


#             f_image.name = "{}_{}_{}_{}_{}_{}{}".format(job_officerid, vol_name, eq_name, subeq_name, abnor_name, timestr, ext)
#             print(f_image.name)


#             #past image
#             pathimage = "/media/{}".format(f_image.name) 
#             print(pathimage)


#             # UP image cload
#             uploaded_file = request.FILES['image']
#             print(uploaded_file)
#             payload=uploaded_file
#             headers = {
#             'Content-Type': 'image/jpg'
#             }
#             path_file = f_image.name

#             url = "https://objectstorage.ap-tokyo-1.oraclecloud.com/p/dI47BfTpwxXJODPhiO1p2wmYqyL0M-6b4TqRxU1ETcPDVFSjOC9sjXxPi9W-NomC/n/peacloud/b/Aidea/o/" + path_file


#             response = requests.request("PUT", url, headers=headers, data=payload)

#             job_picture = "https://objectstorage.ap-tokyo-1.oraclecloud.com/p/dI47BfTpwxXJODPhiO1p2wmYqyL0M-6b4TqRxU1ETcPDVFSjOC9sjXxPi9W-NomC/n/peacloud/b/Aidea/o/{}".format(f_image.name)

#             nameimageold = filename
#             nameimagenew = f_image.name
#             ## save ข้อมูลลง ฐานข้อมูล 
                
#             img = Image(job_officerid=job_officerid, eq_name=eq_name, subeq_name=subeq_name, abnor_name=abnor_name, vol_name=vol_name, abnor_other=abnor_other, nameimageold=nameimageold, nameimagenew=nameimagenew, pathimage=pathimage, job_picture=job_picture)
#             img.save()
                
#             context={'data':{' job_officerid':job_officerid, 'eq_name':eq_name, 'subeq_name':subeq_name, 'abnor_name':abnor_name, 'vol_name':vol_name, 'pathimage':pathimage, 'job_picture':job_picture}}
#             ## save ข้อมูลลง ฐานข้อมูล 

#             pathimage = "/media/{}".format(f_image.name) 
#             vol_name = "DA"
#             eq_name = "PO"
#             subeq_name = "2A"
#             abnor_name ="11"

#             img = Image(job_officerid=job_officerid, eq_name=eq_name, subeq_name=subeq_name, abnor_name=abnor_name, vol_name=vol_name, abnor_other=abnor_other, nameimageold=nameimageold, nameimagenew=nameimagenew, pathimage=pathimage, job_picture=job_picture)
#             img.save()
                
#             context={'data':{' job_officerid':job_officerid, 'eq_name':eq_name, 'subeq_name':subeq_name, 'abnor_name':abnor_name, 'vol_name':vol_name, 'pathimage':pathimage, 'job_picture':job_picture}}
#             ## save ข้อมูลลง ฐานข้อมูล           

#         if  vol_name == "22KV" and eq_name == "เสา" and subeq_name == "คอนคอนกรีต" and abnor_name =="บิ่น,แตก,bolt/nut เปลี่ยนสี,เป็นสนิม":
#             vol_name = "DA"
#             eq_name = "PO"
#             subeq_name = "2A"
#             abnor_name ="02"

#             filename = request.FILES['image'].name
#             f = os.path.splitext(filename)
#             n = f[0]
#             ext = f[1]
#             #timedate & time in Python

#             timestr = time.strftime("%Y%m%d-%H%M%S")


#             f_image.name = "{}_{}_{}_{}_{}_{}{}".format(job_officerid, vol_name, eq_name, subeq_name, abnor_name, timestr, ext)
#             print(f_image.name)


#             #past image
#             pathimage = "/media/{}".format(f_image.name) 
#             print(pathimage)


#             # UP image cload
#             uploaded_file = request.FILES['image']
#             print(uploaded_file)
#             payload=uploaded_file
#             headers = {
#             'Content-Type': 'image/jpg'
#             }
#             path_file = f_image.name

#             url = "https://objectstorage.ap-tokyo-1.oraclecloud.com/p/dI47BfTpwxXJODPhiO1p2wmYqyL0M-6b4TqRxU1ETcPDVFSjOC9sjXxPi9W-NomC/n/peacloud/b/Aidea/o/" + path_file


#             response = requests.request("PUT", url, headers=headers, data=payload)

#             job_picture = "https://objectstorage.ap-tokyo-1.oraclecloud.com/p/dI47BfTpwxXJODPhiO1p2wmYqyL0M-6b4TqRxU1ETcPDVFSjOC9sjXxPi9W-NomC/n/peacloud/b/Aidea/o/{}".format(f_image.name)

#             nameimageold = filename
#             nameimagenew = f_image.name
#             ## save ข้อมูลลง ฐานข้อมูล 
                
#             img = Image(job_officerid=job_officerid, eq_name=eq_name, subeq_name=subeq_name, abnor_name=abnor_name, vol_name=vol_name, abnor_other=abnor_other, nameimageold=nameimageold, nameimagenew=nameimagenew, pathimage=pathimage, job_picture=job_picture)
#             img.save()
                
#             context={'data':{' job_officerid':job_officerid, 'eq_name':eq_name, 'subeq_name':subeq_name, 'abnor_name':abnor_name, 'vol_name':vol_name, 'pathimage':pathimage, 'job_picture':job_picture}}
#             ## save ข้อมูลลง ฐานข้อมูล 

#             pathimage = "/media/{}".format(f_image.name) 
#             vol_name = "DA"
#             eq_name = "PO"
#             subeq_name = "2A"
#             abnor_name ="12"

#             img = Image(job_officerid=job_officerid, eq_name=eq_name, subeq_name=subeq_name, abnor_name=abnor_name, vol_name=vol_name, abnor_other=abnor_other, nameimageold=nameimageold, nameimagenew=nameimagenew, pathimage=pathimage, job_picture=job_picture)
#             img.save()
                
#             context={'data':{' job_officerid':job_officerid, 'eq_name':eq_name, 'subeq_name':subeq_name, 'abnor_name':abnor_name, 'vol_name':vol_name, 'pathimage':pathimage, 'job_picture':job_picture}}
#             ## save ข้อมูลลง ฐานข้อมูล           


#         if  vol_name == "22KV" and eq_name == "เสา" and subeq_name == "คอนคอนกรีต" and abnor_name =="บิ่น,แตก,bond wire หลุด,ขาด":
#             vol_name = "DA"
#             eq_name = "PO"
#             subeq_name = "2A"
#             abnor_name ="02"

#             filename = request.FILES['image'].name
#             f = os.path.splitext(filename)
#             n = f[0]
#             ext = f[1]
#             #timedate & time in Python

#             timestr = time.strftime("%Y%m%d-%H%M%S")


#             f_image.name = "{}_{}_{}_{}_{}_{}{}".format(job_officerid, vol_name, eq_name, subeq_name, abnor_name, timestr, ext)
#             print(f_image.name)


#             #past image
#             pathimage = "/media/{}".format(f_image.name) 
#             print(pathimage)


#             # UP image cload
#             uploaded_file = request.FILES['image']
#             print(uploaded_file)
#             payload=uploaded_file
#             headers = {
#             'Content-Type': 'image/jpg'
#             }
#             path_file = f_image.name

#             url = "https://objectstorage.ap-tokyo-1.oraclecloud.com/p/dI47BfTpwxXJODPhiO1p2wmYqyL0M-6b4TqRxU1ETcPDVFSjOC9sjXxPi9W-NomC/n/peacloud/b/Aidea/o/" + path_file


#             response = requests.request("PUT", url, headers=headers, data=payload)

#             job_picture = "https://objectstorage.ap-tokyo-1.oraclecloud.com/p/dI47BfTpwxXJODPhiO1p2wmYqyL0M-6b4TqRxU1ETcPDVFSjOC9sjXxPi9W-NomC/n/peacloud/b/Aidea/o/{}".format(f_image.name)

#             nameimageold = filename
#             nameimagenew = f_image.name
#             ## save ข้อมูลลง ฐานข้อมูล 
                
#             img = Image(job_officerid=job_officerid, eq_name=eq_name, subeq_name=subeq_name, abnor_name=abnor_name, vol_name=vol_name, abnor_other=abnor_other, nameimageold=nameimageold, nameimagenew=nameimagenew, pathimage=pathimage, job_picture=job_picture)
#             img.save()
                
#             context={'data':{' job_officerid':job_officerid, 'eq_name':eq_name, 'subeq_name':subeq_name, 'abnor_name':abnor_name, 'vol_name':vol_name, 'pathimage':pathimage, 'job_picture':job_picture}}
#             ## save ข้อมูลลง ฐานข้อมูล 

#             pathimage = "/media/{}".format(f_image.name) 
#             vol_name = "DA"
#             eq_name = "PO"
#             subeq_name = "2A"
#             abnor_name ="13"

#             img = Image(job_officerid=job_officerid, eq_name=eq_name, subeq_name=subeq_name, abnor_name=abnor_name, vol_name=vol_name, abnor_other=abnor_other, nameimageold=nameimageold, nameimagenew=nameimagenew, pathimage=pathimage, job_picture=job_picture)
#             img.save()
                
#             context={'data':{' job_officerid':job_officerid, 'eq_name':eq_name, 'subeq_name':subeq_name, 'abnor_name':abnor_name, 'vol_name':vol_name, 'pathimage':pathimage, 'job_picture':job_picture}}
            
#             ## save ข้อมูลลง ฐานข้อมูล           
            









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



