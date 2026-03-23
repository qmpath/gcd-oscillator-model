import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.fft import fft

# Function to compute periods
def compute_period(data):
    n = len(data)
    yf = fft(data)
    xf = np.linspace(0.0, 1.0/(2.0*(1/n)), n//2)
    period = np.argmax(np.abs(yf[:n // 2]))  # Get the period from the FFT
    return period

# Parameters
spin_triples = np.linspace(0, 10, 100)  # Example range for spin triples
torus_thickness = np.linspace(0.1, 5, 100)  # Example range for torus thickness
periods = np.zeros((len(spin_triples), len(torus_thickness)))

# Compute periods across parameter space
for i, spin in enumerate(spin_triples):
    for j, thickness in enumerate(torus_thickness):
        # Example computation - replace this with your specific model's computation
        data = np.sin(np.linspace(0, 10 + spin, 100) / thickness)  # Placeholder data
        periods[i, j] = compute_period(data)

# Create heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(periods, cmap='YlGnBu', xticklabels=10, yticklabels=10)
plt.title("Period Stability across GCD Values")
plt.xlabel("Torus Thickness")
plt.ylabel("Spin Triples")
plt.colorbar(label='Computed Period')
plt.savefig('CMTHeatmap.png')  # Optional: save heatmap image
plt.show()