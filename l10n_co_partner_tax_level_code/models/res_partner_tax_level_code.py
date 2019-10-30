# -*- coding: utf-8 -*-
# Copyright 2019 Juan Camilo Zuluaga Serna <Github@camilozuluaga>
# Copyright 2019 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models

class ResPartnerTaxLevelCode(models.Model):
	_name = 'res.partner.tax.level.code'

	name = fields.Char(string='Name')
	code = fields.Char(string='Code')