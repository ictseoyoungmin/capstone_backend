import sys,os
sys.path.append('backend\djangoreactapi')
from djangoreactapi import settings

# Django url
LOCALHOST = settings.LOCALHOST

# media local path / url
MEDIA_DIR = settings.MEDIA_ROOT
MEDIA_URL = settings.MEDIA_URL

# media/images path / url
USER_IMAGE_DIR = os.path.join(MEDIA_DIR,"images") 
USER_IMAGE_URL = os.path.join(MEDIA_URL,"images") 

# result path / url
OUT_URL = os.path.join(MEDIA_URL,"out") 
OUT_DIR = os.path.join(MEDIA_DIR,"out")
os.makedirs(OUT_DIR,exist_ok=True)

BACKEND_DIR = settings.BASE_DIR

IMAGE_SHAPE = (256,256,3)

# "http://127.0.0.1:8000/media/images/a2_APHuk9o.jpg"
def process_raw_path(raw_path,out = False):
    """  From React path
        "C/:fakeepath/'imageName.jpg' => available url

    Args:
        raw_path (str): frontend to backend / backend to frontend path
        out (bool, optional): True : backend to frontend , False : frontend to backend
        Defaults to False.

    Returns:
        str: url or path, file_name
    """
    file_name = str(raw_path).split('\\')[-1]    
    
    if out: # store path
        url = os.path.join(LOCALHOST+
                        OUT_URL,
                        file_name)
    else: # react src url
        url = os.path.join(USER_IMAGE_DIR,
                        file_name)
    
    print("rrrrrrrrrrrrrrrrrr",url)
    return url,file_name
    
