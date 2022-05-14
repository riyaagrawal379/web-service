from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/my-first-api', methods=['GET'])
def homepage():
    return render_template("index.html")


# ------------------------------------------------------------------ STARTS BROWSER -------------------------------------------------------#

@app.route('/start', methods=['GET'])
def start():
    if 'browser' in request.args:
        browser_name = str(request.args['browser'])
        url = str(request.args['url'])
        if browser_name == "chrome":
            import webbrowser

            chrome_path = '/usr/bin/google-chrome %s'
            webbrowser.get(chrome_path).open(url)
            return "Chrome fired up with specified url"

        elif browser_name == "mozilla":
            import webbrowser
            mozilla_path = '/usr/bin/firefox %s'
            webbrowser.get(mozilla_path).open(url)
            return "Mozilla fired up with specified url"

        else:
            return "This browser isn't available"


# ------------------------------------------------------------- STOPS BROWESER ---------------------------------------------------------------#

@app.route('/stop', methods=['GET'])
def stop():
    if 'browser' in request.args:

        browser_name = str(request.args['browser'])

        if browser_name == "chrome":
            import os
            browserExe = "chrome"
            os.system("pkill " + browserExe)
            return "CHROME CLOSED"

        elif browser_name == "mozilla":
            import os
            os.system("pkill " + "firefox")
            return "MOZILLA CLOSED"

        else:
            return "This browser isnt available"