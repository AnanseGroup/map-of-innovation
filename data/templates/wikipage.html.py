# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1481652657.456763
_enable_loop = True
_template_filename = '/home/ubuntu/isproject/map-of-innovation/mapofinnovation/templates/wikipage.html'
_template_uri = '/wikipage.html'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        status = context.get('status', UNDEFINED)
        primarytype = context.get('primarytype', UNDEFINED)
        last_updated = context.get('last_updated', UNDEFINED)
        name = context.get('name', UNDEFINED)
        secondarytype = context.get('secondarytype', UNDEFINED)
        address = context.get('address', UNDEFINED)
        space_description = context.get('space_description', UNDEFINED)
        website_url = context.get('website_url', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<html>\n<head>\n<link href="https://fonts.googleapis.com/css?family=Libre+Baskerville|Source+Sans+Pro:200,300,300i,400,600" rel="stylesheet">\n<link rel="stylesheet" type="text/css" href="/css/wikipage.css"/>\n<link rel="stylesheet" type="text/css" href="/css/stylesheet.css"/>\n<script type=\'text/javascript\' src=\'/js/wiki.js\'></script>\n<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>\n</head>\n<body>\n ')
        runtime._include_file(context, u'/snippets/header.html', _template_uri)
        __M_writer(u'\n \n<div class="wBlockHeader">\n<div class="w-top-navigation">\n<a href="/" >\n    \t<img src="/assets/edit_button.png" id="w-top-navigation-bar-edit-button">\n</a>Last updated :')
        __M_writer(escape(last_updated))
        __M_writer(u'\n<a href="/" >\n    \t<img src="/assets/flag_button.png" id="w-top-navigation-bar-flag-incorrect-button">\n</a>\n</div>\n <div class="wnavigation-bar">\n    <a href="/" id="wnavigation-bar-article-button" class="navigation-bar-button selected-navigation-bar-button">Article</a>\n    <a href="/" id="wnavigation-bar-talk-button" class="navigation-bar-button">Talk</a>\n    <a href="/" id="wnavigation-bar-document-revision-button" class="navigation-bar-button">Revision</a>\n\t</div>\n</div>\n<div class="wBlockOne">\n<img src="/assets/logoplaceholder.png" alt="#" style="height: 100px; display:block;margin-left: auto;margin-right: auto;">\n<p id="wTitle">')
        __M_writer(escape(name))
        __M_writer(u'</p>\n<p id="wStatus">')
        __M_writer(escape(status))
        __M_writer(u'</p>\n<hr />\n</div>\n<div class="wBlockTwo">\n<div class="rowAlign">\n  <div class="rowTextBlock">\n  <p>Contact Info</p>\n  <a>')
        __M_writer(escape(website_url))
        __M_writer(u'</a>\n  <br/>\n\t<div id="w-address">  \n\t<p><img src="/assets/pin_map.png" alt="" style="width:8px;height: 10px;">')
        __M_writer(escape(address))
        __M_writer(u'</p> \n  </div> \n  </div>\n  <div class="rowTextBlock">\n   <p>Social Media</p>\n   <div class="social-media-block">\n   <a href="#"  id="w-social-button" >\n\t   <img src="/assets/social_twitter.png" class="w-social-button" >\n   </a>\n   <a href="#"  id="w-social-gplus" >\n\t<img src="/assets/social_google+.png" class="w-social-button">   \n   </a>\n   <a href="#" id="w-social-meetup">\n\t<img src="/assets/social_meetup.png"  class="w-social-button">   \n   </a>\n   <a href="#" id="w-social-fablab" >\n   <img src="/assets/social_fablab.png"  class="w-social-button">   \n   \t</a>\n   <a href="#"  id="w-social-facebook">\n\t<img src="/assets/social_facebook.png"  class="w-social-button">      \n   </a>\n   <a href="#"  id="w-social-jabber">\n\t<img src="/assets/social_jabber.png"  class="w-social-button">      \n   </a>\n   <a href="#" id="w-social-linkedin">\n\t<img src="/assets/social_linkedin.png"  class="w-social-button">      \n   </a>\n   </div>\n  </div>\n  <div class="rowTextBlock">\n  <p>Service</p>\n  <ul style="text-align: left;"><li>')
        __M_writer(escape(primarytype))
        __M_writer(u'</li><li>')
        __M_writer(escape(secondarytype))
        __M_writer(u'</li></ul>\n  </div>\n  <div class="rowTextBlock">\n  <p>Capabilities</p>\n  <p>Machines_spaceholder</p>\n  </div>\n</div>\n<hr/>\n</div>\n\n<div class="wBlockTh">\n<div  class="w-block-left">\n   <img src="/assets/social_fablab.png" alt="#" style="width:100%;">   \n  </div>\n<div class="w-block-right"> \n\t<p id="w-space-description">')
        __M_writer(escape(space_description))
        __M_writer(u'</p>\n</div>\n<br/>\n</div>\n<div id="show-more-section">\n<button id="show-more-button" onclick="show_more_wiki()"></button>\n<hr/>\n</div>\n\n</div>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 10, "33": 16, "34": 16, "35": 29, "36": 29, "37": 30, "38": 30, "39": 37, "40": 37, "41": 40, "42": 40, "43": 71, "44": 71, "45": 71, "46": 71, "47": 86, "48": 86, "17": 0, "54": 48, "30": 1, "31": 10}, "uri": "/wikipage.html", "filename": "/home/ubuntu/isproject/map-of-innovation/mapofinnovation/templates/wikipage.html"}
__M_END_METADATA
"""
