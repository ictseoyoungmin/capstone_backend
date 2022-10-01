import sys,os
sys.path.append('backend\djangoreactapi')
from djangoreactapi import settings

MEDIA_DIR = settings.MEDIA_ROOT
USER_IMAGE_DIR = os.path.join(MEDIA_DIR,"images") # 사용자 입력 이미지 DIR
OUT_DIR = os.path.join(MEDIA_DIR,"out")

os.makedirs(OUT_DIR,exist_ok=True)

IMAGE_SHAPE = (256,256,3)
