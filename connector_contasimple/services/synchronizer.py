from odoo.addons.component.core import Component

class PartnerSynchronizer(Component):
    _name = 'contasimple.partner.synchronizer'
    _inherit = 'base.export.synchronizer'
    _apply_on = 'res.partner'
    _usage = 'record.exporter'
    _backend_type = 'contasimple.backend'

    def run(self, binding_id):
        partner = self.env['res.partner'].browse(binding_id)

        # Obtener el mapper y transformar los datos
        mapper = self.component(usage='export.mapper')
        mapped_data = mapper.map_record(partner)

        # Obtener el backend (contasimple) desde el partner
        backend = partner.backend_id

        # Obtener el adapter y hacer la llamada a la API
        adapter = self.component(usage='backend.adapter')
        result = adapter.create(backend, mapped_data)

        # Puedes guardar info de sincronización si hace falta
        self._after_export(partner, result)

    def _after_export(self, partner, result):
        partner.message_post(body=f"Cliente sincronizado con Contasimple. ID: {result.get('id')}")
