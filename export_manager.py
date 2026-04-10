from qgis.PyQt.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QPushButton,
    QLabel, QComboBox, QFileDialog, QMessageBox
)
from qgis.core import QgsProject, QgsVectorFileWriter

class ExportDialog(QDialog):
    def __init__(self, iface):
        super().__init__(iface.mainWindow())
        self.iface = iface
        self.setWindowTitle('Export MilitarySym-V Layer')
        self.setMinimumWidth(350)
        layout = QVBoxLayout()

        layout.addWidget(QLabel('Export format:'))
        self.format_combo = QComboBox()
        self.format_combo.addItems(['KML (Google Earth)', 'GeoJSON', 'Shapefile'])
        layout.addWidget(self.format_combo)

        btn_row = QHBoxLayout()
        export_btn = QPushButton('Export')
        export_btn.clicked.connect(self._export)
        cancel_btn = QPushButton('Cancel')
        cancel_btn.clicked.connect(self.reject)
        btn_row.addWidget(export_btn)
        btn_row.addWidget(cancel_btn)
        layout.addLayout(btn_row)

        pdf_btn = QPushButton('🖨 Open Print Layout for PDF')
        pdf_btn.clicked.connect(self._pdf)
        layout.addWidget(pdf_btn)
        self.setLayout(layout)

    def _export(self):
        layer = None
        for l in QgsProject.instance().mapLayers().values():
            if l.name() == 'MilitarySym-V Symbols':
                layer = l
                break
        if not layer:
            QMessageBox.warning(self, 'Error', 'No MilitarySym-V Symbols layer found.')
            return
        fmt = self.format_combo.currentText()
        driver, ext = ('KML','kml') if 'KML' in fmt else ('GeoJSON','geojson') if 'GeoJSON' in fmt else ('ESRI Shapefile','shp')
        path, _ = QFileDialog.getSaveFileName(self, 'Save', f'militarysym_symbols.{ext}', f'*.{ext}')
        if not path:
            return
        options = QgsVectorFileWriter.SaveVectorOptions()
        options.driverName = driver
        options.fileEncoding = 'UTF-8'
        err = QgsVectorFileWriter.writeAsVectorFormatV3(layer, path, QgsProject.instance().transformContext(), options)
        if err[0] == QgsVectorFileWriter.NoError:
            QMessageBox.information(self, 'Done', f'Exported to:\n{path}')
        else:
            QMessageBox.critical(self, 'Error', f'Export failed: {err[1]}')

    def _pdf(self):
        self.iface.actionShowLayoutManager().trigger()
        self.accept()