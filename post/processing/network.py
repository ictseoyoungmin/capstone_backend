# network define file
from torch import nn


class BaseModel(nn.Module):
    def __init__(self):
        super.__init__(BaseModel,self)
        self.name = "아직안정함"
    
    def get_model(self):
        model = ""
        return model
    
    