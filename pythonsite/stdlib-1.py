import os

print (os.getcwd())
print (os.system('dir'))

import glob
print (glob.glob('*.py'))

import sys
print (sys.argv)
sys.stderr.write('Some error' 'has occured')

url = 'http:\\google.com'
# url = 'http://tycho.usno.navy.mil/cgi-bin/timer.pl'
# import requests
# r = requests.get("http://example.com/foo/bar")

# from urllib.request import urlopen
# for line in urlopen(url):
#     # line = line.decode('utf-8')  # Decoding the binary data to text.
#     print(line)

# from urllib3 import Request, urlopen, URLError