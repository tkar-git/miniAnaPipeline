import csv
import matplotlib.pyplot as plt
import numpy as np

# Baustein 1: Nur für das Einlesen zuständig
def load_data(file_path):
    """Lädt die CSV-Datei und extrahiert die Spalten r, theta und phi."""
    with open(file_path, 'r', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
        # Wenn eine Spalte wie 'r' fehlt, wirft das einen KeyError. 
        # (Genau das, was wir in test_wrong_headers prüfen!)
        return {k: [float(r[k]) for r in rows] for k in ['r', 'theta', 'phi']}

# Baustein 2: NEU - Nur für die Mathematik zuständig (perfekt testbar!)
def calculate_means(data):
    """Berechnet die Mittelwerte für die übergebenen Daten."""
    return {
        'r': np.mean(data['r']),
        'theta': np.mean(data['theta']),
        'phi': np.mean(data['phi'])
    }

# Baustein 3: Nur für die Optik zuständig
def create_plot(data, means):
    """Erstellt die Grafik. Erwartet die rohen Daten UND die fertigen Mittelwerte."""
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

        # Mittelwerte einzeichnen (wir nutzen jetzt das übergebene 'means' Dictionary!)
        for i, key in enumerate(keys, start=1):
            mean_val = means[key]
            ax.plot(i, mean_val, 'ro')
            ax.text(i + 0.1, mean_val, f' Mean: {mean_val:.2f}', color='red', va='center', weight='bold')

    plt.tight_layout()
    return fig

# Der Ausführungs-Block (Wird von pytest komplett ignoriert)
if __name__ == "__main__":
    try:
        # Hier greifen die drei Bausteine wie Zahnräder ineinander
        my_data = load_data('processed.csv')
        my_means = calculate_means(my_data)
        final_fig = create_plot(my_data, my_means)
        plt.show()
    except FileNotFoundError:
        print("Fehler: Die Datei 'processed.csv' wurde nicht gefunden.")
    except KeyError as e:
        print(f"Fehler: Die benötigte Spalte {e} fehlt in der CSV-Datei.")