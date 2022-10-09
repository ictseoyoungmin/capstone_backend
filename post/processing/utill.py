import os
from . import config as cfg
import PIL.Image as image


def process(raw_path):
        # load user data x         
        _,img_name = cfg.process_raw_path(raw_path,out=False) # user image path
        img_name = img_name.split('.')[0]
        user_img = image.open(os.path.join(cfg.USER_IMAGE_DIR,img_name))
        
        # load pre-trained model 
        ## model = torch.load(mm.pth)
        
        # model predict x -> y : 
        ## pred = model(user_img)
        ## heatmap , proba , isForgery = pred 
        
        # store images/out/y
        # result = PIL(pred) 
        ## result.save(cfg.OUT_DIR+'/{img_name}_result.jpg')
        
        heatmap_test = os.path.join(cfg.OUT_DIR,f'{img_name}_result.jpg')
        proba_test = 0.8
        isForgery_test = True
        
        return heatmap_test, proba_test, isForgery_test
        