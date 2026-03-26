import csv
import matplotlib.pyplot as plt
import numpy as np

def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
        # Extrahiert alle Spalten in einem Rutsch
        return {k: [float(r[k]) for r in rows] for k in ['r', 'theta', 'phi']}

def create_plot(data):
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    panels = [(['r'], "Werte"), (['theta', 'phi'], "Winkel")]

    for ax, (keys, title) in zip(axes, panels):
        d_list = [data[k] for k in keys]
        
        # Plot und Design in einem Schritt
        ax.boxplot(d_list, tick_labels=keys, patch_artist=True, 
                   boxprops=dict(facecolor='white'),
                   medianprops=dict(color='black', linewidth=2))
        
        ax.set(facecolor='#EBEBEB', title=title)
        ax.grid(True, color='white')

        # Mittelwerte einzeichnen
        for i, vals in enumerate(d_list, start=1):
            mean_val = np.mean(vals)
            ax.plot(i, mean_val, 'ro')
            ax.text(i + 0.1, mean_val, f' Mean: {mean_val:.2f}', color='red', va='center', weight='bold')

    plt.tight_layout()
    return fig

if __name__ == "__main__":
    try:
        create_plot(load_data('processed.csv'))
        plt.show()
    except FileNotFoundError:
        print("Fehler: 'processed.csv' nicht gefunden.")
