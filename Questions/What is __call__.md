# Question
I often run into code like 

net=ResNet()

net(x)

and ResNet looks like I can't insert something into it. But it works.

And this is because of method __ call __


# Python and class
Everything is an object.
number 5 is int class, string like "Love" is string class...
And the operation like sum of two string is possible due to underscore method.
str1+str2 is same as str1.__ add __(str2)
like this, double underscore plays critical role in invisible world of python.


# __ call __
method __ call __ is invoked when we call a function.
In Python, functions are objects. But usually, we implement __ call __ in a class to make its instances behave like functions (Callable Objects).
Because function is class as well.


# How does it used in ResNet?
nn.Module and ResNet look like this internally with simplifying:
```python
class nn.Module():
  def __call__(self,x):
  result=self.forward(x)
  return result

class ResNet(nn.Module):
  def forward(self,x):
  return 2*x

model=ResNet()
model(x)
```
Here's what's happening

1. model(x)? class with parentheses? then implement __ call __
2. in the call method, it has already forward method, but ResNet inherits nn.Module and overrides the forward method, it is overriden. so as a result, call method implement forward which we define.










