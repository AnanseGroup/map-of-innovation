import logging
import redis
import json
import re
import os
import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators import jsonify
from mapofinnovation.lib.base import BaseController, render
from datetime import datetime

from mapofinnovation.model.innovation_space import Innovation_Space
log = logging.getLogger(__name__)

class BaseapiController(BaseController):

    # @jsonify    
    # def getAllSpaceLocations(self):

    #     session = Session(bind=engine)
    #     spaces = session.query(Innovation_Space)

    #     columns = [x.__str__().split('.')[1] for x in Innovation_Space.__table__.columns]
    #     spaceslist = []
    #     for space in spaces:
    #         spaceslist.append({ column: getattr(space, column) for column in columns })
    #     return spaceslist


    @jsonify
    def getAllSpaceLocations(self):

        session = Session(bind=engine)
        spaces = session.query(Innovation_Space)
        return translate_to_jsonable(spaces)

    @staticmethod
    def translate_to_jsonable(spaces):
        columns = [x.__str__().split('.')[1] for x in Innovation_Space.__table__.columns]
        spaceslist = []
        for space in spaces:
            spaceslist.append({ column: getattr(space, column) for column in columns })
        return spaceslist

 #    @jsonify
 #    def addSpace(self):
    # #add a space
    # if os.environ.get("REDIS_URL") :
    #   redis_url = os.environ.get("REDIS_URL")
    # else:
    #   redis_url = "localhost"
    # r = redis.Redis(redis_url)
    # surl = request.params.get("primary_website")
    # exists = False
    # if surl is None :
    #   pass
    # else :
    #   exists = self._search_space(surl)
    # if exists is False:
    #   tparams=request.params
    #   dparams = {}
    #   for k,v in tparams.items():
    #       dparams.update({k:v})
    #   dparams.update({'archived':False})
    #   dparams.update({'verified':False})
    #   skey = request.params.get("name")+str(datetime.now())
    #   r.hmset(re.sub(' ','',skey),dparams)
    # return {'sucess':'true'}
        
 #    def _search_space(self,surl):
    # if os.environ.get("REDIS_URL") :
 #          redis_url = os.environ.get("REDIS_URL")
 #        else:
 #          redis_url = "localhost"
 #        r = redis.Redis(redis_url)
    # for key in r.scan_iter():
    #   if (r.hget(key,"primary_website")== str(surl)):
    #       return True
    # return False

    @jsonify
    def getSpace(self):
        #get a space details
        skey = request.params.get("id")
        if os.environ.get("REDIS_URL") :
                    redis_url = os.environ.get("REDIS_URL")
        else:
                redis_url = "localhost"
        r = redis.Redis(redis_url)
        space_details = r.hgetall(skey)
        del space_details["g_place_id"]
        return space_details


    def changeSpace(self,id=None):
        #change a space
        #TO DO: implement change space for verified space
        if os.environ.get("REDIS_URL") :
            redis_url = os.environ.get("REDIS_URL")
        else:
            redis_url = "localhost"
        r = redis.Redis(redis_url)
        params=request.params
        temp_params = {}
        for k,v in params.items():
            if(temp_params.has_key(k)) :
                temp_params[k]=temp_params[k]+","+v
            else :
                temp_params.update({k:v})
            r.hmset(id,temp_params)
        return render('/thanks.html',{'s_id':id})
        
 #    @jsonify
 #    def archiveSpace(self):
    # #archive a space
    # skey = request.params.get("id")
    # if os.environ.get("REDIS_URL") :
    #   redis_url = os.environ.get("REDIS_URL")
    # else:
    #   redis_url = "localhost"
    # r = redis.Redis(redis_url)
    # r.hset(skey,'archived',True) 
    # return {'sucess':'true'}
