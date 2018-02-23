# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1519276871.3284273
_enable_loop = True
_template_filename = 'C:/Users/conno/Desktop/Riley/homepage/templates/text.html'
_template_uri = 'text.html'
_source_encoding = 'utf-8'
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
        def content():
            return render_content(context._locals(__M_locals))
        csrf_input = context.get('csrf_input', UNDEFINED)
        form = context.get('form', UNDEFINED)
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
        def content():
            return render_content(context)
        csrf_input = context.get('csrf_input', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\t<h1>Text with Twilio Testing</h1>\r\n\r\n\t<form action="/text" method="post">')
        __M_writer(str( csrf_input ))
        __M_writer('\r\n\t\t<div class="form-group">')
        __M_writer(str( form ))
        __M_writer('</div>\r\n\t\t  <button type="submit">Send</button>\r\n\t\t<div class="clearfix"></div>\r\n\t</form>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/conno/Desktop/Riley/homepage/templates/text.html", "uri": "text.html", "source_encoding": "utf-8", "line_map": {"27": 0, "36": 1, "46": 3, "54": 3, "55": 7, "56": 7, "57": 8, "58": 8, "64": 58}}
__M_END_METADATA
"""
