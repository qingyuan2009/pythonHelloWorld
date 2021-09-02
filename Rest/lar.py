# Local App Router

import requests
import json
import socket
import ctypes
import os
import time
import sys
import re
import subprocess

# import logging
try:
    from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
except ImportError:
    from http.server import HTTPServer, BaseHTTPRequestHandler
try:
    from SocketServer import ThreadingMixIn
except ImportError:
    from socketserver import ThreadingMixIn

_python_v3 = (sys.version_info >= (3, 0))

# Configurable vars
conf_auth_url = "https://sap-health-validation-sat.authentication.eu10.hana.ondemand.com/oauth/token"
conf_client_id = "sb-hl7-fhir-service-785fbe06-affb-4e1a-a60d-a70c599ae8e8!b41899|hl7-fhir-service-staging!b41344"
conf_client_secret = "2gqo1fFh1tCJOn72sCfBxpxhj0w="

conf_username = "someone@sap.com"
conf_password = "************"

# conf_static_home = "/home/vagrant/pa-2021/cost-accounting-ui/skfCOFieldAssignmentUI/webapp"
# conf_static_home = "/home/vagrant/pa-2021/mdc-poc/billing-ui/webapp"
# conf_static_home = "/home/vagrant/pa-2021/manage-billing-ui/reviewAutomatedBillingUI/webapp"
conf_static_home = "C:/Users/i035299/Documents/GitHub/patient-accounting-ui/automatedBillingManagementUI/webapp"

conf_port = 9090

conf_ui5_deployed = True

conf_destinations = {
    "/coophir": "https://fhir-core-svc-staging.cfapps.eu10.hana.ondemand.com/complex-test/fhir",
    "/meta": "https://fhir-meta-svc-staging.cfapps.eu10.hana.ondemand.com/complex-test/fhir",
    "/ExceptionAccount": "http://localhost:8082/FHIRApi/fhir/StructureDefinition/ExceptionAccount",
    "/ChargeItemView": "http://localhost:8082/FHIRApi/fhir/StructureDefinition/ChargeItemView"
}

scp_hks = [
    # "content-type",
    # "expires",
    # "pragma",
    # "strict-transport-security",
    # "cache-control",
    # "content-length",
    # "content-encoding",
    # "vary",
    # "transfer-encoding",
    # "x-content-type-options",
    # "x-xss-protection",
    # "x-vcap-request-id",
    # "x-frame-options",
    # "x-correlationid",
    # "connection",
    "date",
    "scp_hks_end"
]

token = ""


class AppServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True
    pass


