import requests
from requests.exceptions import Timeout

from sys import argv

first, url = argv
print('url : %s', url)
try:
    r = requests.get(url, timeout=10)

    print(r)

except Timeout:
    # print(e_exception)
    print('timeout', TimeoutError)

except Exception as e_exception:
    # print(e_exception)
    e_code = e_exception.code if hasattr(e_exception, 'code') else 400
    e_message = e_exception.message if hasattr(e_exception, 'message') else ','.join(list(map(str, e_exception.args)))
    print(e_code, e_message)