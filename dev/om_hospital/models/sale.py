from odoo import api, fields, models, _


class HospitalPatient(models.Model):
    _inherit = "sale.order"
    sale_description = fields.Char(string='Sale Description')
