from email.policy import default
from odoo import models, fields, api
class Tenant(models.Model):
    _name = "tenant"
    _description = "Test Model for tenants"
    tenant_name = fields.Char(string="Tenant Name")
    tenant_info = fields.Char(string="Contact Info")
    property_tenant_id = fields.One2many('tenantship', 'tenant_id', string="Properties")