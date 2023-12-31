import mouse_action
import utils

def four_choices():
    rect = (170,125,1070,205) 
    choices=[(220,250),(220,340),(220,430),(220,520)]
    
    img = ImageGrab.grab(bbox=rect)  # bbox 定义左、上、右和下像素的4元组
    img.save('temp.jpg')
    img = cv2.imread('temp.jpg')  
    data = { 
        "base64Img":image_to_base64(img)
    }  
    response = requests.post(url, json=json.loads(json.dumps(data)), headers=headers) 
    if response:
        result = json.loads(str(response.content, 'utf-8'))
        print(result)
        pos ,neg = result['pos'],result['neg']
        pos = min(3,pos);neg = min(3,neg) 
        matrix = [[1,0,0,0],
                  [2,1,0,0],
                  [3,2,1,0],
                  [3,2,1,1]
                  ]
        
        choice = matrix[pos][neg]
        print(f'得分{choice}')
        time.sleep(.4+random.random()*.4)
        move( choices[choice][0]+random.randint(-5,5),choices[choice][1]+random.randint(-5,5)) 
        left_click() 
        time.sleep(.4+random.random()*.4)
        
        with open('cepin4.log','a') as fp:
            fp.write(f"{result['text']}\n")
            fp.write(f"{result['pos']}\n{result['neg']}\n")
        return True
    return False

def 竖着的四个选项(epoch=50):
    time.sleep(20)#你要在这段时间跳过前面的示例
    for _ in range(epoch): 
        t0 = time.time()
        succ = four_choices()
        print(f'耗时{time.time()-t0}')
        if not succ:
            break
        time.sleep(6+random.random())

if __name__=="__main__": 
     竖着的四个选项(50)#这个题量不确定啊
        
