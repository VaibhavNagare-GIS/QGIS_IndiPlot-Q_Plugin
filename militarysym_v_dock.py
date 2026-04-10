from qgis.PyQt.QtWidgets import (
    QDockWidget, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QComboBox, QListWidget,
    QListWidgetItem, QPushButton
)
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtCore import Qt, pyqtSignal, QSize
import json
import os

class MilitarySymVDock(QDockWidget):
    place_symbol_requested = pyqtSignal(dict, str, str, str)

    def __init__(self, iface):
        super().__init__('MilitarySym-V - NATO Symbology')
        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__)
        self.symbols = []
        self.setAllowedAreas(Qt.RightDockWidgetArea | Qt.LeftDockWidgetArea)
        self.setMinimumWidth(260)
        self._load_symbols()
        self._build_ui()

    def _load_symbols(self):
        json_path = os.path.join(self.plugin_dir, 'data', 'symbol_library.json')
        with open(json_path, 'r') as f:
            self.symbols = json.load(f)['symbols']

    def _build_ui(self):
        container = QWidget()
        layout = QVBoxLayout()
        layout.setSpacing(6)

        title = QLabel('🪖 MilitarySym-V - NATO Symbols')
        title.setStyleSheet('font-weight: bold; font-size: 13px; padding: 4px;')
        layout.addWidget(title)

        self.category_combo = QComboBox()
        self.category_combo.addItems(['All', 'Friendly', 'Hostile', 'Neutral', 'Special'])
        self.category_combo.currentTextChanged.connect(self._filter_symbols)
        layout.addWidget(self.category_combo)

        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText('🔍 Search symbols...')
        self.search_box.textChanged.connect(self._filter_symbols)
        layout.addWidget(self.search_box)

        self.symbol_list = QListWidget()
        self.symbol_list.setIconSize(QSize(40, 30))
        self.symbol_list.setMinimumHeight(200)
        self._populate_list(self.symbols)
        layout.addWidget(self.symbol_list)

        layout.addWidget(QLabel('Unit Name:'))
        self.unit_name_input = QLineEdit()
        self.unit_name_input.setPlaceholderText('e.g. 21 ENGR REGT')
        layout.addWidget(self.unit_name_input)

        layout.addWidget(QLabel('Unit Size:'))
        self.size_combo = QComboBox()
        self.size_combo.addItems(['Team', 'Squad', 'Platoon', 'Company', 'Battalion', 'Brigade', 'Division'])
        layout.addWidget(self.size_combo)

        layout.addWidget(QLabel('Status:'))
        self.status_combo = QComboBox()
        self.status_combo.addItems(['Present', 'Planned', 'Suspected', 'Destroyed'])
        layout.addWidget(self.status_combo)

        self.place_btn = QPushButton('📍 Place Symbol on Map')
        self.place_btn.setStyleSheet('background-color: #003580; color: white; font-weight: bold; padding: 8px;')
        self.place_btn.clicked.connect(self._on_place_clicked)
        layout.addWidget(self.place_btn)

        export_btn = QPushButton('💾 Export Layer')
        export_btn.setStyleSheet('background-color: #555; color: white; padding: 6px;')
        export_btn.clicked.connect(self._on_export)
        layout.addWidget(export_btn)

        self.status_label = QLabel('Select a symbol and click the map.')
        self.status_label.setStyleSheet('color: gray; font-size: 11px;')
        self.status_label.setWordWrap(True)
        layout.addWidget(self.status_label)

        layout.addStretch()
        container.setLayout(layout)
        self.setWidget(container)

    def _populate_list(self, symbols):
        self.symbol_list.clear()
        for sym in symbols:
            item = QListWidgetItem(sym['name'])
            svg_path = os.path.join(self.plugin_dir, sym['svg'])
            if os.path.exists(svg_path):
                item.setIcon(QIcon(svg_path))
            item.setData(Qt.UserRole, sym)
            self.symbol_list.addItem(item)

    def _filter_symbols(self):
        cat = self.category_combo.currentText()
        search = self.search_box.text().lower()
        filtered = [
            s for s in self.symbols
            if (cat == 'All' or s['category'] == cat)
            and (search == '' or search in s['name'].lower())
        ]
        self._populate_list(filtered)

    def _on_place_clicked(self):
        selected = self.symbol_list.currentItem()
        if not selected:
            self.status_label.setText('⚠️ Please select a symbol first.')
            return
        sym = selected.data(Qt.UserRole)
        unit_name = self.unit_name_input.text() or sym['name']
        size = self.size_combo.currentText()
        status = self.status_combo.currentText()
        self.place_symbol_requested.emit(sym, unit_name, size, status)
        self.status_label.setText(f'📍 Click on the map to place: {unit_name}')

    def _on_export(self):
        from .export_manager import ExportDialog
        dlg = ExportDialog(self.iface)
        dlg.exec_()