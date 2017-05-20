import logging
import redis
import json
import re
import os

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators import jsonify
from mapofinnovation.lib.base import BaseController, render

from baseapi import BaseapiController
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from mapofinnovation.model.innovation_space import Innovation_Space

log = logging.getLogger(__name__)

engine = create_engine("postgres://lyla@/atlas")

class SearchapiController(BaseController):

    def findSpaceByName(self):
	#check if a space with the given name exists
        return {'Success':'true'}
    
    @jsonify
    def findSpacesByType(self):


        s_type = request.params.get("type")
        s_value = request.params.get("name")

        session = Session(bind=engine)
        field = 'primary_id'
        result = session.query(Innovation_Space).filter(getattr(Innovation_Space, s_type) == s_value)
        session.close()
        return BaseapiController.translate_to_jsonable(result)

    def findSpacesAround(self):
	#display all the spaces that exist around this location
	return {"name":"Spaceslist","description":"This is the list of spaces around this location","type":"array","space":{"name_of_space": "","latitude":"","longitude":"", "wiki_link":""}}

    def spaces_search(self):
	#display the spaces matching a given keyword
	return {"name":"Spaceslist","description":"This is the list of spaces around this location","type":"array","space":{"name_of_space": "","latitude":"","longitude":"","wiki_link":""}} 
