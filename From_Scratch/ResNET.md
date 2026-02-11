```python
import torch.nn as nn

#This is bottleneck
class block(nn.Module):
  def __init__(self, in_channels,out_channels,identity_downsample=None,stride=1):
    super(block,self).__init__()
    self.expansion=4
    self.conv1=nn.Conv2d(in_channels,out_channels,kernel_size=1,stride=1,padding=0)
    self.bn1=nn.BatchNorm2d(out_channels)
    self.conv2=nn.Conv2d(out_channels,out_channels,kernel_size=3,stride=stride,padding=1)
    self.bn2=nn.BatchNorm2d(out_channels)
    self.conv3=nn.Conv2d(out_channels,out_channels*self.expansion,kernel_size=1,stride=1,padding=0)
    self.bn3=nn.BatchNorm2d(out_channels*self.expansion)
    self.relu=nn.ReLU()
    self.identity_downsample=identity_downsample
```

<img width="311" height="263" alt="image" src="https://github.com/user-attachments/assets/21c5c272-553d-46bf-ae7a-87c7f215b43d" />

This code is implementation of bottle neck. As this picture showing, the number of channel gets 4 times of input channle(self.expansion=4). 
And the number of layers is 3(We have three convs. conv1, conv2, conv3)
The size of kernel, stride, padding are same as the image from ResNET paper.
