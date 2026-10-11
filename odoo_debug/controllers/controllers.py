from odoo import http
from odoo.http import request

class Debug(http.Controller):

    @http.route('/debug/debug', type='http', auth='none', csrf=False, methods=['GET'])
    def index(self, **kw):
       # params_data = request.env['issabel_api_log.issabel_api_log'].sudo().get_http_params()
     #  if not kw.get('src'):
        #    return "error"
     #   url="http://192.168.1.73/pbxapi/controllers/search_call.php?src=211"
     return 'Hello Wprld'
   