import re

txt = '''
    id=20085 trace_id=18014 func=__ip_se line=3536 mas "SNAT 192.168.99.11"
    id=20085 trace_id=18014 func=__ip_se line=3536 mas "SNAT 192.168.99.14"
    id=20085 trace_id=18014 func=__ip_se line=3536 mas "SNAT 192.168.99.15"
    id=20085 trace_id=18014 func=__ip_se line=3536 mas "SNAT 192.168.99.19"
    id=20085 trace_id=18014 func=__ip_se line=3536 mas "SNAT 0.0.0.0"
'''

## regex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
regex = r'(?:\d{1,3}\.){3}\d{1,3}' ## cú pháp tìm không nhớ (?: ... )
result = re.findall(regex, txt)


"""
    List comprehension
"""
result = [ip for ip in result if ip != '0.0.0.0']
print(result)

regex2 = r'(?!0\.0\.0\.0)(?:\d{1,3}\.){3}\d{1,3}' ## (?! ...) phủ định
result2 = re.findall(regex2, txt)
print(result2)