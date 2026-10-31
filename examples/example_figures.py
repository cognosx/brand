"""Example: the same chart in the CognosX light and dark styles (data are illustrative)."""
import sys
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "python"))
import cognosx_brand as cx

years = np.arange(2014, 2024)
series = {"Infectious disease": [5, 6, 8, 9, 12, 14, 13, 15, 16, 12],
          "Bacterial genetics": [4, 5, 6, 8, 8, 10, 11, 11, 12, 9],
          "Antibiotic resistance": [2, 3, 4, 6, 7, 9, 10, 12, 14, 11],
          "Immunotherapy": [3, 3, 4, 4, 5, 5, 6, 6, 7, 5]}

for dark in (False, True):
    cx.use(dark=dark)
    fig, ax = plt.subplots(figsize=(7.2, 3.8))
    for name, ys in series.items():
        ax.plot(years, ys, label=name)
        ax.text(years[-1] + 0.25, ys[-1], name, va="center", fontsize=8.5,
                color=plt.rcParams["text.color"])
    ax.set_xlim(years[0], years[-1] + 3.2)
    ax.set_xticks(range(2014, 2024, 2))
    ax.set_ylabel("Grants per year")
    ax.set_title("Example chart in the CognosX style")
    ax.legend(loc="upper left", ncol=2)
    cx.credit(fig, dark=dark)
    cx.save(fig, "example_dark" if dark else "example_light", Path(__file__).parent, formats=("png",))
    plt.close(fig)
print("saved")
