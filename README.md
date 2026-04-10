# MilitarySym-V - NATO Military Symbology Plugin for QGIS

<p align="center">
  <img src="icons/plugin_icon.png" alt="MilitarySym-V Icon" width="64"/>
</p>

<p align="center">
  <b>Place, label, and export NATO APP-6D military symbols directly on any QGIS map.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/QGIS-3.34%2B-green?logo=qgis" alt="QGIS Version"/>
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python" alt="Python Version"/>
  <img src="https://img.shields.io/badge/Standard-NATO%20APP--6D-darkred" alt="NATO APP-6D"/>
  <img src="https://img.shields.io/badge/License-GPL--3.0-orange" alt="License"/>
  <img src="https://img.shields.io/badge/Status-Active-brightgreen" alt="Status"/>
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey" alt="Platform"/>
</p>

---

## Overview

**MilitarySym-V** is the **first and only open-source QGIS plugin** that brings NATO APP-6D compliant military symbology into the GIS environment. No comparable open-source tool exists for QGIS that allows direct interactive placement, labelling, and export of standardised military symbols on a geospatial map canvas.

Defence GIS practitioners, researchers, military geographers, and simulation professionals have long had to manually create or import military symbols outside of their GIS workflow. MilitarySym-V fills this gap by providing a fully integrated, dockable interface within QGIS itself by allowing users to select, place, label, and export NATO symbols without leaving the application.

### What makes this different

- **No open-source equivalent exists** - this is the only plugin of its kind in the QGIS ecosystem
- Works with **any basemap** - OpenStreetMap, Google Satellite, Esri, or your own raster layers
- Symbols are stored as a **GeoJSON/memory vector layer** - fully queryable, editable, and exportable
- Built entirely on **PyQGIS and PyQt5** - no external dependencies required beyond QGIS itself
- Follows the **NATO APP-6D standard** for symbol shapes, colours, and affiliations

---

## Features

- 🪖 **14 NATO APP-6D symbols** across four categories: Friendly, Hostile, Neutral, Special
- 🗺️ **Interactive click-to-place** - select a symbol and click anywhere on the map canvas
- 🔍 **Symbol search and category filter** in the dock panel
- 🏷️ **Automatic unit labelling** - every placed symbol is labelled with the unit name
- 📐 **Unit size selector** - Team, Squad, Platoon, Company, Battalion, Brigade, Division
- 🔴 **Status selector** - Present, Planned, Suspected, Destroyed
- 📤 **Multi-format export** - KML (Google Earth), GeoJSON, Shapefile
- 🖨️ **Print Layout integration** - open QGIS Print Layout Manager directly from the plugin
- ⚡ **Rule-based SVG rendering** - each symbol type renders its own SVG marker automatically
- 💾 **Memory + GeoJSON layer** - all placements stored in the `MilitarySym-V Symbols` layer
- 🔄 **Live reload compatible** - works with Plugin Reloader for rapid development

---

## Symbol Library

| Category | Symbols |
|---|---|
| **Friendly** | Infantry, Armour, Engineer, Artillery, Logistics, Headquarters |
| **Hostile** | Infantry, Armour, Unknown |
| **Neutral** | Unit |
| **Special** | Minefield, Obstacle, Bridge, Checkpoint |

Symbols follow NATO APP-6D colour coding:
- **Friendly** - Blue (`#80BFFF`) rectangle frame
- **Hostile** - Red (`#FF8080`) diamond frame
- **Neutral** - Green (`#80FF80`) square frame
- **Special** - Context-specific colours with dashed or solid borders

---

## Requirements

| Component | Minimum Version |
|---|---|
| QGIS | 3.34 (Prizren) or later |
| Python | 3.10 or later |
| Operating System | Windows 10/11, Ubuntu 20.04+, macOS 12+ |
| Internet | Not required (fully offline capable) |

No additional Python packages required. All dependencies are bundled with QGIS.

---

## Installation

### Method 1 - Manual Installation (Recommended)

1. Download or clone this repository:
   ```bash
   git clone https://github.com/VaibhavNagare-GIS/militarysym-v_plugin.git
   ```

2. Rename the cloned folder to `MilitarySym_V` (underscore, not hyphen — Python import requirement)

