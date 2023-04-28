from django.shortcuts import render
from markdown2 import Markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def css(request):
    markdowner=Markdown()
    return render(request,"encyclopedia/css.html", {
        "css_content": markdowner.convert(util.get_entry('CSS'))
    })


