import sys,os
sys.path.append('backend\djangoreactapi')
from djangoreactapi import settings

LOCALHOST = settings.LOCALHOST

MEDIA_DIR = settings.MEDIA_ROOT
MEDIA_URL = settings.MEDIA_URL

USER_IMAGE_DIR = os.path.join(MEDIA_DIR,"images") # 사용자 입력 이미지 DIR
USER_IMAGE_URL = os.path.join(MEDIA_URL,"images") 


OUT_URL = os.path.join(MEDIA_URL,"out") # 출력 히트맵
OUT_DIR = os.path.join(MEDIA_DIR,"out")

os.makedirs(OUT_DIR,exist_ok=True)

IMAGE_SHAPE = (256,256,3)

# "http://127.0.0.1:8000/media/images/a2_APHuk9o.jpg"
def process_raw_path(raw_path,out = False):
    """
        From React path
        "C/:fakeepath/'imageName.jpg' => available url
    """
    local = OUT_URL if out else USER_IMAGE_URL
    url = os.path.join(LOCALHOST+
                        local,
                        str(raw_path).split('C:\\fakepath\\')[1])
    print("rrrrrrrrrrrrrrrrrr",url)    
    return url
    
