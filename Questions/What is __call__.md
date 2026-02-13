# Question
I often run into code like 

net=ResNet()

net(x)

and ResNet looks like I can't insert something into it. But it works.

And this is because of method __ call __

Here, I am going to write about method like that including __ call __

# Python and class
All things in python are class
number 5 is int class, string like "Love" is string class...
And the operation like sum of two string is possible due to underscore method.
str1+str2 is same as str1.__ add __(str2)
like this, double underscore plays critical role in invisible world of python.
