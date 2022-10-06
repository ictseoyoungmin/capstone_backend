from . import config

class Main():
    def __init__(self):
        self.image_dir = config.USER_IMAGE_DIR
        self.result_dir = config.OUT_DIR
        
    def get(self):
        print('GET')

    def run(self,raw_path):
        
        # data x load
        
        # pre-trained model load
        
        # model predict x -> y : 
        path = config.process_raw_path(raw_path)
        return path,0.8,True # 가정
        pass

if __name__ == '__main__':
    sess = Main()
    sess.run()