# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1519167947.2370179
_enable_loop = True
_template_filename = 'C:/Users/conno/Desktop/Riley/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
_exports = ['content']


from django_mako_plus import get_template_css, get_template_js 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n    <meta charset="UTF-8">\r\n    <head>\r\n\r\n        <title>DMP</title>\r\n\r\n')
        __M_writer('        <script src="http://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>\r\n\r\n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\r\n        ')
        __M_writer('\r\n        ')
        __M_writer(str( get_template_css(self, request, context) ))
        __M_writer('\r\n\r\n    </head>\r\n    <body>\r\n\r\n        <header>\r\n        </header>\r\n\r\n        <main>\r\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n        </main>\r\n\r\n    </body>\r\n\r\n    ')
        __M_writer(str( get_template_js(self, request, context) ))
        __M_writer('\r\n\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n                Site content goes here in sub-templates.\r\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/conno/Desktop/Riley/homepage/templates/base.htm", "uri": "base.htm", "source_encoding": "utf-8", "line_map": {"16": 14, "18": 0, "27": 2, "28": 10, "29": 13, "30": 14, "31": 15, "32": 15, "37": 26, "38": 31, "39": 31, "45": 24, "51": 24, "57": 51}}
__M_END_METADATA
"""
