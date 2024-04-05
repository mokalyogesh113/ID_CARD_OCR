import easyocr
import re
import time
start = time.time()

import numpy as np
from imageio.v2 import imread


import sys
sys.stdout.reconfigure(encoding='utf-8')

def get_pan_data(img_path):
  reader = easyocr.Reader(['en', 'hi'])
  result = reader.readtext(img_path,paragraph=False, decoder = "beamsearch")
  # for i in result:
  #   print(i[1])
  str = ""
  for i in result:
    str += i[1]
    str += '\n'

    print(str)

  # print("result to string :- ",str)

  def extract_pan_data(text):
    # Reading the image, extracting text from it, and storing the text into a list.
    all_text_list = re.split(r'[\n]', text)

    # Process the text list to remove all whitespace elements in the list.
    text_list = list()
    for i in all_text_list:
        if re.match(r'^(\s)+$', i) or i=='':
            continue
        else:
            text_list.append(i)

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
    # ###########################################

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

    # ###########################################

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

    # print("Father name" , user_father_name)


    # ###########################################
    return {
        'pan_no' : user_pan_no,
        'dob' : user_dob,
        'name' : user_name,
        'father_name' : user_father_name
    }
    # return [user_pan_no , user_dob]
    # ###########################################
  return extract_pan_data(str)



def read_image(img_path):
    return imread(img_path)

def main():
  data = get_pan_data(read_image('new.png'))
  print("The data is :- ",data)

  # data = get_pan_data("pan-2.png")
  # print("The data is :- ",data)

  # data = get_pan_data("pan-3.png")
  # print("The data is :- ",data) 

  # data = get_pan_data("pan-4.png")
  # print("The data is :- ",data)

  # print((time.time()-start) * 10**3, "ms")
  
  
if __name__ == "__main__":
  main()