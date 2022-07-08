from odoo import models, fields, api
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta

class SaleMoveHeritfacture(models.Model):
    _inherit = 'sale.order'
    sale_date_Facture = fields.Date("Date de prochaine facturation")
    sale_park = fields.Boolean(default=False)
    sale_periode = fields.Integer(default='0')
    ########################## update date
    def curDate(self):
        sale_facture_date= self.env['sale.order'].search([('sale_park','=',True)])
        print(sale_facture_date)
        for sale_fact in sale_facture_date:

            if sale_fact.sale_periode ==1:
                if sale_fact.sale_date_Facture + relativedelta(months=1) <= date.today():
                    sale_fact.sale_date_Facture += relativedelta(months=1)
                    print(sale_fact)
                    print(sale_fact.sale_date_Facture)
                    sale_orders = self.env['sale.order'].search([('sale_maintnance', '=', True), ('invoice_status', '=', 'to invoice')])
                    print(sale_orders)
                    invoice_lines = []
                    for sale in sale_orders:
                        print(sale.sale_commande_fleet_ids[0].fleet_id.fleet_devis_id.id)
                        print(sale_fact.id)
                        if sale.sale_commande_fleet_ids[0].fleet_id.fleet_devis_id.id == sale_fact.id:
                            for line in sale.order_line:
                                if line.display_type:
                                    vals = {
                                        'name': line.name,
                                        'display_type': line.display_type,
                                    }
                                    invoice_lines.append((0, 0, vals))
                                else:
                                    vals = {
                                        'name': line.name,
                                        'price_unit': line.price_unit,
                                        'quantity': line.product_uom_qty,
                                        'product_id': line.product_id.id,
                                        'product_uom_id': line.product_uom.id,
                                        'sale_line_ids': [(6, 0, [line.id])],
                                    }
                                    invoice_lines.append((0, 0, vals))
                            self.env['account.move'].create({
                                'ref': sale.client_order_ref,
                                'move_type': 'out_invoice',
                                'invoice_origin': sale.name,
                                'invoice_user_id': sale.user_id.id,
                                'partner_id': sale.partner_invoice_id.id,
                                'invoice_line_ids': invoice_lines,
                                'acount_maintnance': True,
                            })
                            sale.invoice_status = 'invoiced'
            if sale_fact.sale_periode ==3:
                if sale_fact.sale_date_Facture + relativedelta(months=3) <= date.today():
                    sale_fact.sale_date_Facture += relativedelta(months=3)
                    sale_orders = self.env['sale.order'].search(
                        [('sale_maintnance', '=', True), ('invoice_status', '=', 'to invoice')])
                    print(sale_orders)
                    print(sale_fact)
                    print(sale_fact.sale_date_Facture)
                    invoice_lines = []
                    for sale in sale_orders:
                        print(sale.sale_commande_fleet_ids[0].fleet_id.fleet_devis_id.id)
                        print(sale_fact.id)
                        if sale.sale_commande_fleet_ids[0].fleet_id.fleet_devis_id.id == sale_fact.id:
                            for line in sale.order_line:
                                if line.display_type:
                                    vals = {
                                        'name': line.name,
                                        'display_type': line.display_type,
                                    }
                                    invoice_lines.append((0, 0, vals))
                                else:
                                    vals = {
                                        'name': line.name,
                                        'price_unit': line.price_unit,
                                        'quantity': line.product_uom_qty,
                                        'product_id': line.product_id.id,
                                        'product_uom_id': line.product_uom.id,
                                        'sale_line_ids': [(6, 0, [line.id])],
                                    }
                                    invoice_lines.append((0, 0, vals))
                            self.env['account.move'].create({
                                'ref': sale.client_order_ref,
                                'move_type': 'out_invoice',
                                'invoice_origin': sale.name,
                                'invoice_user_id': sale.user_id.id,
                                'partner_id': sale.partner_invoice_id.id,
                                'invoice_line_ids': invoice_lines,
                                'acount_maintnance': True,
                            })
                            sale.invoice_status = 'invoiced'


class AcountMoveHeritFIN(models.Model):
    _inherit = 'account.move'
    acount_maintnance = fields.Boolean(string="Maintenance", default=False)



