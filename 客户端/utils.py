import base64 
import time 
import requests 
import os
from PIL import Image
from PIL import ImageGrab
import json
import cv2 
import base64

url = "https://animated-orbit-rwxpw7p6v6v3p6qw-5000.app.github.dev/ocr" 
headers = {'content-type': "application/json"}
###np 图片编码成base64形式
def image_to_base64(image_mat):
    image = cv2.imencode('.jpg', image_mat)[1]
    image_code = str(base64.b64encode(image), 'utf-8')
    return image_code
###base64图片解码成numpy图
def base64_to_image(imgBase64):
    img_data = base64.b64decode(imgBase64)
    bs = np.asarray(bytearray(img_data), dtype='uint8')
    img = cv2.imdecode(bs, cv2.IMREAD_COLOR)
    return img

def capture():  
    img = ImageGrab.grab(bbox=(472, 420, 831, 602))  # bbox 定义左、上、右和下像素的4元组
    img.save('temp.jpg') 

def shoot_one():
    
    img = cv2.imread('temp.jpg') 
 
    data = { 
        "base64Img":image_to_base64(img)
    }  
    
    response = requests.post(url, json=json.loads(json.dumps(data)), headers=headers)
    print(response)
    if response:
        result = json.loads(str(response.content, 'utf-8'))
        print(result)
        with open('cepin.log','a') as fp:
            fp.write(f"{result['text']}\n")
            fp.write(f"{result['pos']}\n{result['neg']}\n")
        
        '''中文u8转码
        for v in result.values():
            str_data_to_zh = v.encode('utf-8').decode('unicode_escape')
            print(str_data_to_zh) 
        '''
