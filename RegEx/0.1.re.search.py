import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x) # <re.Match object; span=(0, 17), match='The rain in Spain'>

x2 = re.search("\s", txt)
print("The first white-space character is located in position:", x2.start()) # start vi tri

x3 = re.search("\s.{1}", txt)
print( x3)

txt2 = "0907768350"
x4 = re.search("0\d{9}", txt2)
print("dd:", x4.group()) # group gia tri

txt3 = "Vincent dep trai so 1 the gioi"
x5 = re.search("\d.+", txt3)
print(f'Da tim thay nguoi: "{x5.group()}"')

txt4 = "My email is example@example.com"
email_pattern = r"\S+@\S+" # tim dia chi email
match = re.search(email_pattern, txt4)

if match:
    print("Dia chi email tim thay:", match.group())
    
