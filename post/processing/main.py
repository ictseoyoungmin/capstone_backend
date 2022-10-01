from . import config

class Main():
    def __init__(self):
        self.image_dir = config.USER_IMAGE_DIR
        self.result_dir = config.OUT_DIR
        
    def get(self):
        print('GET')

    def run(self):
        pass

if __name__ == '__main__':
    sess = Main()
    sess.run()