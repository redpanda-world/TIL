# Visual Language Maps for Robot Navigation
## 1. Problem and Contribution
People are great navigator thanks to their ability to build cognitive map.
The problem of models, which navigate using natural language is that they can't generalize to unseen instructions or require copious amount of data.
With incorporate VLM with navigation model, these promlems seem to be disappeared. VLM doesn't require dataset and can generalize.
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

## 3. How can I use these ideas?


## 4. Others