3. Copy the folder to your QGIS plugins directory:

   **Windows:**
   ```
   C:\Users\<YourUsername>\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\
   ```

   **Linux:**
   ```
   ~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/
   ```

   **macOS:**
   ```
   ~/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/
   ```

4. Open QGIS → **Plugins** → **Manage and Install Plugins** → **Installed** tab → enable **MilitarySym-V**

5. The MilitarySym-V toolbar icon will appear. Click it to open the dock panel.

### Method 2 - Plugin Reloader (For Developers)

1. Install the **Plugin Reloader** plugin from the QGIS Plugin Manager
2. Set Plugin Reloader target to `MilitarySym_V`
3. Press the Reload button after any code changes - no QGIS restart needed

---

## Usage

### Placing a Symbol

1. Click the **MilitarySym-V** toolbar icon to open the dock panel
2. Use the **category dropdown** (All / Friendly / Hostile / Neutral / Special) to filter symbols
3. Use the **search box** to find a symbol by name
4. Click the symbol you want in the list
5. Enter a **Unit Name** (e.g., `21 ENGR REGT`)
6. Select **Unit Size** and **Status**
7. Click **📍 Place Symbol on Map**
8. Click anywhere on the map canvas - the symbol is placed and labelled instantly

### Exporting

1. After placing symbols, click **💾 Export Layer**
2. Choose your export format:
   - **KML** - for Google Earth and other KML viewers
   - **GeoJSON** - for web maps, QGIS, and GIS applications
   - **Shapefile** - for ArcGIS and traditional GIS workflows
3. Choose a save location and click **Export**
4. For PDF export, click **🖨 Open Print Layout** to use QGIS's built-in print composer

### Managing the Symbol Layer

All placed symbols are stored in the **`MilitarySym-V Symbols`** memory layer. You can:
- Open the **Attribute Table** to view and edit all placed symbols
- Use QGIS **Selection Tools** to select individual symbols
- Use **Layer Properties** to customise rendering further
- **Save** the layer to a permanent file via Layer → Save As

---

## File Structure

```
MilitarySym_V/
├── __init__.py                  ← Plugin entry point
├── metadata.txt                 ← QGIS plugin metadata
├── militarysym_v.py             ← Main plugin class
├── militarysym_v_dock.py        ← Dock widget UI and logic
├── symbol_placer.py             ← Map click tool (QgsMapTool)
├── symbol_manager.py            ← SVG rule-based renderer + labels
├── export_manager.py            ← Export dialog (KML/GeoJSON/SHP/PDF)
├── icons/
│   └── plugin_icon.png          ← 32×32 toolbar icon
├── data/
│   └── symbol_library.json      ← Symbol catalogue (14 symbols)
├── symbols/
│   ├── friendly/                ← 6 friendly unit SVGs
│   ├── hostile/                 ← 3 hostile unit SVGs
│   ├── neutral/                 ← 1 neutral unit SVG
│   └── special/                 ← 4 special feature SVGs
├── styles/                      ← Reserved for future QML styles
└── help/
    └── README.md
```

---

## Architecture

```
User clicks "Place Symbol"
        │
        ▼
SymbolPlacer (QgsMapTool)
  captures canvas click
        │
        ▼
MilitarySymV._place_symbol()
  transforms coordinates (canvas CRS → EPSG:4326)
  adds feature to memory layer
        │
        ▼
SymbolManager.apply_rule_renderer()
  builds QgsRuleBasedRenderer
  matches symbol_id → SVG file
  applies unit_name labels
        │
        ▼
Layer renders SVG markers on map canvas
```

**CRS handling:** The plugin transforms all click coordinates from the map canvas CRS to EPSG:4326 (WGS84) before storing them. This ensures data integrity regardless of what basemap or projection the user is working in.

---

## Data Model

The `MilitarySym-V Symbols` layer stores the following attributes for each placed symbol:

| Field | Type | Description |
|---|---|---|
| `symbol_id` | String | Internal symbol identifier (e.g., `f_inf`, `h_arm`) |
| `symbol_name` | String | Display name (e.g., `Friendly Infantry`) |
| `unit_name` | String | User-entered unit name (e.g., `21 ENGR REGT`) |
| `size` | String | Unit size (Team → Division) |
| `status` | String | Operational status (Present / Planned / Suspected / Destroyed) |
| `svg_path` | String | Relative path to the SVG file used for rendering |

