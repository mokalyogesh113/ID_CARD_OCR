import easyocr
import re

# import pytesseract

import numpy as np
from imageio.v2 import imread


import sys
sys.stdout.reconfigure(encoding='utf-8')


def get_aadhar_data(img_path):
    
    
    reader = easyocr.Reader(['en','hi'])
    result = reader.readtext(img_path,paragraph=False, decoder = "beamsearch")

    str = ""
    for i in result:
        str += i[1]
        str += '\n'
    
    print(str)

    

    def extract_aadhar_data(text):
        all_text_list = re.split(r'[\n]', text)
        
        # Process the text list to remove all whitespace elements in the list.
        text_list = list()
        for i in all_text_list:
            if re.match(r'^(\s)+$', i) or i=='':
                continue
            else:
                text_list.append(i)

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
        '''
        ():

            aadhar_dob_pat = r'(Year|Birth|irth|YoB|YOB:|DOB:|DOB)'
            date_ele = ""
            index = 0
            dob_idx = 0
            for idx, i in enumerate(text_list):
                if re.search(aadhar_dob_pat, i):
                    index = re.search(aadhar_dob_pat, i).span()[1]
                    date_ele = i
                    dob_idx = idx
                else:
                    continue

            date_str=''
            for i in date_ele[index:]:
                if re.match(r'\d', i):
                    date_str = date_str+i
                elif re.match(r'/', i):
                    date_str = date_str+i
                else:
                    continue
                    
            user_dob = date_str
        '''

        pan_date_pat = r'^\d{2}/\d{2}/\d{4}$'
        dob_found = False
        for idx,i in enumerate(text_list):
            for j in range(len(i) - 9):
                k = i[j:j+10]
                print(k)
                if re.search(pan_date_pat , k):
                    dob_idx = idx
                    user_dob = k
                    dob_found = True
                    break
            if(dob_found):
                break
            

        # 4) Name
        user_name = text_list[dob_idx-1]
        
        # return [user_aadhar_no, user_gender, user_dob, user_name]
        return{
            "user_aadhar_no" :  user_aadhar_no,
            "user_gender" : user_gender,
            "user_dob" : user_dob,
            "user_name" : user_name
        }


    return extract_aadhar_data(str)


def read_image(img_path):
    return imread(img_path)

def main():
    data = get_aadhar_data(read_image('yogesh.png'))
    print("Data Extracted is:- ",data)
    
if __name__ == '__main__':
    main()
    