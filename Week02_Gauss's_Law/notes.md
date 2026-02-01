# Week 02 - Numerical Verification of Gauss's Law Using Surface Integration

## Objective
The objective of this project is to numerically verify Gauss's law by computing the electric flux through differently shaped closed surfaces. The surface integrals will be computed by using discrete area elements \( dA \), and the convergence behaviour from Riemann summation will be investigated with increasing surface resolution through python.

For each simulation, a point charge of 5 nC will be placed within different Gaussian surfaces. According to Gauss's law, the total electric flux through surface enclosing a charge is:

$$
\Phi_E = \frac{Q}{\varepsilon_0}
$$

For a given charge of 5 nC, the theoratical value of the total electric flux is 564.717 Vm.

3 different scenarios will be examined through this experiment:

- A cube with a point charge at the center

- A cube with a point charge near the surface

- Outside of Cube Charge

## Observations
Cube - Centered Charge:

At minimal division count, the calculated electric flux deviated the furthest compared to the rest of the points. The relative convergence is an underestimation. As number of divisions increased, this calculation stabilized, steadily converging towards our controlled electric flux. At the higher division counts, change in our flux appears to be smaller. However, this slow increase still persists the convergence towards our numerical flux value.

Cube - Off Centered Charge:

The fewest division count displayed a much closer calculation of the flux than that of the least observed in the center charge cube. This was not maintained as the flux calculated at ten divisions exhibits clear deviation compared to the patterned convergence that higher points share. The relative convergence of this scenario started at an overestimation. The higher divisions show little change in flux, similar to the cube centered charge.

Outside of Cube Charge:

For all division points, the calculated flux is zero. There is no deviation in this value.
## Explanations
Surface divisions represents the number of fixed areas of the cube used to approximate the electric flux within the closed surface. When divisions are low, the calculated flux within that region becomes inaccurate. This does not take into account the asymmetric electric field distribution. In terms of fields, for example, an area closer to the corner of the cube takes in less of the field than an area of the same dimension that is in the surface center. The variation of the field is not calculated for, This phenomenon is called aliasing. 

This occurence severely deviated the ten point division in the off centered cube data. Due to aliasing, the bigger grid of calculation fails to recognize the steep electric field of the surface closest to the charge. This caused the high field density of this surface to be misrepresented in the Riemann sum, resulting in an underestimation.

At mid to high point divisions, the flux calculation stabilizes and converges towards the fixed value. This indicates an improved numerical accuracy. This simulation proves Gauss's law by Riemann sum. It takes divisions instead of an infinitesimal change in area using the formula:

$$
\oint_{\partial V} \mathbf{E} \cdot d\mathbf{A} = \frac{Q_{\text{enc}}}{\varepsilon_0}
$$

This convergence towards $$\frac{Q_{\text{enc}}}{\varepsilon_0}$$ , is proof enough of gauss's law as we see it approximate closer and closer towards a continuous surface integral.

When the charge is in the center of the cube, the approximation occurs more rapidly. This is due to a more uniform field distribution and its fair symmetry compared to the other scenarios. When the charge is off centered, sharper increases and decreases of field per area makes approximation more difficult to converge. A charge outside of our designated cube has a net zero flux through all tested divisions. This proves that the charge's field passes through the gaussian surface and exits through the opposite side. This means a net zero flux on a surface can't disprove the existence of the charge. In this scenario, Gauss's law cannot work due to one of its requirements being broken, there is no charge enclosed by the cube.

## Limitations


## Conclusion


-----
## Contributors

**Won Lee** - Code Development, Graphical Analysis, Numerical Simulation

**Ron Macarilay**

## References

Matplotlib Document - https://matplotlib.org/

NumPy Document - https://numpy.org/devdocs/reference/routines.html
