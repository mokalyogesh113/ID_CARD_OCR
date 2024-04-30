# Importing Libraries
import easyocr
import re
import time

import numpy as np
from imageio.v2 import imread

import sys
sys.stdout.reconfigure(encoding='utf-8')

def extract_img_data(img_path):
    reader = easyocr.Reader(['en', 'hi'])
    result = reader.readtext(img_path,paragraph=False, decoder = "beamsearch")
    all_text_list = [i[1] for i in result]
    text_list = list()
    for i in all_text_list:
        if re.match(r'^(\s)+$', i) or i=='':
            continue
        else:
            text_list.append(i)
    print('-'*30)
    for i in text_list:
        print(i)
    print('-'*30)
    return text_list

def extract_aadhar_data(text_list):
    # Extracting all the necessary details from the pruned text list.
    # 1) Aadhar Card No.
    aadhar_no_pat = r'^[0-9]{4}\s[0-9]{4}\s[0-9]{4}$'
    for i in text_list:
        if re.match(aadhar_no_pat, i):
            user_aadhar_no = i
        else:
            continue

    # 2) Gender
    aadhar_male_pat = r'(Male|MALE|male)$'
    aadhar_female_pat = r'[(Female)(FEMALE)(female)]$'
    user_gender = ""
    for i in text_list:
        if re.search('(Male|male|MALE)$', i):
            user_gender = 'MALE'
        elif re.search('(Female|FEMALE|female)$', i):
            user_gender = 'FEMALE'
        else:
            continue

    # 3) DOB
    pan_date_pat = r'^\d{2}/\d{2}/\d{4}$'
    dob_found = False
    for idx,i in enumerate(text_list):
        for j in range(len(i) - 9):
            k = i[j:j+10]
            if re.search(pan_date_pat , k):
                dob_idx = idx
                user_dob = k
                dob_found = True
                break
        if(dob_found):
            break

    # 4) Name
    name_pat = r'[A-Z][a-z]+(?:\s+[A-Z][a-z]+)+'
    for i in text_list:
        if re.match(name_pat , i):
            user_name = i
        else:
            continue    

    

    # return [user_aadhar_no, user_gender, user_dob, user_name]
    return{
        "aadhar_no" :  user_aadhar_no,
        "gender" : user_gender,
        "dob" : user_dob,
        "name" : user_name
    }



def extract_pan_data(text_list):  
    # Extracting all the necessary details from the pruned text list.
    # 1) PAN Card No.
    pan_no_pat = r'.*Permanent Account Number Card.*|.*Permanent Account Number.*|.*Permanent Account.*|.*Permanent.*|.*Perm.*|.*Acc.*'
    pan_no = ""
    for i, text in enumerate(text_list):
        if re.match(pan_no_pat, text):
            pan_no = text_list[i+1]
        else:
            continue
    user_pan_no = ""
    for i in pan_no:
        if i.isalnum():
          user_pan_no = user_pan_no + i
        else:
          continue
    
    # 2) DOB
    pan_dob_pat = r'(Year|Birth|irth|YoB|YOB:|DOB:|DOB)'
    user_dob = ""
    dob_idx = -1
    for idx, i in enumerate(text_list):
      if re.search(pan_dob_pat, i):
        date_str=''
        date_ele = text_list[idx+1]
        dob_idx = idx + 1
        for x in date_ele:
            if re.match(r'\d', x):
                date_str = date_str+x
            elif re.match(r'/', x):
                date_str = date_str+x
            else:
                continue
        user_dob = date_str
        break
      else:
        continue
    if(user_dob == ""):
      pan_date_pat = r'^\d{2}/\d{2}/\d{4}$'
      for idx,i in enumerate(text_list):
        if re.search(pan_date_pat , i):
          dob_idx = idx
          user_dob = i
        else:
          continue

    # 3) NAME
    pan_name_pat = r'.*(name|Name).*'
    user_name = ""
    for idx, i in enumerate(text_list):
        if re.search(pan_name_pat, i):
          user_name = text_list[idx + 1]
          break
        else:
          continue
    if(user_name == ""):
      user_name = text_list[dob_idx - 2]

    # 4) Father name
    pan_father_name_pat = r'.*(Father | father).*(name | Name)'
    user_father_name = ""
    for idx, i in enumerate(text_list):
      if re.search(pan_father_name_pat, i):
        user_father_name = text_list[idx + 1]
        break
      else:
        continue
    if(user_father_name == ""):
      user_father_name = text_list[dob_idx - 1]

    # ###########################################
    return {
        'pan_no' : user_pan_no,
        'dob' : user_dob,
        'name' : user_name,
        'father_name' : user_father_name
    }   

    
def get_aadhar_data(img_path):
    return extract_aadhar_data(extract_img_data(img_path))

def get_pan_data(img_path):    
    return extract_pan_data(extract_img_data(img_path))

def main():
    choice = int(input("1. Aadhar Card \n 2. Pan Card"))
    if choice == 1:
        data = extract_aadhar_data(extract_img_data('./IMG/yogesh.png'))
        print("Data Extracted is:- ",data)
    else:
        data = extract_pan_data(extract_img_data('./IMG/new.png'))
        print("Data Extracted is:- ",data) 

if __name__ == '__main__':
    main()