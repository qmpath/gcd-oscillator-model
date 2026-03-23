#!/usr/bin/env python3
"""collapse_example.py - Figure 4: CO-Bridge Period vs Thickness"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

R, p, q = 2.5, 2, 1
dt, steps = 0.001, 20000
sr, sb, sg = 2, -1, 3
r_values = np.linspace(0.1, 1.2, 12)

def get_position(angle, mode, r_val):
    theta, phi = p*angle, q*angle
    radius = R + r_val*np.cos(theta)
    x = radius*np.cos(phi)
    y = radius*np.sin(phi)
    z = r_val*np.sin(theta)
    if mode == 'r': return np.array([x, y, z])
    if mode == 'b': return np.array([z, y, -x])
    return np.array([x, z, -y])

def simulate_with_r(current_r):
    t = np.arange(steps)*dt
    pr = get_position(sr*t, 'r', current_r)
    pb = get_position(sb*t, 'b', current_r)
    pg = get_position(sg*t, 'g', current_r)
    d_rb = np.linalg.norm(pr-pb, axis=0)
    d_rg = np.linalg.norm(pr-pg, axis=0)
    d_bg = np.linalg.norm(pb-pg, axis=0)
    max_d = np.maximum(d_rb, np.maximum(d_rg, d_bg))
    y = max_d - np.mean(max_d)
    fft_vals = np.abs(fft(y)[:steps//2])
    freqs = fftfreq(steps, dt)[:steps//2]
    return 1/freqs[np.argmax(fft_vals[1:])+1]

if __name__ == '__main__':
    print("CO-Bridge: Period vs. Torus Thickness\n")
    results = [simulate_with_r(rv) for rv in r_values]
    plt.figure(figsize=(10, 6))
    plt.plot(r_values, results, 'o-', color='darkcyan', markersize=10)
    plt.axhline(y=2*np.pi, color='r', linestyle='--', label='Theoretical (2π)')
    plt.xlabel('Torus Thickness (r)', fontweight='bold')
    plt.ylabel('Period (s)', fontweight='bold')
    plt.title('CO-Bridge Verdict: Period vs. Thickness')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.savefig('collapse_example_output.png', dpi=300)
    plt.show()
    df = pd.DataFrame({'r': r_values, 'period': results})
    df.to_csv('collapse_example_results.csv', index=False)
    print("Saved: collapse_example_output.png, collapse_example_results.csv")