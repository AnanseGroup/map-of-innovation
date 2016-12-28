# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1481639919.375693
_enable_loop = True
_template_filename = u'/home/ubuntu/isproject/map-of-innovation/mapofinnovation/templates/snippets/header.html'
_template_uri = u'/snippets/header.html'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'<div id="navigation-bar-container">\n  <a href="/">\n    <img src="/assets/logo_ananse.png" id="navigation-bar-home">\n  </a>\n  <div class="navigation-bar">\n    <a href="/" id="navigation-bar-map-button" class="navigation-bar-button selected-navigation-bar-button">MAP</a>\n    <a href="/" id="navigation-bar-about-button" class="navigation-bar-button">ABOUT</a>\n    <a href="/" id="navigation-bar-document-licensing-button" class="navigation-bar-button">DOCUMENTATION & LICENSING</a>\n    <a href="/" id="navigation-bar-wiki-button" class="navigation-bar-button">WIKI</a>\n\t</div>\n\t<div class="navigation-bar-contact-container">\n\t\t<a href="/">\n    \t<img src="/assets/contact_us.png" id="navigation-bar-contact-button">\n    </a>\n\t</div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"17": 0, "28": 22, "22": 1}, "uri": "/snippets/header.html", "filename": "/home/ubuntu/isproject/map-of-innovation/mapofinnovation/templates/snippets/header.html"}
__M_END_METADATA
"""
