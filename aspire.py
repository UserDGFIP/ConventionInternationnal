import re 
import time
with open('portail.htm','r') as f:
    output = f.read()
#print(output)
results = re.findall(r"\"\/.*pdf", output)
import urllib.request    
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)
import os
os.chdir(os.path.dirname(__file__))
import os.path
for r in results:
    try :
        url = "http://webcache.googleusercontent.com/search?q=cache:impots.gouv.fr"+r[1:]
        filename = url.split("/")
        filename = filename[-1]
        #print(filename)
        print(url)
        print(os.path.isfile(os.getcwd()+"\\"+filename+".html"))
        print(os.getcwd()+"\\"+filename)
        if not os.path.isfile(os.getcwd()+"\\"+filename+".html") :
            urllib.request.urlretrieve(url, filename+".html")
            time.sleep(15)
    except Exception as e  :
        print(e)


