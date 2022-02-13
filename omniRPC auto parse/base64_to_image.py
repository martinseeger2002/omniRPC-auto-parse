
import base64
  
  
file = open('data.txt', 'rb')
byte = file.read()
file.close()
  
decodeit = open('image.jpeg', 'wb')
decodeit.write(base64.b64decode((byte)))
decodeit.close()


