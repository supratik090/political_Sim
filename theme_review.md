# 🎨 Political Symbol and Party Theme Configuration Review

Below is the complete summary of all **17 unique symbols** and the matching logic for the **20+ political parties** implemented in the simulation's React UI.

---

## 📋 Symbol Mapping & Emojis

All major party symbols are cropped and extracted directly from the user's uploaded chart, cleaned with transparency keying, and hosted locally in the `/symbols/` public directory. All other minor/generic parties default to a beautifully crafted Ashoka Chakra.

| Symbol Name | Represented Symbol | Local Path / CDN Source | Matching Parties / Names | Description |
| :--- | :--- | :--- | :--- | :--- |
| **`Ashoka Chakra`**| ☸️ Ashoka Chakra | *Procedural SVG* | **Default Fallback** | Symmetrical 24-spoke wheel from the Indian Flag in Navy Blue (`#000080`). |
| **`Lotus`** | 🪷 Lotus | `/symbols/bjp.png` | **BJP**, **NDA**, **NDA (BJP+JD-U)** | Authentic orange/pink multi-layered lotus flower blooming. |
| **`Hand`** | 🖐️ Hand | `/symbols/inc.png` | **INC**, **Congress**, **INC-UDF** | Open palm facing forward, fingers straight, thumb out. |
| **`Hammer`** | ☭ Hammer & Sickle | `/symbols/cpim.png` | **LDF (CPI-M)**, **Left Front** | Crossed hammer and sickle icon representing workers and peasants. |
| **`Closed Fist`** | ✊ Closed Fist | `https://cdn-icons-png.flaticon.com/512/2614/2614742.png` | **Youth Development Party (YDP)** | Styled fist icon representing youth empowerment. |
| **`Tiger`** | 🐯 Tiger Head | `https://cdn-icons-png.flaticon.com/512/3069/3069172.png` | **Tiger Front** | Flat vector tiger head with orange ears and stripes. |
| **`Elephant`** | 🐘 Elephant | `/symbols/bsp.png` | **BSP**, **Elephant Congress** | Full-body side profile of a walking blue elephant. |
| **`Peacock`** | 🦚 Peacock | `https://cdn-icons-png.flaticon.com/512/2620/2620581.png` | **Peacock Party** | Peacock silhouette showcasing its colorful feathers. |
| **`Bicycle (TDP)`**| 🚲 Bicycle | `/symbols/tdp.png` | **TDP** | Row 1, Col 3 (White background) |
| **`Bicycle (SP)`** | 🚲 Bicycle | `/symbols/sp.png` | **Samajwadi Party (SP)** | Row 2, Col 0 (Red/green background) |
| **`Arrow`** | 🏹 Arrow | `/symbols/jdu.png` | **JD-U** | Row 4, Col 3 (Green/white background) |
| **`Lantern`** | 🪔 Lantern | `/symbols/rjd.png` | **RJD** | Row 0, Col 3 (White background) |
| **`Twin Flowers`** | 💐 Twin Flowers | `/symbols/tmc.png` | **TMC** | Row 2, Col 3 (White background) |
| **`Bow & Arrow`** | 🏹 Bow & Arrow | `/symbols/shivsena.png` | **Shiv Sena** | Row 2, Col 1 (White background) |
| **`Ceiling Fan`** | 🌀 Ceiling Fan | `https://cdn-icons-png.flaticon.com/512/924/924619.png` | **INC (YSR)** | Symmetrical 3-blade ceiling fan seen from below. |
| **`Two Leaves`** | 🍃 Two Leaves | `/symbols/aiadmk.png` | **AIADMK** | Green leaves side-by-side representing growth. |
| **`Rising Sun`** | 🌅 Rising Sun | `/symbols/dmk.png` | **DMK** | Sun rising from the horizon radiating bright red/yellow rays. |
| **`Star`** | ⭐ Star | `https://cdn-icons-png.flaticon.com/512/1828/1828884.png` | *Reward Banners* | Shiny golden star. |
| **`Flag`** | 🚩 Flag | `https://cdn-icons-png.flaticon.com/512/206/206124.png` | *System Icon* | Red waving flag icon. |

---

## 🔍 Matched Theme Lookups (`getPartyThemeByName`)

When a party name matches any of the keywords below, the UI overrides its database-seeded properties with this sleek palette:

1.  **BJP / NDA**
    *   **Color**: `#FF9933` (Saffron Orange)
    *   **Symbol**: `Lotus`
2.  **INC / Congress / UDF**
    *   **Color**: `#128807` (National Green)
    *   **Symbol**: `Hand`
3.  **INC (YSR)**
    *   **Color**: `#1E3A8A` (Deep Navy Blue)
    *   **Symbol**: `Ceiling Fan`
4.  **TMC (Trinamool Congress)**
    *   **Color**: `#0095B6` (Trinamool Blue)
    *   **Symbol**: `Twin Flowers`
5.  **Shiv Sena**
    *   **Color**: `#FF9933` (Shiv Sena Saffron)
    *   **Symbol**: `Bow & Arrow`
6.  **LDF (CPI-M) / Left Front**
    *   **Color**: `#D23F31` (Communist Red)
    *   **Symbol**: `Hammer & Sickle`
7.  **RJD**
    *   **Color**: `#1E824C` (Lantern Green)
    *   **Symbol**: `Lantern`
8.  **JD-U**
    *   **Color**: `#196F3D` (Arrow Green)
    *   **Symbol**: `Arrow`
9.  **TDP**
    *   **Color**: `#FDD835` (Telugu Yellow)
    *   **Symbol**: `Bicycle`
10. **Samajwadi Party (SP)**
    *   **Color**: `#1E824C` (Samajwadi Green)
    *   **Symbol**: `Bicycle`
11. **BSP / Elephant Congress**
    *   **Color**: `#1A5276` (Elephant Blue)
    *   **Symbol**: `Elephant`
12. **Youth Development Party (YDP)**
    *   **Color**: `#0ABAB5` (Tiffany/Teal)
    *   **Symbol**: `Closed Fist`
13. **Tiger Front**
    *   **Color**: `#E15554` (Tiger Coral)
    *   **Symbol**: `Tiger`
14. **Peacock Party**
    *   **Color**: `#17B890` (Peacock Green)
    *   **Symbol**: `Peacock`
15. **AIADMK**
    *   **Color**: `#008000` (Leaves Green)
    *   **Symbol**: `Two Leaves`
16. **DMK**
    *   **Color**: `#B22222` (DMK Red)
    *   **Symbol**: `Rising Sun`
