# ORB-SLAM: a Versatile and Accurate Monocular SLAM System
## 1. Problem and Contribution

The traditional SLAM algorithms suffered from high computational cost. 
ORB-SLAM makes it possible to implement SLAM in real-time, maintaining performance comparable to existing models



## 2. Idea
ORB-SLAM tried to get it faster. To achieve it, it used
- ORB features
- Covisibility graph

### WHY?
- ORB stands for Oriented FAST, Rotated Brief. ORB complemented feature-extract algorithms. FAST, as it shows by its name, focuses on speed to extract feature. Also traditional models use other features to implement different tasks such as tracking, localization, and loop closing. But by using ORB, it ends up with unifying it into one kind of feature.
- Covisibility graph is a graph that preserving nodes which share more than 15 points. By not considering points that have less importance, it also decreases burden of computational cost.


## 3. How can I use these ideas?
- When my model is not fast enough, then I think I can use other methods to extract features. Also I can use covisibility or data structures retaining only important information.

## 4. Others




