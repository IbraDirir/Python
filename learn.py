import random
import urllib.request

def  download_web_image(url):
     name = random.randrange(1,1000)
     full_name = str(name) + ".jpeg"
     urllib.request.urlretrieve(url, full_name)

download_web_image("https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSImDyCgy9JmL-eptrGZtPbwmvA4xvL6jhkaed24iAeOcJjbq2SDA")

