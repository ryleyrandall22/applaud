# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1519425178.4858708
_enable_loop = True
_template_filename = 'C:/Users/HerbGlitch/Desktop/BrightBridgeWeb/applaud/applaud/homepage/templates/login.html'
_template_uri = 'login.html'
_source_encoding = 'utf-8'
from django_mako_plus import django_syntax, jinja2_syntax, alternate_syntax
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def __M_anon_6():
            __M_caller = context.caller_stack._push_frame()
            try:
                context._push_buffer()
                __M_writer = context.writer()
                __M_writer('\r\n<a href="{% url \'social:begin\' \'google-oauth2\' %}">Login with Google</a><br>\r\n<a href="{% url \'social:begin\' \'facebook\' %}">Login with Facebook</a>\r\n')
            finally:
                __M_buf, __M_writer = context._pop_buffer_and_writer()
                context.caller_stack._pop_frame()
            __M_writer(django_syntax(local, titles=titles)(__M_buf.getvalue()))
            return ''
        local = context.get('local', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer(django_syntax(local)(str( '{{ name }}' )))
        __M_writer('\r\n\r\n')
        titles = [ 'First', 'Second', 'Third' ] 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['titles'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n')
        __M_anon_6()
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/HerbGlitch/Desktop/BrightBridgeWeb/applaud/applaud/homepage/templates/login.html", "uri": "login.html", "source_encoding": "utf-8", "line_map": {"17": 0, "26": 6, "34": 1, "35": 2, "36": 2, "37": 5, "41": 5, "43": 9, "49": 43}}
__M_END_METADATA
"""
