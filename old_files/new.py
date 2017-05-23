import cv2
import urllib2
import numpy as np
import sys

host = "192.168.0.100:8080"

string = 'http://' + host + '/stream'

stream = urllib2.urlopen(string)

bytes = ''
while True:
        bytes +=stream.read(1024)
        a = bytes.find('\xff\xd8')
        b = bytes.find('\xff\xd9')
        if a != -1 and b != -1:
                jpg = bytes[a:b+2]
                bytes = bytes[b+2:]
                i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.CV_LOAD_IMAGE_COLOR)
                cv2.imshow(string, i)
                if cv2.waitKey(1) == 27:
                        exit(0)

