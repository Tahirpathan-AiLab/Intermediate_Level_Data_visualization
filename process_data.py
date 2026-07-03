import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import utilities.plot_settings 


# ==========================================================
# Export Settings
# ==========================================================

SAVE_PATH = Path(
    r"C:\Users\tanvi\OneDrive\Desktop\Pathan Tahirkhan Aarifkhan\intermediate_level_data_visualization\report\figurs"
)


def export_plot(fig, dpi=300):
    """Automatically save figure as figure_1.png, figure_2.png, ..."""

    SAVE_PATH.mkdir(parents=True, exist_ok=True)

    i = 1
    while (SAVE_PATH / f"figure_{i}.png").exists():
        i += 1

    file_path = SAVE_PATH / f"figure_{i}.png"

    fig.savefig(file_path, dpi=dpi, bbox_inches="tight")

    print(f"Figure saved successfully:\n{file_path}")


# ==========================================================
# Read Excel Files
# ==========================================================

data_2020 = pd.read_excel("data/raw/fsi-2020.xlsx")
data_2021 = pd.read_excel("data/raw/fsi-2021.xlsx")

# ==========================================================
# Process 2020
# ==========================================================

subset_2020 = data_2020.iloc[:, :3]

subset_2020 = pd.merge(
    subset_2020,
    data_2020["Change from Previous Year"],
    left_index=True,
    right_index=True,
)

# ==========================================================
# Process 2021
# ==========================================================

subset_2021 = data_2021.iloc[:, :3]

subset_2021 = pd.merge(
    subset_2021,
    data_2021["X1: External Intervention"],
    left_index=True,
    right_index=True,
)

# ==========================================================
# Rename Columns
# ==========================================================

col_names = [
    "index",
    "Country",
    "Year",
    "improvment",
]

subset_2020.columns = col_names
subset_2021.columns = col_names

# ==========================================================
# Save Processed Data
# ==========================================================

subset_2020.to_pickle("data/processed/processed_data_2020.pkl")
subset_2021.to_pickle("data/processed/processed_data_2021.pkl")

# ==========================================================
# Load Processed Data
# ==========================================================

df_1 = pd.read_pickle("data/processed/processed_data_2020.pkl")
df_2 = pd.read_pickle("data/processed/processed_data_2021.pkl")

# ==========================================================
# Combine Data
# ==========================================================

merged = pd.concat([df_1, df_2], axis=1)

# ==========================================================
# Plot
# ==========================================================

fig, ax = plt.subplots(figsize=(15, 4.5))

merged["improvment"].plot(ax=ax, linewidth=2, label="Improvement")

ax.set_title("Improvement Chart")
ax.set_xlabel("Index")
ax.set_ylabel("Improvement")

ax.set_ylim(-10, 10)

ax.grid(True, linestyle="--", alpha=0.5)

ax.legend(loc="upper left", bbox_to_anchor=(1.02, 1))

plt.tight_layout()

# ==========================================================
# Export Figure
# ==========================================================

export_plot(fig)

# ==========================================================
# Show Figure
# ==========================================================

plt.show()
