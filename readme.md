## 这是自动做性格测试的

* 先PILLOW截图固定位置，然后转成base64发送post请求给服务端
* 服务端由flask搭建，只开放两个接口，用于将带有文字描述的图片经行积极和消极的打分，原理如下：
emsp;&emsp;服务端接收到图片，转成numpy数组，交给[EasyOCR](https://github.com/JaidedAI/EasyOCR)转成文字
emsp;&emsp;文字输入[中文情感识别模型](https://github.com/hiDaDeng/cnsenti)，输出积极和消极的打分
* 将结果发给客户端，通过积极和消极分数做出选择
* 客户端用控制鼠标移动到选项相应坐标点击或拖拽答案

## 用法

### 服务端
* 服务端需要安装easyocr和cnsenti
```shell
   pip install easyocr
   pip install cnsenti
```
* 运行
```shell
   python one_flask.py
```
* 服务端请推荐直接在codespace运行。用一两次没必要部署在自己服务器。
  
### 客户端
* 客户端需要安装PILLOW库和cv2库
* 根据个人屏幕分辨率，修改截图和鼠标点击拖拽的操作位置
* 根据不同的自己的codespace的url，修改请求的url
* 根据不同花样的测试(呕)，选择不同的py文件直接运行，知道题数也可以修改题数，不知道的做完后手动暂停

