# -*- coding: utf-8 -*-
# network define file
"""
네트워크 load 및 predict 진행
"""
import os
from . import config as cfg
import torch
from PIL import Image
import cv2 as cv
from torchvision import transforms
import matplotlib.pyplot as plt
from .pre_trained.model.unet_model import Ringed_Res_Unet

def get_model(train=False,gpu = False):
    # model load(model)
    print('get_model')
    print(os.getcwd())
    model = Ringed_Res_Unet()
    model.load_state_dict(torch.load(
        f'{cfg.BACKEND_DIR}/post/processing/pre_trained/result/logs/defactor/Ringed_Res_Unet/{cfg.MODE_NAME}',
            map_location=torch.device('cpu')))
    
    if train:
        model.train()
    else:
        model.eval()
    if gpu:
        if torch.cuda.is_available():
            model.cuda()
            print('model device : cuda')
            
    return model
        
def pred(model,filename:str):
    print('pred')
    f = filename
    if not filename.endswith('jpg'):
        outfile_path = filename[:-3] + "jpg"
        input_image = cv.imread(filename)
        input_image = cv.cvtColor(input_image,cv.COLOR_BGR2RGB)
        input_image = Image.fromarray(input_image)
        input_image.save(outfile_path, "JPEG", quality=100)
        f = outfile_path
        
    input_image = Image.open(f)
    input_image = input_image.convert("RGB")
    
    preprocess = transforms.Compose([
        transforms.Resize((cfg.IMAGE_SHAPE[0],cfg.IMAGE_SHAPE[1])),
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
        output = model(input_batch)
    output = torch.sigmoid(output)
    output = output.squeeze(0)
    output_predictions = output.permute(1,2,0).detach().numpy()
    pre_image = input_tensor.permute(1,2,0).numpy()
    
    print(output_predictions.shape)
    return output_predictions,pre_image


# Example 
from torchvision.models.segmentation import deeplabv3_resnet101    

def get_model_example():
    print('get_model')
    model = deeplabv3_resnet101(pretrained=True)
    model.eval()
    return model



def pred_test(model,filename):
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

