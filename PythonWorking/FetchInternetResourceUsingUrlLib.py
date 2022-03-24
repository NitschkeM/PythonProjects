import urllib.request

with urllib.request.urlopen('http://python.org/') as response:
    html = response.read()



# Exception has occurred: URLError
# <urlopen error unknown url type: https>
#   File "D:\Software-Development\Projects\PythonProjects\PythonWorking\FetchInternetResourceUsingUrlLib.py", line 3, in <module>
#     with urllib.request.urlopen('http://python.org/') as response: