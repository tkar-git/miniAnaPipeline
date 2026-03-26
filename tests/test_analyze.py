import pytest
import numpy as np
from analyze import load_data  
@pytest.fixture
def sample_data(tmp_path):
    """Erstellt die Fake-Datei, lädt sie und stellt die Daten bereit."""
    test_file = tmp_path / "test.csv"
    test_file.write_text("r,theta,phi\n10,0.1,0.2\n20,0.2,0.4")
    return load_data(test_file)


def test_data_structure(sample_data):
    """Prüft, ob die Daten im richtigen Format aus der CSV kommen."""
    assert sample_data == {'r': [10.0, 20.0], 'theta': [0.1, 0.2], 'phi': [0.2, 0.4]}

def test_mean_r(sample_data):
    """Prüft nur die Berechnung von 'r'."""
    assert np.mean(sample_data['r']) == 15.0

def test_mean_theta(sample_data):
    """Prüft die Berechnung von 'theta' (mit Toleranz für Kommazahlen)."""
    assert np.mean(sample_data['theta']) == pytest.approx(0.15)

def test_mean_phi(sample_data):
    """Prüft die Berechnung von 'phi' (mit Toleranz für Kommazahlen)."""
    assert np.mean(sample_data['phi']) == pytest.approx(0.30)