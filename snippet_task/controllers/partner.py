from odoo.http import request
from odoo import http
import base64
    

class Partners(http.Controller):

    @http.route('/create_partner',type='http', auth="public", website=True) 
    def createpartner(self,**kw):
        print("Submit Button clicked---------------------------------",kw)
        file = kw.get('image_1920')
        filename=base64.b64encode(file.read())
        print('-------------',filename)
        vals={
        'name':kw.get('name'),
        'phone':kw.get('phone'),
        'email':kw.get('email'),
        'image_1920':filename
        }
        partner=request.env['res.partner'].create(vals)

        Attachment = request.env['ir.attachment']
        file_name = kw.get('image_1920').filename
        # file = post.get('attachment')
        attachment_id = Attachment.create({
        'name': file_name,
        'type': 'binary',
        'datas': filename,
        'res_model': partner._name,
        'res_id': partner.id
        })


        return request.render('website.contactus_thanks',{}) 

            