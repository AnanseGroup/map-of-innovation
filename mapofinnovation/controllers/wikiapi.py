import logging
import redis 
import os 

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from mapofinnovation.lib.base import BaseController, render

log = logging.getLogger(__name__)

class WikiapiController(BaseController):

    def getWikiLink(self):
	#return a wikilink given an id
        return {'id':'','internal_wiki_link':''}

   def addWikiLink(self):
	#add a wiki page for a space
	return {'Success':'True'}
