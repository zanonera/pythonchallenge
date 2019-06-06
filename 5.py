# Challenge 5
#http://www.pythonchallenge.com/pc/def/peak.html

import pickle

file = open("banner.p",'rb')
object_file = pickle.load(file)
print(object_file)

#list of lists of tuples:
for line in object_file:
   print("".join([k * v for k, v in line]))