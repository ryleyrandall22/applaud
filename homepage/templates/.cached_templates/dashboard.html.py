# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1519432442.340921
_enable_loop = True
_template_filename = 'C:/Users/conno/Desktop/Riley/homepage/templates/dashboard.html'
_template_uri = 'dashboard.html'
_source_encoding = 'utf-8'
from django_mako_plus import django_syntax, jinja2_syntax, alternate_syntax
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<nav id="navbar-inverse" class="navbar navbar-inverse navbar-fixed-left">\r\n\t<div class="container">\r\n\t  <div class="navbar-header">\r\n\t    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">\r\n\t      <span class="sr-only">Toggle navigation</span>\r\n\t      <span class="icon-bar"></span>\r\n\t      <span class="icon-bar"></span>\r\n\t      <span class="icon-bar"></span>\r\n\t    </button>\r\n\t    <img class="navbar-brand" id="profile" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/logo2.png"/>\r\n\t  </div>\r\n\t  <div id="navbar" class="navbar-collapse collapse">\r\n\t    <ul class="nav navbar-nav">\r\n\t      <li><a href="#">Dashboard</a></li>\r\n\t      <li><a href="#">Google</a></li>\r\n\t      <li><a href="#">Facebook</a></li>\r\n\t      <li><a href="#">Instagram</a></li>\r\n\r\n\t      <li><button id="customer" class="btn btn-info">Customer View</button></li>\r\n\t    </ul>\r\n\r\n\t    <img id="profile2" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/logo.png"/>\r\n\t  </div>\r\n\t</div>\r\n</nav>\r\n\r\n\r\n<div class="container">\r\n\r\n\t<div class="col-md-12">\r\n\r\n\t\t<h1>Dashboard</h1>\r\n\r\n\t</div>\r\n\r\n</div>\r\n\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/conno/Desktop/Riley/homepage/templates/dashboard.html", "uri": "dashboard.html", "source_encoding": "utf-8", "line_map": {"28": 0, "36": 1, "46": 3, "53": 3, "54": 14, "55": 14, "56": 26, "57": 26, "63": 57}}
__M_END_METADATA
"""
