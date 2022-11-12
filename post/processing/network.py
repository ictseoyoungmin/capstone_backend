# network define file
from torch import nn
import torch

class BaseModel():
    def __init__(self):
        self.name = "RRU-Net"
    
    def get_model(self,train=True,gpu = False):
        model = "defactor-[val_dice]-0.7420-[train_loss]-0.0753.pkl"
        
        # model load(model)
        if train:
            model.train()
        else:
            model.eval()
        if gpu:
            if torch.cuda.is_available():
                model.cuda()
                        
        return model
        


# Example 
from torchvision.models.segmentation import deeplabv3_resnet101    
from PIL import Image
from torchvision import transforms
import matplotlib.pyplot as plt
from .config import OUT_DIR

def get_model_example():
    print('get_model')
    model = deeplabv3_resnet101(pretrained=True)
    model.eval()
    return model

def pred(model,filename):
    print('pred')
    input_image = Image.open(filename)
    input_image = input_image.convert("RGB")
    preprocess = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    input_tensor = preprocess(input_image)
    input_batch = input_tensor.unsqueeze(0) # create a mini-batch as expected by the model

    # move the input and model to GPU for speed if available
    if torch.cuda.is_available():
        input_batch = input_batch.to('cuda')
        model.to('cuda')

    with torch.no_grad():
        output = model(input_batch)['out'][0]
    output_predictions = output.argmax(0)
    return output_predictions,input_image.size

def draw_heatmap():
    pass

# for deepLab
def seg_result(pred,input_image_size,show=False):
    # create a color pallette, selecting a color for each class
    print('seg_result')
    palette = torch.tensor([2 ** 25 - 1, 2 ** 15 - 1, 2 ** 21 - 1])
    colors = torch.as_tensor([i for i in range(21)])[:, None] * palette
    colors = (colors % 255).numpy().astype("uint8")

    # plot the semantic segmentation predictions of 21 classes in each color
    r = Image.fromarray(pred.byte().cpu().numpy()).resize(input_image_size)
    r.putpalette(colors)
    
    if show:
        plt.imshow(r)
        plt.show()
    return r
    