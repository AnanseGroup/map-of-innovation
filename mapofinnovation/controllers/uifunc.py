import logging
import json
import redis
import sys
import urllib
import json
import urllib2
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
	if data['street_address'] is '':
		s_address = "No address available"
	else:
		s_address = str(data['street_address']).decode("ISO-8859-1")
	s_primary_website = urllib.unquote(data['primary_website']).decode('utf8' )
	if data['twitter'] is '':
		s_twitter = ''
	else:
		s_twitter = urllib.unquote(data['twitter']).decode('utf8' )
	if data['facebook'] is '':
                s_facebook = ''
        else:
		s_facebook = urllib.unquote(data['facebook']).decode('utf8' )
	if data['jabber'] is '':
                s_jabber = ''
        else:
		s_jabber = urllib.unquote(data['jabber']).decode('utf8' )
	if data['fablabs_url'] is '':
                s_fablabs_url = ''
        else:
		s_fablabs_url = urllib.unquote(data['fablabs_url']).decode('utf8' )
	if data['googleplus'] is '':
                s_googleplus = ''
        else:
		s_googleplus = urllib.unquote(data['googleplus']).decode('utf8' )
	s_country = str(data['country'])
	s_services = ''.join((data['services'])) 
	s_tools = ''.join((data['tools']))
	s_function = ''.join(data['function'])
	if data['image_url'] is '':
		s_image = ''
	else:
		s_image = urllib.unquote(data['image_url']).decode('utf8')

	s_description = str(data['description']).decode('ISO-8859-1')
	if data['last_updated'] is '':
		s_last_updated = ''
	else: 
		s_last_updated = 'Last Updated : '+str(data['last_updated'])
	
	s_ownership=str(data['ownership'])		

	if data['status'] is '':
		s_status = ''
	else:
		s_status = "Status:"+str(data['status'])
	extra_vars={'s_id':id,'s_last_updated':s_last_updated,'s_source':str(data['source']),'s_name':str(data['name']).decode('ISO-8859-1'),'s_status':s_status,'s_primarywebsite':s_primary_website,'s_theme':str(data['theme']),'s_primarytype':str(data['primary_type']),'s_image':s_image,'s_ownership':s_ownership,'s_secondarytype':' ','s_description':s_description,'s_address':s_address,'s_country':s_country,'s_services':s_services,'s_function':s_function,'s_numberofmembers':str(data['number_of_members']),'s_networkaffliation':str(data['network_affiliation']),'s_tools':s_tools,'s_twitter':s_twitter,'s_googleplus':s_googleplus,'s_fablabs_url':s_fablabs_url,'s_facebook':s_facebook,'s_jabber':s_jabber}
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

    def joinus(self):
	return render('/join-us.html')	

    def wiki(self):
	with open('mapofinnovation/public/countries.json') as json_file:    
		data = json.load(json_file)
		c_list=[]
		for p in data['country']:
			c_list.append(str((p['countryName']).encode('ascii','replace')))
		c.list = c_list
        return render('/wiki.html')
	
    def wikilist(self,id=None):
	c.filtertype = id
	c.filterparam = (request.params.get("name"))
	return render('/wikilist.html')	

    def contactus(self):
	return render('/contact.html')

    def editspace(self,id=None):
	return render('/formedit.html')
