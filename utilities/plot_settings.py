import matplotlib.pyplot as plt


def set_plot_style():

    plt.style.use("ggplot")

    plt.rcParams.update(
        {
            # Figure
            "figure.figsize": (15, 5),
            "figure.dpi": 120,
            "figure.facecolor": "white",
            # Axes
            "axes.facecolor": "white",
            "axes.edgecolor": "black",
            "axes.linewidth": 1.2,
            "axes.grid": True,
            "axes.axisbelow": True,
            # Title
            "axes.titlesize": 18,
            "axes.titleweight": "bold",
            # Labels
            "axes.labelsize": 12,
            "axes.labelweight": "bold",
            # Grid
            "grid.color": "gray",
            "grid.linestyle": "--",
            "grid.linewidth": 0.6,
            "grid.alpha": 0.4,
            # Font
            "font.family": "DejaVu Sans",
            "font.size": 11,
            # Lines
            "lines.linewidth": 2.5,
            "lines.markersize": 6,
            # Legend
            "legend.frameon": True,
            "legend.fancybox": True,
            "legend.shadow": True,
            "legend.fontsize": 10,
            "legend.title_fontsize": 11,
            # Tick labels
            "xtick.labelsize": 10,
            "ytick.labelsize": 10,
            # Save Figure
            "savefig.dpi": 300,
            "savefig.bbox": "tight",
        }
    )
