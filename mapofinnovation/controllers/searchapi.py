import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from mapofinnovation.lib.base import BaseController, render

log = logging.getLogger(__name__)

class SearchapiController(BaseController):

    def findSpaceByName(self):
	#check if a space with the given name exists
        return {'Success':'true'}

    def findSpacesAround(self):
	#display all the spaces that exist around this location
	return { "name":"Spaceslist", description"This is the list of spaces around this location","type":"array","space":{ "name_of_space": "", "latitude": ,"longitude": , "wiki_link":""} }

    def spaces_search(self):
	#display the spaces matching a given keyword
	return { "name":"Spaceslist", description"This is the list of spaces around this location","type":"array","space":{ "name_of_space": "", "latitude": ,"longitude": , "wiki_link":""} } 
