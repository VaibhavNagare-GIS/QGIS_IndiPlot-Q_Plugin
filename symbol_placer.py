from qgis.gui import QgsMapTool
from qgis.core import QgsPointXY
from qgis.PyQt.QtCore import pyqtSignal, Qt

class SymbolPlacer(QgsMapTool):
    point_captured = pyqtSignal(QgsPointXY)

    def __init__(self, canvas):
        super().__init__(canvas)
        self.canvas = canvas

    def canvasReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            point = self.toMapCoordinates(event.pos())
            self.point_captured.emit(point)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.canvas.unsetMapTool(self)