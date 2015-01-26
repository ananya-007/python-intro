import urllib.request
url_string = 'http://www.amazon.in/'
url_string = 'https://www.google.co.in/'
print (urllib.request.urlopen(url_string).read())