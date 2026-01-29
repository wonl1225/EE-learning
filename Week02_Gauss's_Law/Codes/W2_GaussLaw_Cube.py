import numpy as np
import matplotlib.pyplot as plt

# Constants
e0 = 8.854e-12  # ε0
Q = 5e-9        # Controlled charge, 5nC
L = 1.0         # Length of a cube, 1 m

# Function for flux calculation
def flux_calculation(position_charge, div):
    """
    This function executes flux calculation for the cubic Gaussian surface using integration.
    Method of Riemann sum was to approximate E · dA for all the 6 sides of the cube.
    
    :param position_charge: Position of the charge in a 3-dimensional space, indicated with (x, y, z) coordinates
    :param div: number of divisions on one side
    """

    # Total flux counter
    flux = 0.0

    # dA is defined as one tiny area
    # Area in the cube is defined as L**2, perform division with div to calculate the tiny area dA
    dA = (L/div)**2

    # np.linspace generates grids in a space, which will be used for contour integration
    x_value = np.linspace(-L/2, L/2, div)       # L/2 since the charge is at the center
    y_value = np.linspace(-L/2, L/2, div)

    # x = ± L/2
    for i in [1, -1]:           # Positive and negative sides of the x
        x = i * L/2             # fixed x position

        # Loop through dA on the x face
        for y in y_value:                   # Split into y-direction
            for z in y_value:               # Split into z-direction

                # Position vector from charge -> surface point
                rx = x - position_charge[0]
                ry = y - position_charge[1]
                rz = z - position_charge[2]

                # Calculate the magnitude of a distance from charge -> surface point
                r = np.sqrt(rx**2 + ry**2 + rz**2)

                # Electric field directed to x-axis, calculated using the Coulomb's law
                Ex = (Q*rx/(4*np.pi*e0))/ r**3

                # Add flux count
                # i prevents flux from cancelling out by multiplying Ex with equal signs
                flux += Ex*i*dA

    # y = ± L/2
    for i in [1, -1]:           # Positive and negative sides of the y
        y = i * L/2       # fixed y position

        # Loop through dA on the y face
        for x in x_value:
            for z in y_value:

                rx = x - position_charge[0]
                ry = y - position_charge[1]
                rz = z - position_charge[2]

                r = np.sqrt(rx**2 + ry**2 + rz**2)

                # Electric field directed to y-axis, calculated using the Coulomb's law
                Ey = (Q*ry/(4*np.pi*e0))/ r**3

                flux += Ey*i*dA

    # z = ± L/2
    for i in [1, -1]:            # Positive and negative sides of the y
        z = i * L/2              # fixed z position

        for x in x_value:
            for y in y_value:
                rx = x - position_charge[0]
                ry = y - position_charge[1]
                rz = z - position_charge[2]

                r = np.sqrt(rx**2 + ry**2 + rz**2)

                # Electric field directed to z-axis, calculated using the Coulomb's law
                Ez = (Q*rz/(4*np.pi*e0))/ r**3

                flux += Ez*i*dA

    return flux


# Simulation
divs = range(5, 105, 5)     # Sampled at various resolutions
theo = Q / e0               # Theoratical electric flux calculated through Gauss's law, 564.717 Vm

centered = []               # Empty list for centered charge
off_centered = []           # Empty list for off-centered charge

# Position of the charge
pos_center = np.array([0.0, 0.0, 0.0])      # Right at the center
pos_off = np.array([0.45, 0.45, 0.45])         # Off by 0.45, which is very close to a surface

# Integration
for div in divs:
    centered.append(flux_calculation(pos_center, div))
    off_centered.append(flux_calculation(pos_off, div))


# Plot the executed results
plt.plot(divs, centered, 'o-', label='centered', color='blue')
plt.plot(divs, off_centered, 'x--', label='off-centered', color='red')

# plt.axhline adds a horizontal reference line, y = theoratical
plt.axhline(theo, linestyle='--', label='Φ', color='black')

plt.xlabel('Divisions')
plt.ylabel('Electric Flux')

plt.legend()
plt.grid()

plt.savefig("GaussLaw_Cube.png", dpi=300)

# Print Errors for the highest resolution
error = abs(off_centered[-1] - theo) / theo * 100
print(f"Percentage error of off-centered charge at divs = 100: {error:.2f}%")


plt.show()