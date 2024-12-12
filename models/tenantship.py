from odoo import models, fields, api
class Tenantship(models.Model):
    _name = "tenantship"
    _description = "Test Model for realtionship between tenants and a property"
    property_tid = fields.Many2one('prop', string="Property", required=True, ondelete='cascade')
    tenant_id = fields.Many2one('tenant', string="tenant", required=True, ondelete='cascade')
    lease_startdate = fields.Date("Start date", default=fields.Datetime.now)
    lease_enddate = fields.Date("End date", default=fields.Datetime.now)
    monthly_rent = fields.Float("Monthly Rent" ,compute="_compute_monthly_rent",store="true")
    @api.depends('property_tid.price')
    def _compute_monthly_rent(self):
        for rec in self:
           if rec.property_tid:
             rec.monthly_rent=rec.property_tid.price/12
