# CognosX brand kit

*Let science data speak.* One source for the CognosX look on the website, reports, slides, figures, newsletters and social posts.

## 1. Colours

| Name | Hex | Use |
|---|---|---|
| Black | `#0a0a0a` | Dark backgrounds: navbar, footer, hero, social cards, video thumbnails |
| Ink | `#141414` | Body text on white |
| Muted | `#5c5c5c` | Secondary text, captions, axis labels |
| Line | `#e6e3dd` | Borders, rules, chart grids |
| Paper | `#ffffff` | Main light background |
| Soft paper | `#f7f5f0` | Alternate light bands, tables, callouts |
| **Amber** | `#FEA500` | The "X." of the logo; buttons, highlights and accents **on dark backgrounds only** |
| Amber ink | `#9a5b00` | Links and accent text **on white** (pure amber is too pale to read on white) |

Rule of thumb: black and white carry the page; amber is the one accent. Use it once per view.

## 2. Chart colours

The website has no chart colours, so these were built around the amber and checked for colour-blind readers (all checks pass). Use them **in this order**, never reordered, never cycled.

| Slot | On white | On black |
|---|---|---|
| 1 (amber) | `#C98000` | `#CC8200` |
| 2 (blue) | `#2F64B5` | `#5A88D0` |
| 3 (brick) | `#C24A2E` | `#D9664C` |
| 4 (teal) | `#0E9A7E` | `#1FAA8A` |
| 5 (violet) | `#8A4FB0` | `#9D78CE` |
| Other / totals | `#9a9890` | `#8a8a8a` |

Sequential (heatmaps, maps), light to dark: `#fbe9c7 #f6cf85 #eeb043 #d98e0b #b87500 #8f5a00 #5f3c00`.

More than 5 categories: fold the rest into "Other", or use small multiples.

## 3. Type

- **Inter** for everything: headings 700, body 400, buttons 600.
- **IBM Plex Mono** for small uppercase labels with wide letter spacing ("SCIENCE INTELLIGENCE FOR HEALTH", eyebrows, figure credits).
- Free from [Google Fonts](https://fonts.google.com/specimen/Inter). On a computer without them: Helvetica Neue or Arial.

## 4. Logo and motifs

- `logos/logo-light.png`: white "CognosX" with an amber "X.", for dark backgrounds (the default).
- `logos/logo-dark.png`: for light backgrounds. `logos/favicon.png`: the "X." mark for small sizes.
- Leave clear space around the logo at least the height of the "X". Never recolour, stretch or add effects.
- Signature motifs: the amber full stop ("speak**.**"), the amber halftone dot field (`logos/halftone.svg`), corners rounded at 10 px, pill-shaped buttons.

## 5. Voice

Short, plain sentences. Evidence first, with the number. Open and checkable ("shared step by step so others can check and repeat it"). Calm, not salesy. English and French.

## 6. Where to use what

| Production | How |
|---|---|
| Website, reports, slides, dashboards (Quarto) | Copy `quarto/_brand.yml` and the `logos/` folder to the project root. |
| Python figures (matplotlib) | `import cognosx_brand as cx; cx.use()` (or `cx.use(dark=True)`), then `cx.credit(fig)` and `cx.save(fig, "name")` |
| Plotly / dashboards | `cx.plotly_template()` makes "cognosx" the default template |
| Decks, docs and designs made with Claude | The "CognosX" design system |
| Canva (thumbnails, LinkedIn, posters) | A Canva Brand Kit with these colours, fonts and logos |
| Substack, LinkedIn, YouTube | Accent `#9a5b00` (or `#FEA500` on dark), black header with the light logo, one thumbnail template |

**Science rule:** in journal manuscripts and preprint figures, use the palette and fonts but **no logo and no credit line** (`cx.credit` is optional). Journals expect neutral figures; keep the logo for reports, slides, newsletters and social cards.

## 7. Files

```
logos/            logo-light.png, logo-dark.png, logo-tagline-light.png, favicon.png, halftone.svg, social-card.png
palette.json      every colour and font, for any tool
quarto/_brand.yml Quarto brand file
python/           cognosx.mplstyle, cognosx_brand.py (matplotlib + Plotly)
examples/         example_light.png, example_dark.png, example_plotly.html, example_figures.py
```

Source of the colours and fonts: `styles/brand.scss` in github.com/cognosx/cognosx.ca (October 2026).
