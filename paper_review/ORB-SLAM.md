# [논문 제목] ORB-SLAM: a Versatile and Accurate Monocular SLAM System
## 1. Summary
Contribution
1. 

System overview
-A. Feature choice
Feature: where and what is it?

Use same features are used to for place recognition to perform frame-rate relocalization and
loop detection. Now that this system doesn't need to calculate features twice, it becomes efficient.
To realize it, Author uses ORB features. 
1. it is fast to cumpute and match
2. it realizes same point as identical even if the view point changes. Even the points are far(wide baseline),
   it can implement its own job well as the points are close.
4. It has good place recognition performance

Loop closing: As the error accumulates, if camera comes back to the origin, it can map the point to strange point.
To prevent this, loop closing is needed. This can move the strange point to origin.
<img width="828" height="671" alt="image" src="https://github.com/user-attachments/assets/a1cd2b9a-36fd-4d73-bfc0-5af87240df18" />





## 2. Key Method



## 3. Critique
- 이 부분은 좋은데, 실시간 처리(Real-time)에는 무거울 것 같음.

## 4. Code Implementation
-

