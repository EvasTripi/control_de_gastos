# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import ValidationError, UserError, RedirectWarning
import re
import json
import base64
import time

class control_gastos_concepto(models.Model):
    _name = "control.gastos.concepto"
    _description = "Descripción del concepto del control de gastos"

    name = fields.Char("Nombre del concepto")

class control_gastos_cuenta(models.Model):
    _name = "control.gastos.cuenta"
    _description = "Descripción de la cuenta del control de gastos"

    name = fields.Char("Nombre de la cuenta")

class control_gastos(models.Model):
    _name = "control.gastos"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Control de gastos"
    _order = "id desc"

    name = fields.Many2one("control.gastos.concepto", string="Concepto")
    account = fields.Many2one("control.gastos.cuenta", string="Cuenta")
    date_move = fields.Date("Fecha del movimiento")
    type_move = fields.Selection([
        ("Ingreso", "Ingreso"),
        ("Egreso", "Egreso"),
    ])
    amount_move = fields.Float("Cantidad del movimiento")
    state_move = fields.Selection([
        ("Borrador", "Borrador"),
        ("Aprobado", "Aprobado")
    ])

    def aprobar_move(self):
        self.write({"state_move": "Aprobado"})
