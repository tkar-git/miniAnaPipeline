import csv
import matplotlib.pyplot as plt
from pathlib import Path

<<<<<<< HEAD
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
=======
def analyze_data():
    r, theta, phi = [], [], []

    file_path = Path(__file__).parent / "data.csv"

    with open(file_path) as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  #Header skip

        for row in reader:
            r.append(float(row[0]))
            theta.append(float(row[1]))
            phi.append(float(row[2]))

    plt.figure(figsize=(8, 5))
    plt.boxplot([r, theta, phi], tick_labels=["r", "theta", "phi"])
    plt.title("Boxplot der Koordinaten")
    plt.ylabel("Wert")
    plt.grid(axis="y", linestyle="--", alpha=0.3)
    plt.tight_layout()
    plt.show()

analyze_data()
>>>>>>> db2a398d4104af748b9b094cbfb7726d09f17130
