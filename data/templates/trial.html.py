# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1481320221.497271
_enable_loop = True
_template_filename = '/home/ubuntu/isproject/map-of-innovation/mapofinnovation/templates/trial.html'
_template_uri = '/trial.html'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        last_updated = context.get('last_updated', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<html>\n<head>\n<link rel="stylesheet" type="text/css" href="/css/wikipage.css"/>\n<link rel="stylesheet" type="text/css" href="/css/stylesheet.css"/>\n<script type=\'text/javascript\' src=\'/js/wiki.js\'></script>\n<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>\n</head>\n<body>\n<p> trying this </p>\n<div class="wBlockHeader">\n<div class="w-top-navigation">\n<a href="/" >\n        <img src="/assets/edit_button.png" id="w-top-navigation-bar-edit-button">\n</a> Last updated :')
        __M_writer(escape(last_updated))
        __M_writer(u'\n<a href="/" >\n        <img src="/assets/flag_button.png" id="w-top-navigation-bar-flag-incorrect-button">\n</a>\n</div>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"24": 14, "17": 0, "31": 25, "25": 14, "23": 1}, "uri": "/trial.html", "filename": "/home/ubuntu/isproject/map-of-innovation/mapofinnovation/templates/trial.html"}
__M_END_METADATA
"""
