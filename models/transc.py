from email.policy import default
from odoo import models, fields, api
class Transc(models.Model):
    _name = "transc"
    _description = "Test Model for properties"

    transc_date = fields.Date("Transaction Date", default=fields.Datetime.now)
    amount = fields.Float(string="Amount")
    property_id = fields.Many2one('prop', string="Property", required=True)
    parties_involved = fields.Text(string="Parties Involved", help="Details of buyers, sellers, or tenants.")