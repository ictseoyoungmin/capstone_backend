import os
from . import config as cfg
import PIL.Image as image
from . import network as net

class Main():
    def __init__(self):
        self.image_dir = cfg.USER_IMAGE_DIR
        self.result_dir = cfg.OUT_DIR
        
    def get(self):
        print('GET')

    def run(self,raw_path): # raw_path: react에서 넘어온 secure path
        
        # 0. 경로 수정
        user_path,img_name = cfg.process_raw_path(raw_path,out=False)
        img_name = img_name.split('.')[0]

        # 1. load model
        model = net.get_model_example()
    
        # 2. pred
        pred, img_size = net.pred(model,user_path)
        
        # result [seg_image, proba, isForgery] 예시 이므로 proba,isForgery 생략
        # 3. 
        seg_image = net.seg_result(pred,img_size,show=False)
        # seg_image, proba, isForgery = net.seg_result(pred,img_size,show=True)
        
        # store out image(segmentation(heatmap))
        print('save')
        store_path = os.path.join(cfg.OUT_DIR,f'{img_name}_result.jpg') 
        seg_image.convert('RGB').save(store_path)
        
        # return 
        seg_test,_ = cfg.process_raw_path(store_path,out=True) 
        proba_test = 0.8
        isForgery_test = True
        
        return seg_test, proba_test, isForgery_test

    def example_run(self,raw_path):
        # user image path 
        user_path,img_name = cfg.process_raw_path(raw_path,out=False)
        img_name = img_name.split('.')[0]

        # load model
        model = net.get_model_example()
    
        # pred
        pred, img_size = net.pred(model,user_path)
        
        # result [seg_image, proba, isForgery] 예시 이므로 proba,isForgery 생략
        seg_image = net.seg_result(pred,img_size,show=False)
        # seg_image, proba, isForgery = net.seg_result(pred,img_size,show=True)
        
        # store out image(segmentation(heatmap))
        print('save')
        store_path = os.path.join(cfg.OUT_DIR,f'{img_name}_result.jpg') 
        seg_image.convert('RGB').save(store_path)
        
        # return 
        seg_test,_ = cfg.process_raw_path(store_path,out=True) 
        proba_test = 0.8
        isForgery_test = True
        
        return seg_test, proba_test, isForgery_test
        
if __name__ == '__main__':
    sess = Main()
    sess.run()
    
    