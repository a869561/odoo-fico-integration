import requests
from odoo.addons.component.core import Component

class ContasimpleAdapter(Component):
    _name = 'contasimple.adapter'
    _inherit = 'base.backend.adapter'
    _usage = 'backend.adapter'
    _backend_type = 'contasimple.backend'

    def create(self, backend_record, data):
        url = f"{backend_record.api_url}/contacts"
        headers = {
            'Authorization': f'Bearer {backend_record.api_key}',
            'Content-Type': 'application/json'
        }

        response = requests.post(url, json=data, headers=headers)

        if response.status_code not in [200, 201]:
            raise Exception(f"Error al crear contacto: {response.text}")
        return response.json()
