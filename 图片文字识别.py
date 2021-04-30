#“You are using pip version 19.0.3, however version 20.0.2 is available.”pip 更新报错解决办法
#解决办法：使用国内的源下载：
#python -m pip install --upgrade pip -i https://pypi.douban.com/simple

import face_recognition
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

client = recognition.recog()

id = 'https://cdn.xiaoxiangxueyuan.com/pimages/material/20200113/c0ff24a1a2081faaff6fb4feeebf5c88.png'
image = requests.get(id).content

res = client.basicGeneral(image)

for i in range(len(res['words_result'])):
    print(res['words_result'][i]['words'])
