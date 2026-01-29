# Week 02 - Numerical Verification of Gauss's Law Using Surface Integration

## Objective
The objective of this project is to numerically verify Gauss's law by computing the electric flux through differently shaped closed surfaces. The surface integrals will be computed by using discrete area elements \( dA \), and the convergence behaviour from Riemann summation will be investigated with increasing surface resolution through python.

For each simulation, a point charge of 5 pC will be placed within different Gaussian surfaces. According to Gauss's law, the total electric flux through surface enclosing a charge is:

$$
\Phi_E = \frac{Q}{\varepsilon_0}
$$

For a given charge of 5 pC, the theoratical value of the total electric flux is 564.717 Vm.

4 different scenarios will be examined through this experiment:

- A cube with a point charge at the center

- A cube with a point charge near the surface

- A sphere

- Irregular closed surface

## Observations
Cube - Centered Charge: At minimal division count, the calculated electric flux deviated the furthest compared to the rest of the points. As number of divisions increased, this calculation stabilized, steadily converging towards our controlled electric flux. At the higher division counts, change in our flux appears to be smaller. However, this slow increase still persists the convergence towards our numerical flux value.

 Cube - Off Centered Charge: The fewest division count displayed a much closer calculation of the flux than that of the least observed in the center charge cube. This was not maintained as the flux calculated at ten divisions exhibits clear deviation compared to the patterned convergence that higher points share.
## Explanations


## Limitations


## Conclusion


-----
## Contributors

**Won Lee** - Code Development, Graphical Analysis, Numerical Simulation

**Ron Macarilay**

## References

Matplotlib Document - https://matplotlib.org/

NumPy Document - https://numpy.org/devdocs/reference/routines.html
