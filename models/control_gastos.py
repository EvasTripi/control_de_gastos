# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import ValidationError, UserError, RedirectWarning
import re
import json
import base64
import time

class control_gastos(models.Model):
    _name = "control.gastos"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Control de gastos"

    date_move = fields.Date("Fecha del movimiento")
    type_move = fields.Selection([
        ("Ingreso", "Ingreso"),
        ("Egreso", "Egreso"),
    ])
    amount_move = fields.Float("Cantidad del movimiento")