class AppHTTPHandler(BaseHTTPRequestHandler):
    def finish(self):
        try:
            BaseHTTPRequestHandler.finish(self)
        except socket.error as e:
            # Broken pipe, connection reset by peer
            if ctypes.get_errno(e) not in BROKEN_SOCK:
                raise

    def handle_one_request(self):
        try:
            BaseHTTPRequestHandler.handle_one_request(self)
        except (ConnectionResetError, ConnectionAbortedError):
            pass

    def send_static_file(self):
        path = self.path.split('?')[0]
        file_content = None
        file_length = 0
        full_path = "%s%s" % (conf_static_home, path)
        try:
            with open(full_path, "rb") as fd:
                file_content = fd.read()
                file_length = os.stat(full_path).st_size
        except IOError:
            print('IOError in reading %s' % (path))
            self.send_error(404)
            return

        self.send_response(200)
        self.send_header('X-Frame-Options', 'SameOrigin')
        self.send_header('x-xss-protection', '1; mode=block')
        self.send_header('Content-Length', '%d' % file_length)
        # self.send_header('Content-Type', 'text/html')
        # if self.path.endswith('.json'):
        #     self.send_header('X-Content-Type-Options', 'nosniff')
        #     self.send_header('Content-Type', 'application/json')
        # elif self.path.endswith('.js'):
        #     self.send_header('X-Content-Type-Options', 'nosniff')
        #     self.send_header('Content-Type', 'application/javascript')
        self.end_headers()
        self.wfile.write(file_content)

    def dispatch(self, func):
        global token
        if token == "":
            token = fetch_client_token()
            if token == "":
                self.send_error(401)
                return

        headers = {}
        headers['Authorization'] = 'Bearer ' + token
        payload = None

        if self.headers['Content-Length'] != None:
            content_length = int(self.headers['Content-Length'])
            if content_length > 0:
                payload = self.rfile.read(content_length)
                headers['Content-Length'] = self.headers['Content-Length']
        if self.headers['Content-Type'] != None:
            headers['Content-Type'] = self.headers['Content-Type']

        headers['Accept-Encoding'] = ""
        headers['Connection'] = "close"

        print("Dispatched to: %s" % self.dispatch_path)

        app_response = func(
            self.dispatch_path,
            # stream = False,
            headers=headers,
            data=payload
        )

        self.send_response(app_response.status_code)
        for hk in app_response.headers.keys():
            if hk.lower() not in scp_hks:
                self.send_header(hk, app_response.headers[hk])
                # print("Header.%s: %s" % (hk, app_response.headers[hk]))
        self.end_headers()
        self.wfile.write(app_response.content)
        self.wfile.flush()

    def do_GET(self):
        # print("GET " + conf_app_uri + self.path)
        if self.path == "/token":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(to_bytes(token))
        elif self.need_delegating():
            self.dispatch(requests.get)
        else:
            self.send_static_file()

    def do_POST(self):
        # print("POST " + conf_app_uri + self.path)
        if self.need_delegating():
            self.dispatch(requests.post)
        else:
            self.send_error(404)

    def do_PUT(self):
        # print("PUT " + conf_app_uri + self.path)
        if self.need_delegating():
            self.dispatch(requests.put)
        else:
            self.send_error(404)

    def do_PATCH(self):
        # print("PATCH " + conf_app_uri + self.path)
        if self.need_delegating():
            self.dispatch(requests.patch)
        else:
            self.send_error(404)

    def do_DELETE(self):
        # print("DELETE " + conf_app_uri + self.path)
        global token
        if self.path == '/token':
            token = ""
            self.send_response(200)
            self.end_headers()
            self.wfile.write(to_bytes("Token deleted"))
            return
        elif self.need_delegating():
            self.dispatch(requests.delete)
        else:
            self.send_error(404)

    def need_delegating(self):
        dest = get_top_folder(self.path)
        if dest not in conf_destinations.keys():
            return False
        self.dispatch_path = conf_destinations[dest] + self.path[len(dest):]
        return True


def get_top_folder(path):
    segs = path.split("/")
    top = segs[0]
    if len(segs) >= 2:
        top = segs[1]
    top = "/" + top.split("?")[0]
    return top


def fetch_user_token():
    oauth_response = requests.post(
        conf_auth_url,
        data={'client_id': conf_client_id, 'client_secret': conf_client_secret,
              'username': conf_username, 'password': conf_password,
              'grant_type': 'password', 'response_type': 'user_token'
              })
    if oauth_response.status_code != 200:
        print('Gen token error: %d' % oauth_response.status_code)
        return ""
    token = oauth_response.json()['access_token']
    print('Gen token:\n%s' % token)
    return token


def fetch_client_token():
    oauth_response = requests.get(
        conf_auth_url + "?grant_type=client_credentials",
        auth=(conf_client_id, conf_client_secret))
    if oauth_response.status_code != 200:
        print('Gen token error: %d' % oauth_response.status_code)
        return ""
    token = oauth_response.json()['access_token']
    print('Gen token:\n%s' % token)
    return token


def to_bytes(txt):
    if _python_v3:
        return txt.encode("utf-8")
    return txt


def start_server():
    print('Server listening on port %d' % conf_port)
    http_server = AppServer(('', int(conf_port)), AppHTTPHandler)
    http_server.serve_forever()


def start_ui5_server():
    if not conf_ui5_deployed:
        return
    conf_destinations["/resources"] = "http://localhost:8080/resources"
    subprocess.Popen("npm run serve", shell=True, stdout=subprocess.PIPE,
                     # stderr = subprocess.PIPE
                     cwd=conf_static_home + "/..")


def main():
    start_ui5_server()
    start_server()


main()