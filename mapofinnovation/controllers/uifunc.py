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
          "services": "services",
	  "wiki":"wiki"
        }
        if os.environ.get("REDIS_URL") :
          redis_url = os.environ.get("REDIS_URL")
        else:
          redis_url = "localhost"
        r = redis.Redis(redis_url)
        i = 0 
        for key in r.scan_iter():
          marker = {}
          row = r.hgetall(key)
	  marker['id'] = unicode(key, errors='replace')
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
      r = redis.Redis(redis_url)
      if id is None :
        return 'Provide a valid space id'
      elif r.exists(id):
	data = r.hgetall(id)
	s_address = str(data['street_address']).decode("ISO-8859-1")
	s_primary_website = urllib.unquote(data['primary_website']).decode('utf8' )
	s_twitter = urllib.unquote(data['twitter']).decode('utf8' )
	s_facebook = urllib.unquote(data['facebook']).decode('utf8' )
	s_jabber = urllib.unquote(data['jabber']).decode('utf8' )
	s_fablabs_url = urllib.unquote(data['fablabs_url']).decode('utf8' )
	s_googleplus = urllib.unquote(data['googleplus']).decode('utf8' )
	s_services = ''.join(data['services']) 
	s_tools = ''.join(data['tools '])
	s_function = ''.join(data['function'])
	if data['image_url'] is '':
		s_image = '/assets/image_placeholder.jpg'
	else:
		s_image = urllib.unquote(data['image_url']).decode('utf8' )
	s_tags=s_services+''+str(data['network_affiliation'])
	extra_vars={'s_last_updated':str(data['last_updated']),'s_name':str(data['name']),'s_status':str(data['status']),'s_primarywebsite':s_primary_website,'s_primarytype':str(data['primary_type']),'s_image':s_image,'s_tags':s_tags,'s_secondarytype':' ','s_description':str(data['description']),'s_address':s_address,'s_services':s_services,'s_function':s_function,'s_numberofmembers':str(data['number_of_members']),'s_networkaffliation':str(data['network_affiliation']),'s_tools':s_tools,'s_twitter':s_twitter,'s_googleplus':s_googleplus,'s_fablabs_url':s_fablabs_url,'s_facebook':s_facebook,'s_jabber':s_jabber}
        return render('/wikipage.html',extra_vars)
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

    def comingSoon(self):
	return render('/coming-soon.html')
