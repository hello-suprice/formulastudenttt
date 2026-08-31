'''
KTH Formula Student Driverless - Exercise 2: Visualisation
Student: Nader

Syfte:
Enkelt visualiseringsverktyg med OOP för att plotta funktionen:
h(t) = 3*pi * exp(-5 * sin(2*pi*t))
'''

import numpy as np
import matplotlib.pyplot as plt


class BasePlotter:
    '''
    Basklass som skapar figurfönstret och sätter grundlayout.
    '''
    def __init__(self, title="Plott"):
        self.fig, self.ax = plt.subplots()
        self.ax.set_title(title)
        self.ax.set_xlabel("Tid t [s]")
        self.ax.set_ylabel("h(t)")
        self.ax.grid(True)

    def show(self):
        plt.show()


class FunctionPlotter(BasePlotter):
    '''
    Subklass som räknar ut matematiken och ritar grafen.
    '''
    def __init__(self, t_start=0.0, t_slut=3.0):
        super().__init__(title="Plottning av h(t)")
        # Skapa en tidsvektor med 500 punkter
        self.t = np.linspace(t_start, t_slut, 500)

    def calculate_h(self):
        '''
        Beräknar lambda(t) och h(t).
        '''
        lambda_t = 5.0 * np.sin(2.0 * np.pi * 1.0 * self.t)
        h_t = 3.0 * np.pi * np.exp(-lambda_t)
        return h_t

    def plot_data(self):
        '''
        Ritar upp kurvan.
        '''
        h = self.calculate_h()
        self.ax.plot(self.t, h, label="h(t)", color="red")
        self.ax.legend()


# Kör programmet
if __name__ == "__main__":
    plotter = FunctionPlotter(t_start=0.0, t_slut=3.0)
    plotter.plot_data()
    plotter.show()