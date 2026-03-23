#!/usr/bin/env python3
"""sweepread.py - Utilities for reading and processing sweep data"""
import numpy as np
import pandas as pd

def read_sweep_csv(filepath):
    """Read sweep results CSV file."""
    return pd.read_csv(filepath)

def filter_by_gcd(df, gcd_value):
    """Filter sweep results by GCD value."""
    return df[df['GCD'] == gcd_value]

def compute_stability(df):
    """Compute stability metric (std/mean) for each GCD."""
    results = []
    for gcd_val in df['GCD'].unique():
        subset = df[df['GCD'] == gcd_val]['Period']
        mean_p = subset.mean()
        std_p = subset.std()
        stability = std_p / mean_p if mean_p > 0 else np.nan
        results.append({'GCD': gcd_val, 'Mean': mean_p, 'Std': std_p, 'Stability': stability})
    return pd.DataFrame(results)

def summary_stats(df):
    """Print summary statistics."""
    print("\n" + "="*60)
    print("SWEEP DATA SUMMARY")
    print("="*60)
    print(f"Total rows: {len(df)}")
    if 'GCD' in df.columns:
        print(f"Unique GCDs: {sorted(df['GCD'].unique())}")
    if 'Period' in df.columns:
        print(f"Period range: {df['Period'].min():.4f} - {df['Period'].max():.4f} s")
        print(f"Mean period: {df['Period'].mean():.4f} s")
        print(f"Std period: {df['Period'].std():.4f} s")
    print("="*60 + "\n")