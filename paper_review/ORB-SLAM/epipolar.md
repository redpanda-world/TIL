# Epipolar Geometry & Fundamental Matrix

## 1. Epipolar Geometry

**Epipolar Geometry** completely describes the relative position and orientation between two cameras. It represents the intrinsic projective geometry between two views.

<img width="716" height="284" alt="image" src="https://github.com/user-attachments/assets/1c9783ea-c36a-4746-b291-87a2f35761d0" />


### Key Concepts
* **Epipole ($e_l, e_r$)**: The image point of the origin (pinhole) of one camera as viewed by the other camera. It is the intersection of the baseline with the image plane.

### Geometric Derivation
Consider a point $P$ in 3D space viewed by two cameras (Left and Right).
* **$X_l$**: Point coordinate in the Left Camera frame.
* **$X_r$**: Point coordinate in the Right Camera frame.
* **$t$ ($3 \times 1$)**: Position of the right camera in the left camera's frame (Translation).
* **$R$ ($3 \times 3$)**: Orientation of the right camera with respect to the left camera (Rotation).

The relationship between the coordinates is given by:

$$
X_l = R X_r + t
$$

### The Coplanarity Constraint
The vectors $X_l$, $t$, and $R X_r$ (which is $X_r$ rotated to the left frame) must be coplanar. This geometric constraint can be expressed using the scalar triple product (dot product and cross product):

$$
X_l \cdot (t \times R X_r) = 0
$$

Using the **skew-symmetric matrix** notation $[t]_x$ for the cross product:
$$
[t]_x = \begin{pmatrix}
0 & -t_z & t_y \\
t_z & 0 & -t_x \\
-t_y & t_x & 0
\end{pmatrix}
$$

The equation becomes:

$$
X_l^T [t]_x R X_r = 0
$$

### Essential Matrix ($E$)
We define the **Essential Matrix** $E$ as:
$$
E = [t]_x R
$$

Thus, the epipolar constraint in normalized image coordinates (camera coordinates) is:
$$
X_l^T T_x R X_r = 0
$$

---

## 2. Fundamental Matrix ($F$)

While the Essential Matrix ($E$) works with metric coordinates (camera frame), we often work with pixel coordinates in images. The **Fundamental Matrix** ($F$) generalizes $E$ for uncalibrated cameras involving intrinsic parameters.

<img width="495" height="135" alt="image" src="https://github.com/user-attachments/assets/9069d4b8-31bb-49f2-9e21-6f93e6daff2c" />
<img width="495" height="340" alt="image" src="https://github.com/user-attachments/assets/c74541ac-d65f-4507-b81b-2d07d4d1c59d" />




### From Camera to Pixel Coordinates
Using the Camera Matrix $K$ (Calibration Matrix), we relate the homogeneous pixel coordinates $\tilde{u}$ to the camera coordinates $X$:

$$
\tilde{u} = K X \quad \Rightarrow \quad X = K^{-1} \tilde{u}
$$
*(Note: Scale factors $z_l, z_r$ are omitted here as they are non-zero and the equation is homogeneous)*

For the left and right cameras:
* Left: $X_l = K_l^{-1} \tilde{u}_l$
* Right: $X_r = K_r^{-1} \tilde{u}_r$

### Derivation
Substitute these into the Essential Matrix equation ($X_l^T E X_r = 0$):

$$
(K_l^{-1} \tilde{u}_l)^T E (K_r^{-1} \tilde{u}_r) = 0
$$

Applying the transpose rule $(AB)^T = B^T A^T$:

$$
\tilde{u}_l^T K_l^{-T} E K_r^{-1} \tilde{u}_r = 0
$$

### Definition of Fundamental Matrix
We define the term in the middle as the **Fundamental Matrix $F$**:

$$
F = K_l^{-T} E K_r^{-1}
$$

So, the relationship in terms of image (pixel) coordinates is:

$$
\tilde{u}_l^T F \tilde{u}_r = 0
$$

### Relationship between $E$ and $F$
Conversely, if we know $F$ and the intrinsic parameters, we can recover $E$:

$$
E = K_l^T F K_r
$$
