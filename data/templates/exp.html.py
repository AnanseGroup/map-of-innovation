# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1481321215.902124
_enable_loop = True
_template_filename = u'/home/ubuntu/isproject/map-of-innovation/mapofinnovation/templates/exp.html'
_template_uri = u'/exp.html'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'<div id="show-more-container" class="close">\n<div class="wBlockFour">\n<hr/>\n\t<div class="rowAlign">\n  \t\t<div class="rowTextBlock">\n\t\t<p>Host</p>  \n  \t\t</div>\n  \t\t<div class="rowTextBlock">\n  \t\t<p>\tTags</p>\n  \t\t</div> \n  \t\t<div class="rowTextBlock">\n  \t\t<p>Access</p>  \n  \t\t</div>\n  \t\t<div class="rowTextBlock">  \n  \t\t<p>Size</p>\n  \t\t</div>\n\n\t</div>\n\t<hr/>\n</div>\n\n<div class="wBlockLast">\n\t<div class="rowAlign">\n  \t\t<div class="rowTextBlock">\n  \t\t\t<p>Documentation Links</p>\n  \t\t</div>\n  \t\t<div class="rowTextBlock">\n  \t\t\t<p>Accessibility by Public Transport</p>\n  \t\t</div>\n  \t\t<div class="rowTextBlock">\n\t\t\t<p>Materials to Use </p>  \n  \t\t</div>\n  \t\t<div class="rowTextBlock">\n  \t\t\t<p>Residencies</p>\n  \t\t</div>\n\t</div>\t\n</div>\n<button id="show-less-button" onclick="show_less_wiki()"></button>\n</div>\n\n<div id="show-more-container" class="hide"></div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"17": 0, "28": 22, "22": 1}, "uri": "/exp.html", "filename": "/home/ubuntu/isproject/map-of-innovation/mapofinnovation/templates/exp.html"}
__M_END_METADATA
"""
