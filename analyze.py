import csv
import matplotlib.pyplot as plt
import numpy as np

def analyze_data(file_path):
    # Wir laden alle 4 Spalten
    data_dict = {'r': [], 'theta': [], 'phi': []}
    
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            for key in data_dict.keys():
                data_dict[key].append(float(row[key]))
            
    return data_dict

# Daten laden
file_path = 'processed.csv'
data_dict = analyze_data(file_path)

# Wir teilen die Daten in zwei Gruppen auf, damit die Skalierung passt
groups = [
    ['r'], # Längenls
    ['theta', 'phi'] # Winkel
]

fig, axes = plt.subplots(1, 2, figsize=(12, 6)) # 1 Zeile, 2 Spalten
axes = axes.flatten()

for idx, group_keys in enumerate(groups):
    ax = axes[idx]
    
    # Daten für diese Gruppe extrahieren
    plot_data = [data_dict[k] for k in group_keys]
    
    # Boxplot
    bplot = ax.boxplot(plot_data, 
                       patch_artist=True, 
                       tick_labels=group_keys,
                       medianprops={'color': 'black', 'linewidth': 2})
    
    # Design-Anpassung (wie im Bild)
    ax.set_facecolor('#EBEBEB')
    ax.grid(True, color='white')
    ax.set_title("Werte" if idx == 0 else "Winkel")

    for i, patch in enumerate(bplot['boxes']):
        patch.set_facecolor('white')
        
        # Mittelwert berechnen und einzeichnen
        mean_val = np.mean(plot_data[i])
        ax.plot(i + 1, mean_val, 'ro', markersize=5)
        
        # Text-Label für Mean
        ax.text(i + 1, mean_val, f'  Mean: {mean_val:.2f}', 
                color='red', va='center', fontweight='bold')

plt.tight_layout()
plt.show()
