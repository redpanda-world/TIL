# RANSAC(RANdom SAmple Consensus)

## Why is it needed
we need to robustly compute transformation in the presence of wrong matches.
RANSAC can help with this.
If number of outliers is less than 50%, RANSAC can help.


### General RANSAC Algorithm:

1. Randomly choose **s** samples. Typically **s** is the minimum samples to fit a model.
2. Fit the model to the randomly chosen samples.
3. Count the number **M** of data points (inliers) that fit the model within a measure of error **ε**.
4. Repeat Steps 1-3 **N** times.
5. Choose the model that has the largest number **M** of inliers.
