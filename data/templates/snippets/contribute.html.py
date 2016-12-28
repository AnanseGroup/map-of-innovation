# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1481661756.775927
_enable_loop = True
_template_filename = u'/home/ubuntu/isproject/map-of-innovation/mapofinnovation/templates/snippets/contribute.html'
_template_uri = u'/snippets/contribute.html'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'<div id="contribute-bar-container" class="closed source-sans">\n\t<a href="#" id="contribute-bar-button">CONTRIBUTE</a>\n<!--   <div class="search-bar-container">\n    <input type="text" name="searchbar" class="search-bar">\n    <img src="../assets/search.png" id="magnifying-glass">\n\t</div> -->\n\t<div id="contribute-content">\n\t\t<h2 class="header">WELCOME!</h2>\n\t\t<p>Ever find yourself wondering, <em>where are all the crazy creative people?</em> We\u2019re building an open wiki-database of all the community innovation spaces.</p>\n\t\t<a href="#" class="button pink">JOIN US</a>\n\t</div>\n</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"17": 0, "28": 22, "22": 1}, "uri": "/snippets/contribute.html", "filename": "/home/ubuntu/isproject/map-of-innovation/mapofinnovation/templates/snippets/contribute.html"}
__M_END_METADATA
"""
