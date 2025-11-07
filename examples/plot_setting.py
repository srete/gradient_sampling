import matplotlib.pyplot as plt
from cycler import cycler
# import seaborn as sns


def set_plot_style():

    plt.rcParams.update({
        # --- Fonts ---
        #"font.family": "serif",
        #"font.serif": ["Times New Roman", "Times", "DejaVu Serif"],
        "font.size": 10.5,
        "axes.labelsize": 10.5,
        "axes.titlesize": 11,
        "xtick.labelsize": 9.5,
        "ytick.labelsize": 9.5,
        "legend.fontsize": 9.5,

        # --- Figure ---
        "figure.figsize": (5, 4),
        "figure.dpi": 100,
        "savefig.dpi": 300,
        "figure.autolayout": True,

        # --- Line and grid style ---
        "axes.prop_cycle": cycler(color=plt.cm.tab10.colors), # cycler(color=plt.cm.Set2.colors),
        "lines.linewidth": 1.5,
        "axes.grid": True,
        "grid.linestyle": ":",
        "grid.alpha": 0.4,

        # --- Spectrograms / images ---
        "image.cmap": "magma",
        "image.interpolation": "none",
        "image.origin": "lower",

        # --- Colorbar and ticks ---
        "axes.titlepad": 6,
        "xtick.direction": "in",
        "ytick.direction": "in",
    })
