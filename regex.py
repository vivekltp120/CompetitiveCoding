import re

text='667-567-134 give me Mr. Vaibhav Mr. T Mr. Prashant the phone number,and emailid.phone number is 9450037508.email id is vivekltp120@gmail.com chaurasiavivek87@gmail.com'
text2='''
Mr. Vivek
Mr Vaibhav
vivekltp120@gmail.com
vaibhav@aol.com
https://www.google.com
http://amazon.com
https://edureka.edu

'''

regex=re.findall('[\w.+%-_]{1,20}@\w{2,3}[.][a-zA-Z]{2,3}',text)


remail=re.compile(r'[\w.+%-_]{1,20}@\w{2,10}\.[a-zA-Z]{2,3}')
remail2=re.compile(r'[\w.+%-_]+@[a-zA-Z]+.[a-zA-Z]+')
print(remail.findall(text))
print(remail2.findall(text))


reg=re.compile(r'number')
print(reg.findall(text))

rnum=re.compile(r'\d{3}-\d{3}-\d{3}')
print(rnum.findall(text))


nreg=re.compile(r'Mr\.?\s[A-Z]\w*')
print(nreg.findall(text2))

rsplit=re.split('\W',text)
print(rsplit)


sitereg=re.compile(r'https?://.\w+.\w+.\w+')
matches=sitereg.finditer(text2)
for match in matches:
    print(match.group())