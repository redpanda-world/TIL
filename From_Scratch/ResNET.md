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
The size of kernel is same as the image in the paper.
- conv1
  
$$O = \left\lfloor \frac{I - K + 2P}{S} \right\rfloor + 1$$

According to this formula and even intuitively, conv1 has to have 1 stride and 0 padding to keep the size.

-conv2

$(W - 3 + 2 \times 1) / 1 + 1 = W$
according to this, the stride should be 1 with padding 1.
The reason why variable is used is to implement downsample as well by setting stride to 2 or more.

```python
  def forward(self,x):
        identitiy=x

        x=self.conv1(x)
        x=self.bn1(x)
        x=self.relu(x)

        x=self.conv2(x)
        x=self.bn2(x)
        x=self.relu(x)

        x=self.conv3(x)
        x=self.bn3(x)
        
        if self.identity_downsample is not None:
            identitiy=self.identity_downsample(identitiy)

        x+=identitiy
        x=self.relu(x)
        return x
```

This is code implementing forward method.
The reason why it is processed like this is this is the basic structure of bottle neck as shown above.
And because x varies during the process, to add x at the end of the bottle neck, it should be preserved by storing it in identity.
self.identity_downsamle(identity) make the channel be able to be summed to x. the shape of x can be different from identity.





