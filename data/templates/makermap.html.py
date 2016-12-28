# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1481661756.769149
_enable_loop = True
_template_filename = '/home/ubuntu/isproject/map-of-innovation/mapofinnovation/templates/makermap.html'
_template_uri = '/makermap.html'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<html>\n<head>\n\t<link href="https://fonts.googleapis.com/css?family=Libre+Baskerville|Source+Sans+Pro:200,300,300i,400,600" rel="stylesheet">\n\t<link rel="stylesheet" type="text/css" href="/css/leaflet.css" />\n    <link rel="stylesheet" type="text/css" href="/css/MarkerCluster.css" />\n    <link rel="stylesheet" type="text/css" href="/css/MarkerCluster.Default.css" />\n    <link rel="stylesheet" type="text/css" href="/css/stylesheet.css" />\n    <script type=\'text/javascript\' src="/js/leaflet.js"></script>\n\t\t<script type=\'text/javascript\' src=\'/js/leaflet.markercluster.js\'></script>\n\t\t<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>\n    <title>Ananse Innovation Map</title>\n</head>\n<body>\n\n    ')
        runtime._include_file(context, u'/snippets/header.html', _template_uri)
        __M_writer(u'\n\n    ')
        runtime._include_file(context, u'/snippets/contribute.html', _template_uri)
        __M_writer(u'\n\n    <div id="map-page-title-container">\n    \t<h1 id="map-page-title">Innovation Spaces Near And Far</h1>\n    </div>\n    <div id="map-container">\n\t    <div id="map"></div>\n    </div>\n    <div id="filters">\n    \t<ul id="type-filter" class="filter-menu">\n')
        for a in ("All", "Hub", "Event", "Gallery", "Retail", "Virtual", "Ecovillage", "Cluster"):
            __M_writer(u'                <li>\n                    <a href="#" class="filter-item" data-filter-group="type" data-filter-item="')
            __M_writer(escape(a.lower()))
            __M_writer(u'">\n                        <div class="filter-type-color ')
            __M_writer(escape(a.lower()))
            __M_writer(u'-color"></div>')
            __M_writer(escape(a))
            __M_writer(u'\n                    </a>\n                </li>\n')
        __M_writer(u'<!--     \t\t<li><a href="#" class="filter-item" data-filter-group="type" data-filter-item="factory">Factory</a></li>\n\t\t\t\t<li><a href="#" class="filter-item" data-filter-group="type" data-filter-item="library">Library</a></li>\n    \t\t<li><a href="#" class="filter-item" data-filter-group="type" data-filter-item="lab">Lab</a></li>  -->\n    \t</ul>\n    \t<ul id="theme-filter" class="filter-menu">\n    \t\n    \t</ul>\n    \t<ul id="originator-filter" class="filter-menu">\n    \t\n    \t</ul>\n    </div>\n    <div id="filter-bar">\n')
        for a in ("Type", "Theme", "Originator"):
            __M_writer(u'                <a href="/" id="filter-bar-type-button" class="filter-bar-button" data-filter="')
            __M_writer(escape(a.lower()))
            __M_writer(u'">\n                    <span class="filter-button-text">')
            __M_writer(escape(a))
            __M_writer(u'</span>\n                    <img src="/assets/plus.png" class="filter-button-plus">\n                    <img src="/assets/minus.png" class="filter-button-minus">\n                </a>\n')
        __M_writer(u'            <div id="sponsor-container">\n<!--                <span id="navigation-bar-supported-text">Supported by</span> --!>\n                <a href="https://www.giz.de/" target="_blank">\n                    <img src="/assets/giz-logo.png" id="sponsor-giz">\n                </a>\n                <a href="https://www.fabfoundation.org/" target="_blank">\n                    <img src="/assets/fab-foundation-logo.png" id="sponsor-fab-foundation">\n                </a>\n            </div>\n\t\t</div>\n    <p id="markerjson" hidden>')
        __M_writer(escape(c.markers))
        __M_writer(u'</p>\n    <script type=\'text/javascript\' src="/js/main.js"></script>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"17": 0, "23": 1, "24": 15, "25": 15, "26": 17, "27": 17, "28": 27, "29": 28, "30": 29, "31": 29, "32": 30, "33": 30, "34": 30, "35": 30, "36": 34, "37": 46, "38": 47, "39": 47, "40": 47, "41": 48, "42": 48, "43": 53, "44": 63, "45": 63, "51": 45}, "uri": "/makermap.html", "filename": "/home/ubuntu/isproject/map-of-innovation/mapofinnovation/templates/makermap.html"}
__M_END_METADATA
"""
