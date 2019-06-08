# Challenge 6
#http://www.pythonchallenge.com/pc/def/channel.html
#http://www.pythonchallenge.com/pc/def/channel.zip
import re

# importing required modules 
from zipfile import ZipFile 
  
# specifying the zip file name 
file_name = "channel.zip"
archive = ZipFile(file_name, 'r')

txt="90052.txt"
getComments=''
# opening the zip file in READ mode 
with ZipFile(file_name, 'r') as zip: 
   for i in range(0,1000):
      with zip.open(txt) as my_file:
         getComments+=archive.getinfo(txt).comment.decode("utf-8")   #decode removes the b'' from string
         s=str(my_file.read())
         print(s)
         s=str(re.findall("(?i)next nothing is (\d+)",s))   #ignore the case in the string, get all the decimals
         txt=str(s.strip("['']"))+'.txt'
         print(txt)
         print(getComments)