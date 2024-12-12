from odoo import models, fields, api
class Ownership(models.Model):
    _name = "ownership"
    _description = "Test Model for ownership"
    property_id = fields.Many2one('prop', string="Property", required=True, ondelete='cascade')
    owner_id = fields.Many2one('owner', string="Owner", required=True, ondelete='cascade')
    ownership_percentage = fields.Float(string="Ownership Percentage", compute="_compute_ownership_percentage", store=True)

    @api.depends('property_id.owner_rel_ids')
    def _compute_ownership_percentage(self):
        """Compute ownership percentage for each owner of a property."""
        for rel in self:
            if rel.property_id:
                total_owners = len(rel.property_id.owner_rel_ids)
                rel.ownership_percentage = 100.0 / total_owners if total_owners > 0 else 0.0