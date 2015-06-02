import inspect
import subprocess as sub
import sys, os, re, json, yaml, urllib2
from datetime import datetime, timedelta
import readline
import rlcompleter

if 'libedit' in readline.__doc__:
    readline.parse_and_bind("bind ^I rl_complete")
    readline.parse_and_bind("bind ^R em-inc-search-prev")
else:
    readline.parse_and_bind("tab: complete")

def attrs(obj=None, show=None, depth=0):
    if not obj:
        #Equivalent to empty dir() from top level interpreter
        frame = inspect.currentframe().f_back
        attrlist = frame.f_locals
        typer = lambda attr: type(attrlist[attr])
    else:
        attrlist = dir(obj)
        typer = lambda attr: type(getattr(obj, attr))
    attrfilter = lambda attr: not attr.startswith("_")
    if depth == 1:
        attrfilter = lambda attr: not attr.startswith("__")
    if depth == 2:
        attrfilter = lambda attr: True
    attrs = [ attr for attr in attrlist if attrfilter(attr)]
    types = [ typer(attr) for attr in attrs ]
    vals = sorted(zip(attrs,types), key=lambda x: str(x[1]))
    if show:
        vals = [ val for val in vals if any( showtype in str(val[0]) for showtype in show ) ]
    fmtdict(vals, align=True)

def fmtdict(d, align=False):
    if type(d) == list and type(d[0]) == tuple:
        keys = [ i[0] for i in d ]
        tuples = d
    else:
        keys = d.keys()
        tuples = d.items()
    fmt = "{k}:{spc}{v}"
    if not align:
        print "\n".join("{k}: {v}".format(k=k, v=v) for k,v in tuples)
    else:
        maxlen = max(len(str(k)) for k in keys) + 1
        print "\n".join("{k}:{spc}{v}".format(k=k, spc=" "*(maxlen-len(str(k))), v=v) for k,v in tuples)

def byline(l):
    print "\n".join(str(i) for i in l)
keys=byline

def pp(obj):
    print json.dumps(obj, indent=2)

def pickkeys(obj, *keys):
    return { key: obj[key] for key in keys}

def writeto(buffer, f):
    with open(f, "w") as out:
        out.write(buffer)
