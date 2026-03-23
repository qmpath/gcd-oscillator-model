def read_sweep_csv(file_path):
    """Reads a sweep CSV file and returns the data as a list of dictionaries."""
    import csv
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]


def filter_by_gcd(data, gcd_threshold):
    """Filters the sweep data based on the gcd threshold."""
    return [entry for entry in data if float(entry['gcd']) >= gcd_threshold]


def compute_stability(data):
    """Computes stability metrics for the given data."""
    stability_metrics = {}  # Initialize metrics dictionary
    # Example calculations:
    stability_metrics['mean'] = sum(float(entry['value']) for entry in data) / len(data)
    stability_metrics['std_dev'] = (sum((float(entry['value']) - stability_metrics['mean'])**2 for entry in data) / len(data))**0.5
    return stability_metrics


def summary_stats(data):
    """Computes summary statistics of the sweep data."""
    stats = {
        'count': len(data),
        'average': sum(float(entry['value']) for entry in data) / len(data) if len(data) > 0 else 0,
    }
    return stats
