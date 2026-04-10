# MilitarySym-V

A QGIS plugin for placing, labelling, and exporting NATO APP-6D military symbols on any QGIS map.

Built for defence GIS use cases including training simulations and operational planning. No open-source equivalent currently exists for QGIS.

---

## Features

- Dockable panel with a searchable symbol library
- 14 NATO APP-6D symbols across four categories: Friendly, Hostile, Neutral, Special
- Click-to-place symbols directly on the map canvas
- Per-symbol labelling with unit name, size, and status
- Rule-based SVG renderer (each symbol type gets its own SVG)
- Export to KML, GeoJSON, and Shapefile
- One-click access to QGIS Print Layout for PDF export
- Works with any basemap including Google Satellite (EPSG:3857 canvas supported)

---

## Requirements

- QGIS 3.34 or higher (tested on 3.40.12)
- Python 3.12 (bundled with QGIS)
- Windows, Linux, or macOS

---

## Installation

### Manual (recommended for now)

1. Download or clone this repository.
2. Copy the `MilitarySym_V` folder into your QGIS plugins directory:

**Windows:**
```
C:\Users\<your-username>\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\
```

**Linux:**
```
~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/
```

3. The folder on disk must be named `MilitarySym_V` (underscore, not hyphen). Python cannot import from hyphenated folder names.

4. Open QGIS. Go to Plugins > Manage and Install Plugins > Installed. Enable `MilitarySym-V`.

5. The plugin icon and menu entry appear under Plugins > MilitarySym-V.

---

## Usage

1. Open the plugin dock from the toolbar or Plugins menu.
2. Filter symbols by category (Friendly, Hostile, Neutral, Special) or use the search box.
3. Select a symbol from the list.
4. Enter a unit name, pick a unit size and operational status.
5. Click "Place Symbol on Map", then click anywhere on the map canvas.
6. The symbol appears with a label. Repeat for additional symbols.
7. Use "Export Layer" to save your symbols as KML, GeoJSON, or Shapefile.

To place across different CRS basemaps (including EPSG:3857 satellite tiles), the plugin handles coordinate transformation automatically.

---

## Known Limitations

- Memory layer only. Symbols are lost when QGIS is closed unless exported first.
- Symbol library currently covers 14 types. Full APP-6D coverage is a future goal.
- PDF export opens the Print Layout manager. A direct one-click PDF export is planned.
- No undo for placed symbols (remove features manually via the attribute table).

---

## License

This project is licensed under the GNU General Public License v3.0.

See [LICENSE](LICENSE) for the full text, or visit https://www.gnu.org/licenses/gpl-3.0.html.

In short: you are free to use, modify, and distribute this plugin. Any modified version must also be released under GPL-3.0 and keep the source open.

---

## Author

**Vaibhav Shivaji Nagare**
M.Sc. Geoinformatics

[![Email](https://img.shields.io/badge/Email-vaibhavnagare20%40gmail.com-red?logo=gmail)](mailto:vaibhavnagare20@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-VaibhavNagare--GIS-black?logo=github)](https://github.com/VaibhavNagare-GIS)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-vaibhav--nagare--gis-blue?logo=linkedin)](https://www.linkedin.com/in/vaibhav-nagare-gis)

---

## Contributing

Bug reports and feature requests: https://github.com/VaibhavNagare-GIS/militarysym-v_plugin/issues

Pull requests are welcome. Please test changes in QGIS 3.34 or higher before submitting.
---

---

<p align="center">
  <i>MilitarySym-V - Bringing NATO military symbology to open-source GIS.</i>
</p>
