# Visual Language Maps for Robot Navigation
## 1. Problem and Contribution
People are great navigator thanks to their ability to build cognitive map.
The problem of models, which navigate using natural language is that they can't generalize to unseen instructions or require copious amount of data.
With incorporate VLM with navigation model, these problems seem to be disappeared. VLM doesn't require dataset and can generalize.
However there are other problems. it struggles
1. to recognize the same objects as same objects based on where the robot is seeing
2. and localize spatial goal like 'between sofa and TV'.

Key contribution: Localizing spatial goals like 'between sofa and TV'  &   determining whether the objects are obstacles or not based on embodiment.(Desk could be an obstacle to turtlebot but not so to drone)

As the picture shows, VLMaps fuses 3D map and embedding of each points.



## 2. Idea
The key idea of VLMaps is to fuse pretrained visual language features with 3D reconstruction. 
Author fused LSeg embedding with their corresponding 3D map locations. Then it doesn't need to label the segmentation manually.
<img width="745" height="265" alt="image" src="https://github.com/user-attachments/assets/1a5430f6-1bbf-4b20-b2b9-b7d45417025f" />

The pipeline consist of four steps.
### A. Building a Visual-Language Map
kEY idea: Convert pixel coordinate to world coordinate and project world coordinate to plane to match it to grid map.
And stack embedding on the each pixels.

### B. Localizing Open-Vocabulary Landmarks   
Key idea: We can convert human text to embedding by applying LSeg and make matrix . Also we have map embedding &Q&. we can measure similarity by calculating $$\mathbf{S} = \mathbf{Q} \cdot \mathbf{E}^T$$. S indicates how likely this pixel belongs to the class

### C. Generating Open-Vocabulary Obstacle Maps
Key idea: It set potential obstacle list in advance based on embodiment.

### D. Zero-Shot Spatial Goal Navigation from Language
Key idea: Convert natural language to language that robot can understand using LLM.

## 3. How can I use these ideas?
1. I can combine LLM model to translate natural language to robot language.
  This could be general. If I don't consider the amount of time to operate, I can combine it to any model like ORB-SLAM.  
2. I can measure similarity by computing inner product.
   This is often used like attention. If I have to work on project of object detection, I guess I can apply this to decrease the amount of time to calculate.
## 4. Others
### Limitation
As I run this model, I couldn't even find multiple objects. It can find just one object by typing 'chair', or'sofa' but can't if I type 'sofa and chair' 
And even though  I succeed to find a singe object, its performance doesn't seem like great. It notes unidentified area as sofa, or chair.

### The reason of this Limitation
I think it's because of the way that it calculate the similarity.
$$\mathbf{S} = \mathbf{Q} \cdot \mathbf{E}^T$$
As the paper says, Q, E have just a word. So the similarity pluged if I type multiple objects.
