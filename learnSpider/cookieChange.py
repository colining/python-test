str = "c_secure_uid=NTQ5; c_secure_pass=7d72b685dccd03101b9f7eb6344f7c76; letskillie6=false; c_secure_user_link_online=success"
str1 = ':'
result = ''
items = str.split(';')
for each in items:
    a = each.split('=')
    result += "'"+a[0]+"'"+":""'"+a[1]+"',"

print result




