"""CognosX brand helpers for Python figures (matplotlib and Plotly).

    import cognosx_brand as cx
    cx.use()                      # matplotlib style + sequential colormap
    fig, ax = plt.subplots(); ...; cx.credit(fig); cx.save(fig, "figure1")
    cx.plotly_template()          # registers and activates the "cognosx" Plotly template

Rules: categorical colours in fixed order (CATEGORICAL), amber first;
pure amber #FEA500 only on dark backgrounds; one y-axis per chart;
no logo on figures meant for journals (use credit=False).
"""
from __future__ import annotations

from pathlib import Path

HERE = Path(__file__).resolve().parent

BLACK, INK, MUTED, LINE = "#0a0a0a", "#141414", "#5c5c5c", "#e6e3dd"
PAPER, SOFT, AMBER, AMBER_INK = "#ffffff", "#f7f5f0", "#FEA500", "#9a5b00"

CATEGORICAL = ["#C98000", "#2F64B5", "#C24A2E", "#0E9A7E", "#8A4FB0"]          # on white
CATEGORICAL_DARK = ["#CC8200", "#5A88D0", "#D9664C", "#1FAA8A", "#9D78CE"]     # on black
NEUTRAL = "#9a9890"            # "other", totals, context series
SEQUENTIAL = ["#fbe9c7", "#f6cf85", "#eeb043", "#d98e0b", "#b87500", "#8f5a00", "#5f3c00"]  # heatmaps


def use(dark: bool = False) -> None:
    """Apply the CognosX matplotlib style (and the dark variant if asked)."""
    import matplotlib.pyplot as plt
    from matplotlib import colormaps
    from matplotlib.colors import LinearSegmentedColormap
    plt.style.use(HERE / "cognosx.mplstyle")
    if "cognosx_amber" not in colormaps:
        colormaps.register(LinearSegmentedColormap.from_list("cognosx_amber", SEQUENTIAL))
    plt.rcParams["image.cmap"] = "cognosx_amber"
    if dark:
        from cycler import cycler
        plt.rcParams.update({
            "figure.facecolor": BLACK, "axes.facecolor": BLACK, "savefig.facecolor": BLACK,
            "text.color": "#e9e9e9", "axes.titlecolor": "#ffffff", "axes.labelcolor": "#bdbdbd",
            "axes.edgecolor": "#bdbdbd", "xtick.color": "#bdbdbd", "ytick.color": "#bdbdbd",
            "grid.color": "#2a2a2a", "patch.edgecolor": BLACK,
            "axes.prop_cycle": cycler(color=CATEGORICAL_DARK),
        })


def credit(fig, text: str = "Source: CognosX analysis · cognosx.ca", dark: bool = False) -> None:
    """Small mono credit line at the bottom left (reports, Substack, social; not journals)."""
    fig.text(0.01, -0.02, text.upper(), fontsize=7, family="monospace",
             color=AMBER if dark else AMBER_INK, ha="left", va="top")


def save(fig, name: str, folder: str | Path = ".", formats=("png", "pdf", "svg")) -> None:
    folder = Path(folder)
    folder.mkdir(parents=True, exist_ok=True)
    for ext in formats:
        fig.savefig(folder / f"{name}.{ext}")


def plotly_template(activate: bool = True, dark: bool = False):
    """Register a 'cognosx' (or 'cognosx_dark') Plotly template."""
    import plotly.graph_objects as go
    import plotly.io as pio
    bg, fg, grid = (BLACK, "#e9e9e9", "#2a2a2a") if dark else (PAPER, INK, LINE)
    t = go.layout.Template()
    t.layout = go.Layout(
        font=dict(family="Inter, Helvetica Neue, Arial, sans-serif", size=13, color=fg),
        title=dict(font=dict(size=17, color=fg), x=0.0, xanchor="left"),
        paper_bgcolor=bg, plot_bgcolor=bg,
        colorway=CATEGORICAL_DARK if dark else CATEGORICAL,
        xaxis=dict(gridcolor=grid, linecolor=MUTED if not dark else "#bdbdbd", zeroline=False, ticks="outside"),
        yaxis=dict(gridcolor=grid, linecolor=MUTED if not dark else "#bdbdbd", zeroline=False),
        legend=dict(bgcolor="rgba(0,0,0,0)", orientation="h", y=1.08, x=0),
        colorscale=dict(sequential=[[i / (len(SEQUENTIAL) - 1), c] for i, c in enumerate(SEQUENTIAL)]),
        hoverlabel=dict(font=dict(family="Inter, Arial, sans-serif")),
        margin=dict(l=60, r=24, t=70, b=50),
    )
    name = "cognosx_dark" if dark else "cognosx"
    pio.templates[name] = t
    if activate:
        pio.templates.default = name
    return t
