from qgis.PyQt.QtWidgets import QAction, QMessageBox
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtCore import Qt
from qgis.core import (
    QgsProject, QgsVectorLayer, QgsField, QgsFeature,
    QgsGeometry, QgsPointXY, QgsWkbTypes
)
from qgis.PyQt.QtCore import QVariant
import os

class MilitarySymV:
    def __init__(self, iface):
        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__)
        self.dock_widget = None
        self.map_tool = None
        self.active_sym = None
        self.active_unit = None
        self.active_size = None
        self.active_status = None

    def initGui(self):
        icon = QIcon(os.path.join(self.plugin_dir, 'icons', 'plugin_icon.png'))
        self.action = QAction(icon, 'MilitarySym-V', self.iface.mainWindow())
        self.action.triggered.connect(self.toggle_dock)
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu('MilitarySym-V', self.action)

    def toggle_dock(self):
        from .militarysym_v_dock import MilitarySymVDock
        if self.dock_widget is None:
            self.dock_widget = MilitarySymVDock(self.iface)
            self.dock_widget.place_symbol_requested.connect(self._start_placement)
            self.iface.addDockWidget(Qt.RightDockWidgetArea, self.dock_widget)
        self.dock_widget.setVisible(not self.dock_widget.isVisible())

    def _start_placement(self, sym, unit_name, size, status):
        from .symbol_placer import SymbolPlacer
        self.active_sym = sym
        self.active_unit = unit_name
        self.active_size = size
        self.active_status = status
        self.map_tool = SymbolPlacer(self.iface.mapCanvas())
        self.map_tool.point_captured.connect(self._place_symbol)
        self.iface.mapCanvas().setMapTool(self.map_tool)

    def _place_symbol(self, point):
        from qgis.core import QgsCoordinateTransform, QgsCoordinateReferenceSystem, QgsProject

        canvas_crs = self.iface.mapCanvas().mapSettings().destinationCrs()
        wgs84 = QgsCoordinateReferenceSystem('EPSG:4326')
        transform = QgsCoordinateTransform(canvas_crs, wgs84, QgsProject.instance())
        point_4326 = transform.transform(point)

        layer = self._get_or_create_layer()
        layer.startEditing()
        feat = QgsFeature(layer.fields())
        feat.setGeometry(QgsGeometry.fromPointXY(point_4326))
        feat.setAttribute('symbol_id',   self.active_sym['id'])
        feat.setAttribute('symbol_name', self.active_sym['name'])
        feat.setAttribute('unit_name',   self.active_unit)
        feat.setAttribute('size',        self.active_size)
        feat.setAttribute('status',      self.active_status)
        feat.setAttribute('svg_path',    self.active_sym['svg'])
        layer.addFeature(feat)
        layer.commitChanges()
        
        if self.dock_widget:
            self.dock_widget.status_label.setText(f'✅ Placed: {self.active_unit}')

    def _get_or_create_layer(self):
        for layer in QgsProject.instance().mapLayers().values():
            if layer.name() == 'MilitarySym-V Symbols':
                return layer
        layer = QgsVectorLayer('Point?crs=EPSG:4326', 'MilitarySym-V Symbols', 'memory')
        pr = layer.dataProvider()
        pr.addAttributes([
            QgsField('symbol_id',   QVariant.Type.String),
            QgsField('symbol_name', QVariant.Type.String),
            QgsField('unit_name',   QVariant.Type.String),
            QgsField('size',        QVariant.Type.String),
            QgsField('status',      QVariant.Type.String),
            QgsField('svg_path',    QVariant.Type.String),
        ])
        layer.updateFields()
        QgsProject.instance().addMapLayer(layer)
        from .symbol_manager import SymbolManager
        SymbolManager(self.plugin_dir).apply_rule_renderer(layer)
        return layer

    def unload(self):
        self.iface.removeToolBarIcon(self.action)
        self.iface.removePluginMenu('MilitarySym-V', self.action)
        if self.dock_widget:
            self.iface.removeDockWidget(self.dock_widget)