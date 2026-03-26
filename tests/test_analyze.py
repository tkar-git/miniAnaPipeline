import pytest
import numpy as np
import matplotlib.pyplot as plt
from analyze import load_data, calculate_means, create_plot

@pytest.fixture
def sample_data(tmp_path):
    """Baut eine gültige Fake-CSV für Standard-Tests."""
    test_file = tmp_path / "test.csv"
    test_file.write_text("r,theta,phi\n10,0.1,0.2\n20,0.2,0.4")
    return load_data(test_file)

# --- Erfolgs-Tests (Happy Path) ---

def test_calculate_means(sample_data):
    res = calculate_means(sample_data)
    assert res['r'] == 15.0
    assert res['theta'] == pytest.approx(0.15)
    assert res['phi'] == pytest.approx(0.30)

def test_plot_generation(sample_data):
    means = calculate_means(sample_data)
    fig = create_plot(sample_data, means)
    assert fig is not None
    assert len(fig.axes) == 2
    plt.close(fig)

# --- Fehler-Tests (Edge Cases) ---

def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_data("nirgendwo.csv")

def test_wrong_headers(tmp_path):
    bad_file = tmp_path / "bad.csv"
    bad_file.write_text("x,y,z\n10,0.1,0.2")
    with pytest.raises(KeyError):
        load_data(bad_file)