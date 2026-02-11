#problem: I want to download dataset!!

import os
from torchvision import datasets
from torchvision import transforms


#first of all we decide where to store the dataset
datapath='./data'

#There is a chance that it is already exist, check it
if not os.path.exists(datapath):
  os.makedirs(datapath)

#datapath:set the path to store dataset
#split:take only training dataset
#downlod=True:If there's no file in the datapath, download it
#transform=transforms.ToTensor(): because we will use pytorch, transform it into tensor
train_dataset=datasets.STL10(datapath,split='train',download=True,transform=transforms.ToTensor())
test_dataset=datasets.STL10(datapath,split='test',download=True,transform=transforms.ToTensor())
