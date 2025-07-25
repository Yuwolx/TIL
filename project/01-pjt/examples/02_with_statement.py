# use open finction way
import sys
print(sys.getdefaultencoding)
# Can check incording type
data = open('example.txt','r')
print(data)
print(data.read())
#data.close()
print(data.read())

with open('example.txt.','r',encoding='utf-8') as file:
    content = file.read()
    print(content)
print(content)