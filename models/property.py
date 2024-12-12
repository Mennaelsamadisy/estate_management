from email.policy import default
from odoo import models, fields, api
class Property(models.Model):
    _name = "prop"
    _description = "Test Model for properties"
    name = fields.Char(string="Name")
    address = fields.Char(string="Address")
    type = fields.Char(string="Type")
    size = fields.Float(string='Size')
    size_unit = fields.Selection(
        [('sqm', 'Square Meters'), ('sqft', 'Square Feet')],
        string='Size Unit',
        default='sqm',
    )
    price =fields.Float(string="Price")
    description = fields.Char(string="Description")
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([('north', 'North'), ('south', 'South'),('east','East'),('west','West')])
    owner_rel_ids = fields.One2many('ownership', 'property_id', string="Ownership Details")
    tenant_rel_id = fields.One2many('tenantship', 'property_tid', string="tenants details")

