from bottle import route, request, run, template, static_file
from subprocess import call

frozen=0

def sendMail(subj, body):
    cmdStr = "echo '" + body + "'"
    cmdStr += " | "
    cmdStr += "mail -s '" + subj + "'"
    cmdStr += " david.storch@10gen.com"
    call(cmdStr, shell=True)

@route('/githook')
def index():
    return str(frozen)

@route('/freeze', method="POST")
def freeze():
    global frozen
    frozen=1
    msg = request.forms.get("msg")
    if not msg:
        msg = ""
    sendMail("CODE FREEZE", msg)
    return template("toggle", frozen=frozen)

@route('/unfreeze', method="POST")
def unfreeze():
    global frozen
    frozen=0
    msg = request.forms.get("msg")
    if not msg:
        msg = ""
    sendMail("CODE FREEZE LIFTED", msg)
    return template("toggle", frozen=frozen)

@route('/static/button')
def button():
    return static_file("bigredbutton.jpg", root="/Users/dstorch/code/isbuildfrozen/")

@route('/')
def unfreeze():
    global frozen
    return template("toggle", frozen=frozen)

run(host='localhost', port=8080)
