# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1519429177.8971155
_enable_loop = True
_template_filename = 'C:/Users/HerbGlitch/Desktop/BrightBridgeWeb/applaud/applaud/homepage/templates/index.html'
_template_uri = 'index.html'
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
        user = context.get('user', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        user = context.get('user', UNDEFINED)
        def content():
            return render_content(context)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if not request.user.is_authenticated:
            __M_writer('    <p class="display-4">Hello, ')
            __M_writer(str( user.username ))
            __M_writer('</p>\r\n')
        else:
            __M_writer('    <a class="lead" href="{% url \'login\' %}">Log in</a>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/HerbGlitch/Desktop/BrightBridgeWeb/applaud/applaud/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"28": 0, "37": 1, "42": 9, "48": 3, "56": 3, "57": 4, "58": 5, "59": 5, "60": 5, "61": 6, "62": 7, "68": 62}}
__M_END_METADATA
"""
