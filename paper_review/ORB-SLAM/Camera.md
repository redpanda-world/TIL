# Forward Imaging Model & Camera Calibration

## 1. Overview of Forward Imaging Model

**Point P is projected onto Image Plane.**
The complete mapping process where a 3D point $P$ is projected onto a 2D image plane is called the **Forward Imaging Model**.

<img width="735" height="518" alt="image" src="https://github.com/user-attachments/assets/65334719-55b3-4520-b2c4-967a4e41e11e" />

### Coordinate Transformation
The process of transforming World Coordinates to Pixel Coordinates is as follows:

1.  **World Coordinate** $X_w = (x_w, y_w, z_w)^T$
    * $\Downarrow$ Coordinate Transformation (Extrinsic Parameters)
2.  **Camera Coordinate** $X_c = (x_c, y_c, z_c)^T$
    * $\Downarrow$ Perspective Projection
3.  **Image Coordinate** $X_i = (x_i, y_i)^T$

### Perspective Projection
The projection from the Camera Coordinate system to the Image Plane is derived using similar triangles (Focal length: $f$).

$$
\frac{x_i}{f} = \frac{x_c}{z_c} \quad \text{and} \quad \frac{y_i}{f} = \frac{y_c}{z_c}
$$

Thus, the Image Coordinates $(x_i, y_i)$ are:

$$
x_i = f \frac{x_c}{z_c}, \quad y_i = f \frac{y_c}{z_c}
$$

---

## 2. Image Coordinate to Pixel Coordinate

We need to figure out the mapping from Image Coordinates (physical unit: mm) to Pixel Coordinates (digital unit: pixel).

<img width="780" height="519" alt="image" src="https://github.com/user-attachments/assets/cc8790b5-3325-4371-be23-a8515553ea4f" />

### Key Parameters
* **Image Plane**: $x_i, y_i$ (unit: mm)
* **Image Sensor**: $u, v$ (unit: pixel)
* **Principal Point $(o_x, o_y)$**: The point where the optical axis pierces the sensor.
* **Pixel Densities**: $m_x, m_y$ (pixels/mm)

### Mapping Equation
$$
\begin{aligned}
u &= m_x x_i + o_x = m_x f \frac{x_c}{z_c} + o_x \\
v &= m_y y_i + o_y = m_y f \frac{y_c}{z_c} + o_y
\end{aligned}
$$

Since individual parameters like $m_x$ and $f$ are unknown or hard to separate, we group them into single parameters.

> **Intrinsic Parameters**
> * $f_x = m_x f$
> * $f_y = m_y f$
> * $o_x, o_y$

Substituting these into the equation:
$$
u = f_x \frac{x_c}{z_c} + o_x, \quad v = f_y \frac{y_c}{z_c} + o_y
$$

---

## 3. Homogeneous Coordinates

Perspective Projection is essentially a **non-linear** transformation (due to division by $z_c$). To represent this as a **linear** transformation (Matrix Multiplication), we introduce **Homogeneous Coordinates**.

### Representation of a 2D Point
$$
u \rightarrow \tilde{u} = (\tilde{u}, \tilde{v}, \tilde{w})^T
$$
Here, $\tilde{w}$ represents a fictitious dimension. In the world of homogeneous coordinates:

$$
u = \begin{pmatrix} u \\ v \\ 1 \end{pmatrix} \equiv \begin{pmatrix} \tilde{w}u \\ \tilde{w}v \\ \tilde{w} \end{pmatrix} = \tilde{u}
$$

---

## 4. Matrix Formulation (Camera to Pixel)

We can express the equations above in matrix form.

<img width="765" height="519" alt="image" src="https://github.com/user-attachments/assets/53455556-0bf3-4796-8bd3-4dc64f75a528" />


### Homogeneous Coordinates of $(u, v)$

$$
u = m_x x_i + o_x = m_x f \frac{x_c}{z_c} + o_x
$$

$$
v = m_y y_i + o_y = m_y f \frac{y_c}{z_c} + o_y
$$

This vector can be decomposed into a matrix multiplication:

$$\begin{pmatrix} f_x x_c + z_c o_x \\ f_y y_c + z_c o_y \\ z_c \end{pmatrix} = \begin{pmatrix} f_x & 0 & o_x & 0 \\ 0 & f_y & o_y & 0 \\ 0 & 0 & 1 & 0 \end{pmatrix} \begin{pmatrix} x_c \\ y_c \\ z_c \\ 1 \end{pmatrix}$$

### Intrinsic Matrix (Calibration Matrix) $K$
We define the matrix $K$ containing only the camera's internal parameters:

$$
K = \begin{pmatrix}
f_x & 0 & o_x \\
0 & f_y & o_y \\
0 & 0 & 1
\end{pmatrix}
$$

### Final Equation
Finally, the relationship between Pixel Coordinate $\tilde{u}$ and Camera Coordinate $\tilde{X}_c$ is expressed as:

$$
\tilde{u} = (K | 0) \tilde{X}_c = M_{int} \tilde{X}_c
$$

* $\tilde{u}$: Pixel Coordinate (Homogeneous)
* $\tilde{X}_c$: Camera Coordinate (Homogeneous)
* $M_{int}$: Projection Matrix containing Intrinsic Parameters
