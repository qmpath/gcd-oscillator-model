#!/usr/bin/env python3
"""analyze_sweep.py - Plot harmonic distribution from sweep CSV"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

def load_and_plot(csv_path):
    if not csv_path:
        print("Usage: python src/analyze_sweep.py <csv_file>\n")
        print("Example: python src/analyze_sweep.py immunity_test_results.csv")
        sys.exit(1)
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        print(f"ERROR: File not found: {csv_path}")
        sys.exit(1)
    if 'GCD' not in df.columns or 'Period' not in df.columns:
        print(f"ERROR: CSV must have 'GCD' and 'Period' columns. Found: {df.columns.tolist()}")
        sys.exit(1)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    for gcd_val in sorted(df['GCD'].unique()):
        subset = df[df['GCD'] == gcd_val]['Period']
        ax1.hist(subset, alpha=0.6, label=f'GCD={gcd_val}', bins=10)
    ax1.set_xlabel('Period (s)', fontweight='bold')
    ax1.set_ylabel('Frequency', fontweight='bold')
    ax1.set_title('Period Distribution by GCD')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    grouped = df.groupby('GCD')['Period'].agg(['mean', 'std'])
    ax2.errorbar(grouped.index, grouped['mean'], yerr=grouped['std'], fmt='o-', capsize=5)
    ax2.set_xlabel('GCD', fontweight='bold')
    ax2.set_ylabel('Mean Period (s)', fontweight='bold')
    ax2.set_title('Mean Period vs. GCD')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('harmonic_distribution.png', dpi=300)
    plt.show()
    print("Saved: harmonic_distribution.png")

if __name__ == '__main__':
    csv_file = sys.argv[1] if len(sys.argv) > 1 else None
    load_and_plot(csv_file)