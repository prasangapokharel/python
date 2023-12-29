import requests
from PIL import Image
url=''
data= requests.get(url).content
f= open('image.jpg', 'wb')
f.write(data)
f.close()
img = Image.open('img.jpg')
img.show()