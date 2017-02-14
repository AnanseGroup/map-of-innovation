import logging
import redis
import json
import re
import os

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators import jsonify
from mapofinnovation.lib.base import BaseController, render

log = logging.getLogger(__name__)

class SearchapiController(BaseController):

    def findSpaceByName(self):
	#check if a space with the given name exists
        return {'Success':'true'}
    
    @jsonify
    def findSpacesByType(self):
	s_type = request.params.get("type")
	s_value = request.params.get("name")
	spaceslist = []
        if os.environ.get("REDIS_URL") :
                redis_url = os.environ.get("REDIS_URL")
        else:
                redis_url = "localhost"
        r = redis.Redis(redis_url)
        for key in r.scan_iter():
                if (r.hget(key,s_type)== str(s_value)):
                	row = r.hgetall(key)
                	space={}
                	for i in row:
                        #do not show private fields 
                        	if i in ("image_url", "g_place_id"):
                                	pass
                        	else:
                                	space[i]=unicode(row[i], errors='replace')
                	spaceslist.append(space)
        return spaceslist	

    def findSpacesAround(self):
	#display all the spaces that exist around this location
	return {"name":"Spaceslist","description":"This is the list of spaces around this location","type":"array","space":{"name_of_space": "","latitude":"","longitude":"", "wiki_link":""}}

    def spaces_search(self):
	#display the spaces matching a given keyword
	return {"name":"Spaceslist","description":"This is the list of spaces around this location","type":"array","space":{"name_of_space": "","latitude":"","longitude":"","wiki_link":""}} 
