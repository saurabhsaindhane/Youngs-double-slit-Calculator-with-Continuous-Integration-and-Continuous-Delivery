import tkinter as tk
class YoungsDoubleSlitCalculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Young's Double Slit Calculator")
        self.root.geometry("400x200")

        self.label1 = tk.Label(self.root, text="Enter values for the following parameters:")
        self.label1.pack()

        self.label2 = tk.Label(self.root, text="Wavelength of light (nm):")
        self.label2.pack()
        self.entry1 = tk.Entry(self.root)
        self.entry1.pack()

        self.label3 = tk.Label(self.root, text="Distance between slits (mm):")
        self.label3.pack()
        self.entry2 = tk.Entry(self.root)
        self.entry2.pack()

        self.label4 = tk.Label(self.root, text="Distance to the screen (m):")
        self.label4.pack()
        self.entry3 = tk.Entry(self.root)
        self.entry3.pack()

        self.button1 = tk.Button(self.root, text="Calculate", command=self.calculateYoungsDoubleSlit)
        self.button1.pack()

    def calculateYoungsDoubleSlit(self):
        wavelength = float(self.entry1.get())
        slit_distance = float(self.entry2.get()) / 1000
        screen_distance = float(self.entry3.get())

        # Calculation of Young's Double Slit Formula
        diffraction_pattern = (wavelength * screen_distance) / (slit_distance * 10 ** -3)
        self.result_label = tk.Label(self.root, text=f"Diffraction Pattern Width: {diffraction_pattern:.2f} mm")
        self.result_label.pack()


class CoefficientOfViscosityCalculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Coefficient of Viscosity Calculator")
        self.root.geometry("400x200")

        self.label1 = tk.Label(self.root, text="Enter values for the following parameters:")
        self.label1.pack()

        self.label2 = tk.Label(self.root, text="Density of liquid (kg/m^3):")
        self.label2.pack()
        self.entry1 = tk.Entry(self.root)
        self.entry1.pack()

        self.label3 = tk.Label(self.root, text="Sphere radius (m):")
        self.label3.pack()
        self.entry2 = tk.Entry(self.root)
        self.entry2.pack()

        self.label4 = tk.Label(self.root, text="Terminal velocity (m/s):")
        self.label4.pack()
        self.entry3 = tk.Entry(self.root)
        self.entry3.pack()

        self.button2 = tk.Button(self.root, text="Calculate", command=self.calculateCoefficientOfViscosity)
        self.button2.pack()

    def calculateCoefficientOfViscosity(self):
        density = float(self.entry1.get())
        radius = float(self.entry2.get())
        velocity = float(self.entry3.get())

        # Calculation of Coefficient of Viscosity Formula
        viscosity_coefficient = (2 * density * radius ** 2 * velocity) / 9
        self.result_label = tk.Label(self.root, text=f"Viscosity Coefficient: {viscosity_coefficient:.2f} Pa*s")
        self.result_label.pack()

import tkinter as tk

class RocketVelocityCalculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Rocket Velocity Calculator")
        self.root.geometry("400x200")

        self.label1 = tk.Label(self.root, text="Enter values for the following parameters:")
        self.label1.pack()

        self.label2 = tk.Label(self.root, text="Thrust of rocket (N):")
        self.label2.pack()
        self.entry1 = tk.Entry(self.root)
        self.entry1.pack()

        self.label3 = tk.Label(self.root, text="Mass of rocket (kg):")
        self.label3.pack()
        self.entry2 = tk.Entry(self.root)
        self.entry2.pack()

        self.label4 = tk.Label(self.root, text="Time of burn (s):")
        self.label4.pack()
        self.entry3 = tk.Entry(self.root)
        self.entry3.pack()

        self.button1 = tk.Button(self.root, text="Calculate", command=self.calculateRocketVelocity)
        self.button1.pack()

    def calculateRocketVelocity(self):
        thrust = float(self.entry1.get())
        mass = float(self.entry2.get())
        time = float(self.entry3.get())

        # Calculation of rocket velocity formula
        velocity = (thrust * time) / mass
        self.result_label = tk.Label(self.root, text=f"Rocket Velocity: {velocity:.2f} m/s")
        self.result_label.pack()


# Creating instance of RocketVelocityCalculator class
rocket_velocity = RocketVelocityCalculator()

# Main event loop



# Creating instance of YoungsDoubleSlitCalculator and CoefficientOfViscosityCalculator classes
youngs_double_slit = YoungsDoubleSlitCalculator()
coefficient_of_viscosity = CoefficientOfViscosityCalculator()

# Main event loop
youngs_double_slit.root.mainloop()
