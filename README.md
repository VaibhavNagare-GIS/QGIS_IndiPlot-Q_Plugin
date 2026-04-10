# MilitarySym-V - NATO Military Symbology Plugin for QGIS

<p align="center">
  <img src="https://raw.githubusercontent.com/VaibhavNagare-GIS/militarysym-v_plugin/main/icons/plugin_icon.png" alt="MilitarySym-V Icon" width="120"/>
</p>

<p align="center">
  <b>Place, label, and export NATO APP-6D military symbols directly on any QGIS map.</b>
</p>

<p align="center">
  <a href="https://qgis.org"><img src="https://img.shields.io/badge/QGIS-3.34%2B-green?logo=qgis" alt="QGIS Version"/></a>
  <a href="https://www.python.org"><img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python" alt="Python Version"/></a>
  <a href="[https://www.nato.int/cps/en/natohq/topics_89644.htm](https://www.nato.int/en/about-us/organization/nato-structure/nato-standardization-office)"><img src="https://img.shields.io/badge/Standard-NATO%20APP--6D-darkred" alt="NATO APP-6D"/></a>
  <a href="https://www.gnu.org/licenses/gpl-3.0.html"><img src="https://img.shields.io/badge/License-GPL--3.0-orange" alt="License"/></a>
  <a href="https://github.com/VaibhavNagare-GIS/militarysym-v_plugin"><img src="https://img.shields.io/badge/Status-Active-brightgreen" alt="Status"/></a>
  <a href="https://github.com/VaibhavNagare-GIS/militarysym-v_plugin/releases"><img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey" alt="Platform"/></a>
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

- 14 NATO APP-6D symbols across four categories: Friendly, Hostile, Neutral, Special
- Interactive click-to-place on any map canvas
- Symbol search and category filter in the dock panel
- Automatic unit labelling with name, size, and status
- Unit size selector: Team to Division
- Status selector: Present, Planned, Suspected, Destroyed
- Export to KML, GeoJSON, and Shapefile
- Print Layout integration for PDF export
- Rule-based SVG rendering per symbol type
- Works with any basemap and CRS (coordinate transform handled automatically)

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

---

## Usage

1. Click the MilitarySym-V toolbar icon to open the dock.
2. Filter or search for a symbol, then select it from the list.
3. Enter unit name, size, and status.
4. Click **Place Symbol on Map**, then click anywhere on the canvas.
5. To export, click **Export Layer** and choose KML, GeoJSON, or Shapefile.
6. For PDF, click **Open Print Layout** to use the QGIS print composer.

All placed symbols are stored in the **MilitarySym-V Symbols** memory layer. Save it via Layer > Save As before closing QGIS or your data will be lost.

---

**CRS handling:** The plugin transforms all click coordinates from the map canvas CRS to EPSG:4326 (WGS84) before storing them. This ensures data integrity regardless of what basemap or projection the user is working in.

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

## Known Limitations

- The `MilitarySym-V Symbols` layer is a **memory layer** - it is lost when QGIS closes unless you save it to a file via Layer → Save As before closing
- Tactical graphics (lines, boundaries, phase lines) are **not yet implemented** - v1.0.0 supports point symbols only
- The plugin requires the **map canvas CRS** to be set before placing symbols by using a basemap (Google, OSM, Esri) sets this automatically

---

## Contributing

Contributions are welcome. To contribute:

Bug reports and feature requests: [GitHub Issues](https://github.com/VaibhavNagare-GIS/militarysym-v_plugin/issues)

To contribute: fork the repo, create a feature branch, test in QGIS 3.34+, and open a Pull Request.

Include QGIS version, OS, and Python Console output when reporting bugs.

---

## License

Licensed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html).

This plugin is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

---

## Author

**Vaibhav Shivaji Nagare**
M.Sc. Geoinformatics

[![Email](https://img.shields.io/badge/Email-vaibhavnagare20%40gmail.com-red?logo=gmail)](mailto:vaibhavnagare20@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-VaibhavNagare--GIS-black?logo=github)](https://github.com/VaibhavNagare-GIS)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-vaibhav--nagare--gis-blue?logo=linkedin)](https://www.linkedin.com/in/vaibhav-nagare-gis)

---

## Acknowledgements

- [QGIS Development Team](https://qgis.org) - for the PyQGIS framework
- [NATO Standardization Office](https://www.nato.int/en/about-us/organization/nato-structure/nato-standardization-office) - for the APP-6D standard documentation
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
