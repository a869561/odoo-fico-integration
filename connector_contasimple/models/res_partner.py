from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    backend_id = fields.Many2one(
        'contasimple.backend',
        string="Contasimple Backend",
        help="Selecciona el backend de Contasimple para sincronizar este cliente."
    )

    def export_to_contasimple(self):
        for partner in self:
            if partner.backend_id:
                exporter = self.env['contasimple.partner.synchronizer'].with_context(
                    connector_no_export=False
                )
                exporter.run(partner.id)