---

## NATO APP-6D Compliance

This plugin implements a working subset of the NATO APP-6D symbology standard. Symbol shapes follow the standard's affiliation-based frame geometry:

- **Rectangle frame** → Friendly units
- **Diamond (rotated square) frame** → Hostile units  
- **Square frame** → Neutral units
- **Dashed/custom frames** → Special features (Minefields, Obstacles, etc.)

Internal symbol modifiers (crosses, ellipses, triangles) identify the functional unit type (Infantry, Armour, Engineer, etc.) following APP-6D conventions.

> **Note:** This is a working implementation of the standard for educational, research, and planning purposes. It is not a fully certified APP-6D implementation. Full APP-6D certification requires additional symbol modifiers and echelon indicators not yet implemented in v1.0.0.

---

## Roadmap

- [ ] Echelon indicators (size markers above the frame)
- [ ] Additional symbol modifiers (task force, headquarters staff)
- [ ] Full APP-6D symbol set (100+ symbols)
- [ ] Symbol rotation support
- [ ] Custom symbol colour overrides
- [ ] Symbol attribute editing from the dock panel
- [ ] MGRS coordinate display on placement
- [ ] Tactical graphics (lines and areas, not just points)
- [ ] Symbol set import/export (JSON profiles)
- [ ] QGIS Plugin Repository release

---

## Known Limitations

- The `MilitarySym-V Symbols` layer is a **memory layer** - it is lost when QGIS closes unless you save it to a file via Layer → Save As before closing
- Tactical graphics (lines, boundaries, phase lines) are **not yet implemented** - v1.0.0 supports point symbols only
- The plugin requires the **map canvas CRS** to be set before placing symbols by using a basemap (Google, OSM, Esri) sets this automatically

---

## Contributing

Contributions are welcome. To contribute:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Make your changes and test in QGIS 3.34+
4. Commit with a clear message: `git commit -m "Add echelon indicators for battalion level"`
5. Push and open a Pull Request

Please follow the existing code style (PyQGIS conventions, 4-space indentation, descriptive variable names).

### Reporting Issues

Use the [GitHub Issues](https://github.com/VaibhavNagare-GIS/militarysym-v_plugin/issues) page to report bugs or request features. Include:
- QGIS version and OS
- Steps to reproduce the issue
- Screenshot of the error (Python Console output if available)

---

## Development Setup

```bash
# Clone the repo
git clone https://github.com/VaibhavNagare-GIS/militarysym-v_plugin.git

# Rename for Python compatibility
mv militarysym-v_plugin MilitarySym_V

# Copy to QGIS plugins directory (Windows example)
cp -r MilitarySym_V "C:/Users/<user>/AppData/Roaming/QGIS/QGIS3/profiles/default/python/plugins/"

# Install Plugin Reloader from QGIS Plugin Manager for live reloading
```

**Recommended IDE:** VS Code with the [QGIS Plugin Tools](https://marketplace.visualstudio.com/items?itemName=elpeonCom.qgis-plugin-tools) extension.

---

## License

This project is licensed under the **GNU General Public License v3.0**.

See [LICENSE](LICENSE) for the full license text.

This plugin is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

---

## Author

**Vaibhav Shivaji Nagare**  
M.Sc. Geoinformatics  
vaibhavnagare20@gmail.com  
[github.com/VaibhavNagare-GIS](https://github.com/VaibhavNagare-GIS)

---

## Acknowledgements

- [QGIS Development Team](https://qgis.org) - for the PyQGIS framework
- [NATO Standardization Office](https://www.nato.int/cps/en/natohq/topics_89644.htm) - for the APP-6D standard documentation
- The open-source GIS community - for making defence GIS tooling accessible

---

## Citation

If you use MilitarySym-V in research, training, or publications, please cite it as:

```
Nagare, V. S. (2026). MilitarySym-V: NATO Military Symbology Plugin for QGIS (v1.0.0).
GitHub. https://github.com/VaibhavNagare-GIS/militarysym-v_plugin
```

---

<p align="center">
  <i>MilitarySym-V - Bringing NATO military symbology to open-source GIS.</i>
</p>
