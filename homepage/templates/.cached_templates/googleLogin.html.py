# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1519433491.4053051
_enable_loop = True
_template_filename = 'C:/Users/conno/Desktop/Riley/homepage/templates/googleLogin.html'
_template_uri = 'googleLogin.html'
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
        local = context.get('local', UNDEFINED)
        def __M_anon_8():
            __M_caller = context.caller_stack._push_frame()
            try:
                context._push_buffer()
                __M_writer = context.writer()
                __M_writer('\r\n\r\n<div class="container-fluid">\r\n\r\n\t<div class="col-md-12">\r\n\r\n\t\t<a href="{% url \'social:begin\' \'google-oauth2\' %}"><button class="btn btn-danger">Login with Google</button></a>\r\n\r\n\t</div>\r\n\r\n</div>\r\n\r\n\r\n')
            finally:
                __M_buf, __M_writer = context._pop_buffer_and_writer()
                context.caller_stack._pop_frame()
            __M_writer(django_syntax(local, titles=titles)(__M_buf.getvalue()))
            return ''
        def content():
            return render_content(context._locals(__M_locals))
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
        local = context.get('local', UNDEFINED)
        def __M_anon_8():
            __M_caller = context.caller_stack._push_frame()
            try:
                context._push_buffer()
                __M_writer = context.writer()
                __M_writer('\r\n\r\n<div class="container-fluid">\r\n\r\n\t<div class="col-md-12">\r\n\r\n\t\t<a href="{% url \'social:begin\' \'google-oauth2\' %}"><button class="btn btn-danger">Login with Google</button></a>\r\n\r\n\t</div>\r\n\r\n</div>\r\n\r\n\r\n')
            finally:
                __M_buf, __M_writer = context._pop_buffer_and_writer()
                context.caller_stack._pop_frame()
            __M_writer(django_syntax(local, titles=titles)(__M_buf.getvalue()))
            return ''
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        __M_writer(django_syntax(local)(str( '{{ name }}' )))
        __M_writer('\r\n')
        titles = [ 'First', 'Second', 'Third' ] 
        
        __M_writer('\r\n')
        __M_anon_8()
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/conno/Desktop/Riley/homepage/templates/googleLogin.html", "uri": "googleLogin.html", "source_encoding": "utf-8", "line_map": {"28": 0, "38": 8, "47": 1, "52": 23, "58": 3, "67": 8, "76": 3, "77": 5, "78": 5, "79": 7, "81": 7, "83": 21, "89": 83}}
__M_END_METADATA
"""
