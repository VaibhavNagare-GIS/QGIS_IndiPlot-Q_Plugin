from qgis.core import (
    QgsRuleBasedRenderer, QgsSymbol, QgsSvgMarkerSymbolLayer,
    QgsWkbTypes, QgsPalLayerSettings, QgsVectorLayerSimpleLabeling,
    QgsTextFormat, QgsUnitTypes
)
from qgis.PyQt.QtGui import QFont, QColor
import os

class SymbolManager:
    def __init__(self, plugin_dir):
        self.plugin_dir = plugin_dir

    def apply_rule_renderer(self, layer):
        symbols = [
            ('f_inf', 'symbols/friendly/infantry.svg'),
            ('f_arm', 'symbols/friendly/armour.svg'),
            ('f_eng', 'symbols/friendly/engineer.svg'),
            ('f_art', 'symbols/friendly/artillery.svg'),
            ('f_log', 'symbols/friendly/logistics.svg'),
            ('f_hq',  'symbols/friendly/headquarter.svg'),
            ('h_inf', 'symbols/hostile/infantry.svg'),
            ('h_arm', 'symbols/hostile/armour.svg'),
            ('h_unk', 'symbols/hostile/unknown.svg'),
            ('n_unit','symbols/neutral/unit.svg'),
            ('s_mine','symbols/special/minefield.svg'),
            ('s_obs', 'symbols/special/obstacle.svg'),
            ('s_bri', 'symbols/special/bridge.svg'),
            ('s_chk', 'symbols/special/checkpoint.svg'),
        ]

        # Build a fresh rule-based renderer
        default_sym = QgsSymbol.defaultSymbol(QgsWkbTypes.PointGeometry)
        renderer = QgsRuleBasedRenderer(default_sym)
        root = renderer.rootRule()

        # Remove the default catch-all rule
        root.removeChildAt(0)

        for sym_id, svg_rel in symbols:
            svg_abs = os.path.join(self.plugin_dir, svg_rel)

            # Build SVG marker from scratch
            svg_layer = QgsSvgMarkerSymbolLayer(svg_abs)
            svg_layer.setSize(12)
            svg_layer.setSizeUnit(QgsUnitTypes.RenderMillimeters)

            # Create a point symbol and replace its layer
            point_symbol = QgsSymbol.defaultSymbol(QgsWkbTypes.PointGeometry)
            point_symbol.deleteSymbolLayer(0)
            point_symbol.appendSymbolLayer(svg_layer)

            # Create rule
            rule = QgsRuleBasedRenderer.Rule(point_symbol)
            rule.setFilterExpression(f'"symbol_id" = \'{sym_id}\'')
            rule.setActive(True)
            root.appendChild(rule)

        layer.setRenderer(renderer)
        self._apply_labels(layer)
        layer.triggerRepaint()

    def _apply_labels(self, layer):
        settings = QgsPalLayerSettings()
        settings.fieldName = 'unit_name'
        settings.enabled = True
        txt = QgsTextFormat()
        txt.setFont(QFont('Arial', 8, QFont.Bold))
        txt.setColor(QColor('#000000'))
        settings.setFormat(txt)
        layer.setLabeling(QgsVectorLayerSimpleLabeling(settings))
        layer.setLabelsEnabled(True)