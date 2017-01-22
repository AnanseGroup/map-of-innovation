import logging
import json
import redis
import sys
import urllib
import os

from urlparse import urlparse
from pylons import request, response, session, tmpl_context as c, url
from pylons.decorators import jsonify
from pylons.controllers.util import abort, redirect
from mapofinnovation.lib.base import BaseController, render

log = logging.getLogger(__name__)
class UifuncController(BaseController):

    def index(self):
        # Return a rendered front page  template
        markers = []
        indices = {
          "name": "name",
          "city": "city",
          "country": "country",
          "website": "primary_website",
          "primarytype": "primary_type",
          "multitypes": "types_multiple",
          "description": "description",
          "latitude": "latitude",
          "longitude":"longitude",
          "services": "services"
        }
        if os.environ.get("REDIS_URL") :
          redis_url = os.environ.get("REDIS_URL")
        else:
          redis_url = "localhost"
        r = redis.from_url(redis_url)
        i = 0 
        for key in r.scan_iter():
          marker = {}
          row = r.hgetall(key)
          for header in indices.keys():
            marker[header] = unicode(row[str(indices[header])], errors='replace')
          markers.append(marker)
        c.markers = json.dumps(markers)		
        return render('/makermap.html')

    def wikipage(self,id=None):
      #Return a wiki for the given space 
      if os.environ.get("REDIS_URL") :
        redis_url = os.environ.get("REDIS_URL")
      else:
        redis_url = "localhost"
      r = redis.from_url(redis_url)
      if id is None :
        return 'Provide a valid space id'
      elif r.exists(id):
        data = r.hgetall(id)
        addresstext = str(data['street_address']).decode("ISO-8859-1")
        websitetext = urllib.unquote(data['primary_website']).decode('utf8')
        return render('/wikipage.html',extra_vars={'last_updated':str(data['last_updated']),'name':str(data['name']),'status':str(data['status']),'website_url':websitetext,'primarytype':str(data['primary_type']),'secondarytype':'','space_description':str(data['description']),'address':addresstext})
      else :
        return 'There is no space with this id. Please recheck and submit'

    def about(self):
        return render('/about.html')		
    
    def goals(self):
        return render('/goals.html')

    def userDocs(self):
    	return render('/user-documentation.html')

    def devDocs(self):
    	return render('/developer-documentation.html')