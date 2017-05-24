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

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from mapofinnovation.model.innovation_space import Innovation_Space
engine = create_engine("postgres://lyla@/atlas")


log = logging.getLogger(__name__)
class UifuncController(BaseController):

    def index(self):
        # Return a rendered front page  template
        return render('/makermap.html')

    def wikipage(self,id=None):
        #Return a wiki for the given space 
        session = Session(bind=engine)
        result = session.query(Innovation_Space).filter(Innovation_Space.primary_id==id).one()
        session.close()
        return render('/wikipage.html',result.__json__())
        # extra_vars={'s_id':id,'s_last_updated':s_last_updated,'s_source':str(data['source']),
        # 's_name':str(data['name']).decode('ISO-8859-1'),'s_status':s_status,'s_primarywebsite':s_primary_website,
        # 's_email':str(data['email']),'s_theme':str(data['theme']),'s_primarytype':str(data['primary_type']),
        # 's_image':s_image,'s_ownership':s_ownership,'s_secondarytype':' ','s_description':s_description,
        # 's_address':s_address,'s_country':s_country,'s_services':s_services,'s_function':s_function,
        # 's_numberofmembers':str(data['number_of_members']),'s_networkaffliation':str(data['network_affiliation']),
        # 's_tools':s_tools,'s_twitter':s_twitter,'s_googleplus':s_googleplus,'s_fablabs_url':s_fablabs_url,'s_facebook':s_facebook,'s_jabber':s_jabber}
      
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
    
    def gigmap(self):
        # Return a rendered front page  template
        return render('/makermap-gig.html')
