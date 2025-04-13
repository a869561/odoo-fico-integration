from odoo.addons.component.core import Component

class PartnerExportMapper(Component):
    _name = 'contasimple.partner.export.mapper'
    _inherit = 'base.export.mapper'
    _usage = 'export.mapper'
    _apply_on = 'res.partner'
    _backend_type = 'contasimple.backend'

    def _map_direct(self):
        return [
            ('name', 'name'),
            ('email', 'email'),
            ('phone', 'telephone'),
        ]

    def map_record(self, record):
        data = {}
        for source, target in self._map_direct():
            data[target] = record[source]
        return data
