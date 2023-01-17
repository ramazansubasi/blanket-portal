from odoo import fields, models, api,_
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError
import requests
import json
cookie = "blanket"

class blanketProfile(models.Model):
    _name = "blanket.profile"

    name = fields.Char(string="Name")
    blanket_id = fields.Char(string="Device Id")
    blanket_status = fields.Selection([('active','Active'),('passive', 'Passive'),('home', 'At Home')],
                                   string="Device Status",
                                   )
    live_status = fields.Selection([('wifionline','Wifi Online'),('gsmonline','Gsm Online'),('offline', 'Offline')],
    string="Live Status", default="offline"
    )
    city = fields.Char(string="City")
    #customer_id = fields.Many2one('res.partner', string="Customer")
    customer_id = fields.Many2many('res.partner',relation='x_blanket_profile_res_partner_rel', column1='blanket_profile_id',column2='res_partner_id', string="Customer")
    last_action_user = fields.Many2one('res.partner', string="Last Action User")
    blanket_update = fields.Boolean(string="Device Update")
    blanket_version = fields.Char(string="Version")
    blanket_home_mode = fields.Boolean(string="Home Mode")
    blanket_image = fields.Binary(string="Image")

    @api.onchange('blanket_status')
    def _get_partner(self):
        partner = self.env['res.users'].browse(self.env.uid).partner_id
        for rec in self: 
            rec.last_action_user = partner.id

    def write_Device_Status_Active(self):
        if self.blanket_update == False:
            self.write({'blanket_status': 'active'})
            self.write({'blanket_update': True})
            partner = self.env['res.users'].browse(self.env.uid).partner_id
            for rec in self: 
                rec.last_action_user = partner.id
        else:
            raise ValidationError("Cihaz Son Yaptığınız Ayarları Henüz Almadı. 1 Dakika Sonra Tekrar Deneyiniz.")
        
    def write_Device_Status_Passive(self):
        if self.blanket_update == False:
            self.write({'blanket_status': 'passive'})
            self.write({'blanket_update': True})
            partner = self.env['res.users'].browse(self.env.uid).partner_id
            for rec in self: 
                rec.last_action_user = partner.id
        else:
            raise ValidationError("Cihaz Son Yaptığınız Ayarları Henüz Almadı. 1 Dakika Sonra Tekrar Deneyiniz.")

    def write_Device_Status_Home(self):
        if self.blanket_update == False:
            self.write({'blanket_status': 'home'})
            self.write({'blanket_update': True})
            partner = self.env['res.users'].browse(self.env.uid).partner_id
            for rec in self: 
                rec.last_action_user = partner.id
        else:
            raise ValidationError("Cihaz Son Yaptığınız Ayarları Henüz Almadı. 1 Dakika Sonra Tekrar Deneyiniz.")

    def create_emergency_report(self):
        partner = self.env['res.users'].browse(self.env.uid).partner_id
        user_name = "Belirlenemeyen"
        for rec in self: 
            user_name = partner.name
        self.env['reports.profile'].sudo().create({
            'name': user_name + " Adlı kullanıcı Acil Durum Çağrısında Bulundu.",
            'ademco_id': "B001-000"
            })
    def create_ambulance_report(self):
        partner = self.env['res.users'].browse(self.env.uid).partner_id
        user_name = "Belirlenemeyen"
        for rec in self: 
            user_name = partner.name
        self.env['reports.profile'].sudo().create({
            'name': user_name + " Adlı kullanıcı Ambulans Çağrısında Bulundu.",
            'ademco_id': "B002-000"
            })
    def create_fire_report(self):
        partner = self.env['res.users'].browse(self.env.uid).partner_id
        user_name = "Belirlenemeyen"
        for rec in self: 
            user_name = partner.name
        self.env['reports.profile'].sudo().create({
            'name': user_name + " Adlı kullanıcı Yangın Çağrısında Bulundu.",
            'ademco_id': "B003-000"
            })
        

                              
class ResPartnersInherit(models.Model):
    _inherit = 'res.partner'

#discount_percentage = fields.Float("Discount Percentage")

    #gender = fields.Selection([('male','Male'),('female', 'Female'),('other', 'Other'),],string="Gender")
    #type_of_person = fields.Selection([('adult','Adult'),('child', 'Child'),('baby', 'Baby'),('driver', 'Driver')],string="Person Type")
    
    # How to OverRide Create Method Of a Model
    # https://www.youtube.com/watch?v=AS08H3G9x1U&list=PLqRRLx0cl0hoJhjFWkFYowveq2Zn55dhM&index=26
    
    #@api.model
    #def create(self, vals_list):
    #    res = super(ResPartners, self).create(vals_list)
    #    print("yes working")
    #    # do the custom coding here
    #    return res
    