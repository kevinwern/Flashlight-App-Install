import os
import urllib

def results(fields, original_query):
    message = fields['~message']
    query_data = {'entity': 'macSoftware', 'term': message}
    query_string = urllib.urlencode(query_data)
    html = open(os.path.join(os.getcwd(),'main.html')).read()
    return {
        "title": "Install apps: '{0}'".format(message),
        "run_args": [message],
        "html" : html % (query_string),
        "webview_links_open_in_browser" : True
    }

def run(message):
    os.system('"Install apps: {0}"'.format(message))
