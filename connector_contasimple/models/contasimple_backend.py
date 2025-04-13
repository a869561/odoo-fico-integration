from odoo import models, fields

class ContasimpleBackend(models.Model):
    _name = 'contasimple.backend'
    _description = 'Backend de conexión a Contasimple'

    name = fields.Char(string="Nombre", required=True)
    api_url = fields.Char(string="URL de la API", default="https://api.contasimple.com")
    api_key = fields.Char(string="API Key", required=True)
    active = fields.Boolean(default=True)
