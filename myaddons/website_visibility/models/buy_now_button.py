from odoo import http
from odoo.addons.website.controllers.main import Website
class Website(Website):
	@http.route(auth='user')
   def index(self, **kw):
       super(Website, self).index()
       return http.request.render('<template_external_id>', {data})