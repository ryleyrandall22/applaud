# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
<<<<<<< HEAD
_modified_time = 1519432442.340921
=======
_modified_time = 1519454424.8582048
>>>>>>> jessica
_enable_loop = True
_template_filename = '/Users/SamNYiran/Desktop/CodingLife/riley/Applaud/homepage/templates/dashboard.html'
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
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
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
        __M_writer('\n\n<nav id="navbar-inverse" class="navbar navbar-inverse navbar-fixed-left">\n\t<div class="container">\n\t  <div class="navbar-header">\n\t    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">\n\t      <span class="sr-only">Toggle navigation</span>\n\t      <span class="icon-bar"></span>\n\t      <span class="icon-bar"></span>\n\t      <span class="icon-bar"></span>\n\t    </button>\n\t    <img class="navbar-brand" id="profile" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/logo2.png"/>\n\t  </div>\n\t  <div id="navbar" class="navbar-collapse collapse">\n\t    <ul class="nav navbar-nav">\n\t      <li><a href="#">Dashboard</a></li>\n\t      <li><a href="#">Google</a></li>\n\t      <li><a href="#">Facebook</a></li>\n\t      <li><a href="#">Instagram</a></li>\n\n\t      <li><button id="customer" class="btn btn-info">Customer View</button></li>\n\t    </ul>\n\n\t    <img id="profile2" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/logo.png"/>\n\t  </div>\n\t</div>\n</nav>\n\n\n<!-- <div style="height: 100vh"> -->\n\n\t<!-- <div class="col-md-12"> -->\n\n\t\t<div class="section_box">\n\t\t\t<div class="reivews_sec">Reviews</div>\n\t\t\t\t<div class="review_innersec" style="width: 65%">\n\t\t\t\t\t\t<div class="reviews_top_stat">\n\t\t\t\t\t\t\t\t<div class="inner_top_stat">\n\t\t\t\t\t\t\t\t\t<div class="stat_inner">Search Appearance This Month</div>\n\t\t\t\t\t\t\t\t\t<div class="stat_inner stat_num">142</div>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t<div class="inner_top_stat">\n\t\t\t\t\t\t\t\t\t<div class="stat_inner">Average Rating</div>\n\t\t\t\t\t\t\t\t\t<div class="stat_inner stat_num">4.0</div>\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t<div class="most_recent_reviews">\n\t\t\t\t\t\t\t<div class="reivews_sec">Most Recent Reviews</div>\n\t\t\t\t\t\t\t<!-- <div class="each_review"></div>\n\t\t\t\t\t\t\t<div class="each_review"></div>\n\t\t\t\t\t\t\t<div class="each_review"></div>\n\t\t\t\t\t\t\t<div class="each_review"></div> -->\n\t\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t\t<div class="review_innersec" style="width: 35%">\n\t\t\t\t\t<div class="inner_right_box">\n\t\t\t\t\t\t<div style="text-align: center; font-size: 20px;">New Review SMS</div>\n\t\t\t\t\t\t<div class="inner_right_box_left" style="margin-left: 5px;">\n\t\t\t\t\t\t\t<div style="margin-top: 10px;">Name:</div>\n\t\t\t\t\t\t\t<input />\n\t\t\t\t\t\t\t<div>Phone:</div>\n\t\t\t\t\t\t\t<input />\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t<div class="inner_right_box_left send_box"><button>Send</button></div>\n\t\t\t\t\t</div>\n\t\t\t\t\t<div class="inner_right_box">\n\t\t\t\t\t\t\t<div class="reivews_sec">Total Reviews</div>\n\t\t\t\t\t\t\t<div class="right_box_lower_inner">47</div>\n\t\t\t\t\t\t\t<div class="right_box_lower_inner"></div>\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t</div>\n\n\t\t<div class="section_box">\n\t\t\t<div class="reivews_sec">Social</div>\n\t\t\t<div class="social_box" style="height: 80px;">\n\t\t\t\t\t<div class="social_box_sec">\n\t\t\t\t\t\t<div class="social_box_sectitle">Followers:</div>\n\t\t\t\t\t\t<div class="social_box_secnumb">1212</div>\n\t\t\t\t\t</div>\n\t\t\t\t\t<div class="social_box_sec">\n\t\t\t\t\t\t<div class="social_box_sectitle">Profile Views:</div>\n\t\t\t\t\t\t<div class="social_box_secnumb">1212</div>\n\t\t\t\t\t</div>\n\t\t\t\t\t<div class="social_box_sec">\n\t\t\t\t\t\t<div class="social_box_sectitle">Total Engagement:</div>\n\t\t\t\t\t\t<div class="social_box_secnumb">1212</div>\n\t\t\t\t\t</div>\n\t\t\t\t\t<div class="social_box_sec">\n\t\t\t\t\t\t<div class="social_box_sectitle">Page Likes:</div>\n\t\t\t\t\t\t<div class="social_box_secnumb">1212</div>\n\t\t\t\t\t</div>\n\t\t\t\t\t<div class="social_box_sec">\n\t\t\t\t\t\t<div class="social_box_sectitle">Page Views:</div>\n\t\t\t\t\t\t<div class="social_box_secnumb">1212</div>\n\t\t\t\t\t</div>\n\t\t\t\t\t<div class="social_box_sec">\n\t\t\t\t\t\t<div class="social_box_sectitle">Page Actions:</div>\n\t\t\t\t\t\t<div class="social_box_secnumb">1212</div>\n\t\t\t\t\t</div>\n\t\t\t</div>\n\t\t\t<div class="social_box">\n\t\t\t\t<div class="social_graph_box">\n\t\t\t\t\t<div class="reivews_sec">Instagram Link Clicks</div>\n\t\t\t\t\t<div class="social_graph_box_inner"></div>\n\t\t\t\t\t<div class="social_graph_box_inner social_num">8</div>\n\t\t\t\t</div>\n\t\t\t\t<div class="social_graph_box">\n\t\t\t\t\t<div class="reivews_sec">Facebook Reach</div>\n\t\t\t\t\t<div class="social_graph_box_inner"></div>\n\t\t\t\t\t<div class="social_graph_box_inner social_num">21</div>\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t</div>\n\n\t<!-- </div> -->\n\n<!-- </div> -->\n\n<style>\nbody {\n\tfont-family: Helvetica;\n}\n\n\n.section_box {\n\twidth: 98%;\n\theight: 380px;\n\tborder: 4px solid lightgray;\n\tmargin: 0 auto;\n\tmargin-bottom: 15px;\n}\n\n.reivews_sec {\n\twidth: 100%;\n\theight: 35px;\n\tbackground: lightgray;\n\tdisplay: flex;\n\tjustify-content: center;\n\talign-items: center;\n\tfont-size: 18px;\n\tfont-weight: bold;\n\n}\n\n.review_innersec {\n\theight: calc(100% - 35px);\n\tborder: 1px solid lightgray;\n\twidth: 50%;\n\tfloat: left;\n}\n\n.inner_top_stat {\n\twidth: 50%;\n  border: 2px solid lightgray;\n  float: left;\n  height: 85px;\n}\n\n.stat_inner {\n\tfloat: left;\n\twidth: 50%;\n\theight: 100%;\n\ttext-align: center;\n\tfont-size: 20px;\n\tmargin-top: 10px;\n\tcolor: #87aea0;\n}\n\n.each_review {\n\theight: 54px;\n\tborder: 2px solid gray;\n}\n\n.inner_right_box {\n\theight: 50%;\n}\n\n.right_box_lower_inner {\n\twidth: 50%;\n\tfont-size: 80px;\n\tfont-size: lightgreen;\n\ttext-align: center;\n\tcolor: #87aea0;\n}\n\n.inner_right_box_left {\n\twidth: 49%;\n\t/* border: 2px solid red; */\n\tfloat: left;\n\theight: calc(100% - 35px)\n}\n\n.inner_right_box_left button {\n\twidth: 80%;\n\theight: 60%;\n\tbackground-color: #87aea0;\n\tborder-radius: 10px;\n\tcolor: white;\n\tmargin-left: 15px;\n\tmargin-top: 25px;\n}\n\n.inner_right_box_left input {\n\tborder: 2px solid gray;\n}\n\n.social_box_sec {\n\tborder: 2px solid lightgray;\n\theight: 100%;\n\twidth: calc(100% / 6);\n\tfloat: left;\n}\n\n.social_box_sectitle {\n\tfont-size: 17px;\n\tfont-style: bold;\n\tmargin-left: 5px;\n}\n\n.social_box_secnumb {\n\tfont-size: 28px;\n\ttext-align: center;\n\tcolor: #87aea0;\n\tmargin-top: 5px;\n}\n\n.social_graph_box {\n\twidth: 50%;\n\theight: 260px;\n\tfloat: left;\n\tborder: 2px solid lightgray;\n}\n\n.social_graph_box_inner {\n\twidth: 50%;\n\ttext-align: center;\n\tfont-size: 80px;\n\tcolor: #87aea0;\n\tfloat: left;\n\theight: 100px;\n}\n\n.social_num {\n\tmargin-top: 45px;\n}\n\n.stat_num {\n\tfont-size: 65px;\n\tmargin-top: -10px;\n}\n\n@media (max-width: 1400px) {\n\t.stat_inner {\n\t\tfont-size: 15px;\n\t}\n\t.stat_num {\n\t\tfont-size: 50px;\n\t}\n\t.send_box {\n\t\tdisplay: none;\n\t}\n\t.social_box_sectitle {\n\t\tfont-size: 15px;\n\t}\n\t.right_box_lower_inner {\n\t\tfont-size: 65px;\n\t\tmargin-top: 20px;\n\t}\n}\n</style>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
<<<<<<< HEAD
{"filename": "C:/Users/conno/Desktop/Riley/homepage/templates/dashboard.html", "uri": "dashboard.html", "source_encoding": "utf-8", "line_map": {"28": 0, "36": 1, "46": 3, "53": 3, "54": 14, "55": 14, "56": 26, "57": 26, "63": 57}}
=======
{"filename": "/Users/SamNYiran/Desktop/CodingLife/riley/Applaud/homepage/templates/dashboard.html", "uri": "dashboard.html", "source_encoding": "utf-8", "line_map": {"27": 0, "35": 1, "40": 275, "46": 3, "53": 3, "54": 14, "55": 14, "56": 26, "57": 26, "63": 57}}
>>>>>>> jessica
__M_END_METADATA
"""
