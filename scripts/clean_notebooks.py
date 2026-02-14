#!/usr/bin/env python3
"""Notebook cleanup script for Monte Carlo Backtesting project.

This script processes all .ipynb files to:
1. Remove empty trailing cells
2. Clear large outputs (plotly JSON, embedded images)
3. Add missing markdown section headers to distribution notebooks
4. Clean up redundant print-only cells (e.g. cells that just say 'df')
"""

import json
import os
import glob

BASE_DIR = "/Users/karos/Documents/Monte Carlo Backtesting for Profitable Trading"


def load_notebook(path):
    with open(path, "r") as f:
        return json.load(f)


def save_notebook(path, nb):
    with open(path, "w") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
        f.write("\n")


def remove_trailing_empty_cells(cells):
    """Remove empty code cells from the end."""
    while cells and cells[-1].get("cell_type") == "code":
        src = "".join(cells[-1].get("source", []))
        if src.strip() == "":
            cells.pop()
        else:
            break
    return cells


def clear_outputs(cells):
    """Clear all cell outputs and reset execution counts."""
    for cell in cells:
        if cell.get("cell_type") == "code":
            cell["outputs"] = []
            cell["execution_count"] = None
    return cells


def make_markdown_cell(text):
    """Create a markdown cell with given text."""
    return {
        "cell_type": "markdown",
        "id": None,
        "metadata": {},
        "source": [text]
    }


def make_code_cell(source):
    """Create a code cell with given source."""
    return {
        "cell_type": "code",
        "execution_count": None,
        "id": None,
        "metadata": {},
        "outputs": [],
        "source": source if isinstance(source, list) else [source]
    }


# ── Distribution notebooks: add section headers ──────────────────────────

DIST_HEADERS = {
    "01_log_normal_distribution.ipynb": [
        ("# Log-Normal Distribution\n\n"
         "The log-normal distribution models asset returns where the "
         "logarithm of the price follows a normal distribution."),
        "## 1 — Generating Log-Normal Returns & Plotting",
        "## 2 — Synthetic Price Series Using Log-Normal Returns",
    ],
    "02_cauchy_distribution.ipynb": [
        ("# Cauchy Distribution\n\n"
         "The Cauchy distribution has heavier tails than the normal, "
         "making it useful for modeling extreme price movements."),
        "## 1 — Generating Cauchy Samples & Plotting",
        "## 2 — Synthetic Price Series Using Cauchy Returns",
    ],
    "03_laplace_distribution.ipynb": [
        ("# Laplace Distribution\n\n"
         "The Laplace (double exponential) distribution has sharper peaks "
         "and heavier tails than the Gaussian, better capturing financial "
         "return distributions."),
        "## 1 — Generating Laplace Samples & Plotting",
        "## 2 — Laplace vs Normal: Side-by-Side Comparison",
        "## 3 — Synthetic Price Series Using Laplace Returns",
        "## 4 — Multiple Simulations Comparison",
    ],
    "04_student_t_distribution.ipynb": None,  # Already has headers
    "05_triangular_distribution.ipynb": [
        ("# Triangular Distribution\n\n"
         "The triangular distribution is defined by a minimum, maximum, and "
         "mode — useful for bounded return scenarios."),
        "## 1 — Generating Triangular Samples & Plotting",
        "## 2 — Synthetic Price Series Using Triangular Returns",
    ],
    "06_pareto_distribution.ipynb": [
        ("# Pareto Distribution\n\n"
         "The Pareto distribution follows the 80/20 power-law, modeling "
         "scenarios with rare but extreme events."),
        "## 1 — Comparing Pareto Shapes & Plotting",
        "## 2 — Synthetic Price Series Using Pareto Returns",
    ],
}


def add_headers_to_distribution_notebook(cells, headers):
    """Insert markdown headers before each code cell in a distribution notebook."""
    if headers is None:
        return cells

    new_cells = []
    code_idx = 0
    for cell in cells:
        if cell.get("cell_type") == "code":
            src = "".join(cell.get("source", []))
            if src.strip() == "":
                continue  # skip empty cells
            if code_idx < len(headers):
                new_cells.append(make_markdown_cell(headers[code_idx]))
            code_idx += 1
            new_cells.append(cell)
        else:
            new_cells.append(cell)
    return new_cells


def process_notebook(path, dist_headers=None):
    """Full cleanup pipeline for a single notebook."""
    nb = load_notebook(path)
    cells = nb.get("cells", [])

    # 1. Add headers for distribution notebooks without any markdown
    if dist_headers is not None:
        cells = add_headers_to_distribution_notebook(cells, dist_headers)

    # 2. Clear outputs
    cells = clear_outputs(cells)

    # 3. Remove trailing empty cells
    cells = remove_trailing_empty_cells(cells)

    nb["cells"] = cells
    save_notebook(path, nb)
    print(f"  ✅ Cleaned: {os.path.basename(path)} ({len(cells)} cells)")


def main():
    # Process distribution notebooks
    dist_dir = os.path.join(BASE_DIR, "02_distributions")
    print("\n── 02_distributions/ ──")
    for fname, headers in DIST_HEADERS.items():
        fpath = os.path.join(dist_dir, fname)
        if os.path.exists(fpath):
            process_notebook(fpath, dist_headers=headers)

    # Process randomness trading data notebooks
    rand_dir = os.path.join(BASE_DIR, "03_randomness_trading_data")
    print("\n── 03_randomness_trading_data/ ──")
    for nb_file in sorted(glob.glob(os.path.join(rand_dir, "*.ipynb"))):
        process_notebook(nb_file)

    # Process backtesting notebook
    bt_dir = os.path.join(BASE_DIR, "04_monte_carlo_backtesting")
    print("\n── 04_monte_carlo_backtesting/ ──")
    for nb_file in sorted(glob.glob(os.path.join(bt_dir, "*.ipynb"))):
        process_notebook(nb_file)

    # Process random generators notebook
    rg_dir = os.path.join(BASE_DIR, "01_random_generators")
    print("\n── 01_random_generators/ ──")
    for nb_file in sorted(glob.glob(os.path.join(rg_dir, "*.ipynb"))):
        process_notebook(nb_file)

    print("\n✅ All notebooks cleaned successfully!")


if __name__ == "__main__":
    main()
