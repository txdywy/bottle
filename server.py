from bottle import route, run, template, request, abort, redirect, response
import bottle


app = application = bottle.app()


# -----------------------------------------------------------------------------------
# Web server Get method
@route('/<path>', method='GET')
def index(path):
    print "----------------- Begin ----------------------"
    redirect("www.google.com")