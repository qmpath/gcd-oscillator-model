# GCD Oscillator Model
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19167512.svg)](https://doi.org/10.5281/zenodo.19167512)

A minimalist geometric model of three coupled oscillators moving on orthogonal torus knots. The model reveals that the greatest common divisor (GCD) of the spin differences acts as a topological invariant—the **Magic Maslov Number**—governing the system’s robustness to geometric perturbations. Integer spins exhibit boson‑like coherence (topological protection), while half‑integer spins show fermion‑like fragility.

This repository contains all simulation code, analysis scripts, and data required to reproduce the results of the paper:
The GCD Oscillator Model: Rational Geometric Protection in a Three‑Torus Network, Preprint, 2026, 10.5281/zenodo.19167512.
(preprint available at Zenodo)---

## Repository Structure

gcd-oscillator-model/
├── README.md
├── LICENSE
├── requirements.txt
├── src/
│   ├── simulation.py
│   └── utils.py
├── interactive/
│   └── applet.py
├── notebooks/
│   └── stability_analysis.ipynb
├── data/
│   └── stability_data.csv
└── figures/
    ├── fig1_stability.png
    ├── fig2_heatmap.png
    └── ...
