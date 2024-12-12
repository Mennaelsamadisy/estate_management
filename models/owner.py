from email.policy import default
from odoo import models, fields, api
class Owner(models.Model):
    _name = "owner"
    _description = "Test Model for owners"
    owner_name = fields.Char(string="Owner Name")
    owner_phone = fields.Char(string='Phone Number')
    owner_email = fields.Char(string='Email Address')
    property_rel_ids = fields.One2many('ownership', 'owner_id', string="Properties")