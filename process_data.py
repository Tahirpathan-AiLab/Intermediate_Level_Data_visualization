import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import utilities.plot_settings

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
REPORT_DIR = ROOT / "report" / "figures"


def export_plot(fig, dpi=300):
    """Save a figure with the next available sequential filename."""
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    index = 1
    while (REPORT_DIR / f"figure_{index}.png").exists():
        index += 1
    file_path = REPORT_DIR / f"figure_{index}.png"
    fig.savefig(file_path, dpi=dpi, bbox_inches="tight")
    print(f"Figure saved successfully: {file_path}")


def load_and_prepare(path, value_column):
    data = pd.read_excel(path)
    subset = data.iloc[:, :3].copy()
    subset["improvement"] = data[value_column]
    subset.columns = ["index", "Country", "Year", "improvement"]
    return subset


def main():
    data_2020 = load_and_prepare(
        DATA_DIR / "raw" / "fsi-2020.xlsx", "Change from Previous Year"
    )
    data_2021 = load_and_prepare(
        DATA_DIR / "raw" / "fsi-2021.xlsx", "X1: External Intervention"
    )

    processed_dir = DATA_DIR / "processed"
    processed_dir.mkdir(parents=True, exist_ok=True)
    data_2020.to_pickle(processed_dir / "processed_data_2020.pkl")
    data_2021.to_pickle(processed_dir / "processed_data_2021.pkl")

    # Stack yearly datasets as rows instead of aligning unrelated columns side-by-side.
    merged = pd.concat([data_2020, data_2021], ignore_index=True)

    fig, ax = plt.subplots(figsize=(15, 4.5))
    merged["improvement"].plot(ax=ax, linewidth=2, label="Improvement")
    ax.set_title("Improvement Chart")
    ax.set_xlabel("Index")
    ax.set_ylabel("Improvement")
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.legend(loc="upper left", bbox_to_anchor=(1.02, 1))
    plt.tight_layout()
    export_plot(fig)
    plt.show()


if __name__ == "__main__":
    main()
