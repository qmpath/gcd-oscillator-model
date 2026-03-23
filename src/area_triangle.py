import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Pool

def triangle_area(v1, v2, v3):
    a = np.linalg.norm(v2 - v1)
    b = np.linalg.norm(v3 - v1)
    c = np.linalg.norm(v3 - v2)
    s = (a + b + c) / 2
    return np.sqrt(s * (s - a) * (s - b) * (s - c))

def stability_simulation(triangle_vertices, num_samples=1000):
    areas = []
    for _ in range(num_samples):
        area = triangle_area(*triangle_vertices)
        areas.append(area)
    return areas

def fft_analysis(data):
    return np.fft.fft(data)

def main():
    vertices = [np.array([0, 0]), np.array([1, 0]), np.array([0.5, np.sqrt(3)/2])]
    with Pool() as pool:
        areas = pool.map(stability_simulation, [vertices]*10)
    # Flatten the list of areas
    flat_areas = [area for sublist in areas for area in sublist]
    fft_result = fft_analysis(flat_areas)
    
    # Plotting results
    plt.plot(np.abs(fft_result))
    plt.title('FFT of Triangle Area Stability Simulation')
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()