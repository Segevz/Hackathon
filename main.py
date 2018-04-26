# -*- coding: utf-8 -*-
# !/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from os import curdir, sep
import cgi
from urlparse import urlparse, parse_qs
from JsonHandler import get_users_query, update_user, get_user, get_courses_for_school, get_all_schools, get_all_users
from Config import KEY_LIST


PORT_NUMBER = 80


# This class will handles any incoming request from
# the browser
class myHandler(BaseHTTPRequestHandler):
    # Handler for the GET requests
    def do_GET(self):
        if self.path[0] is not '/':
            self.send_error(404, 'Unvalid request: %s' % self.path)
        reply = False
        query_components = parse_qs(urlparse(self.path).query)
        for key in query_components.keys():
            if key.lower() not in KEY_LIST:
                self.send_error(404, 'Unvalid request: %s' % self.path)
                self.wfile.writelines([key, "    ",query_components.get(key)])
                self.wfile.write(self.path)
                return
        try:
            query_head = self.path.split('/')[1:-1]
            print query_head[0].lower()
            if len(query_components) is 0:
                if "users" in query_head:
                    results = get_all_users()
                    reply = True
                elif "schools" in query_head:
                    results = get_all_schools()
                    reply = True
            elif "users" in query_head:
                results = get_users_query(query_components)
                reply = True
            elif "update" in query_head:
                results = update_user(query_components)
                reply = True
            elif "profile" in query_head:
                results = get_user(query_components["id"][0])
                reply = True
            elif "courses" in query_head:
                results = get_courses_for_school(query_components["school"])
                reply = True
            elif "schools" in query_head:
                results = get_all_schools()
                reply = True
        except Exception as e:
            self.send_error(404, 'Unvalid request: %s' % self.path)
            return

        if reply:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(results)
        else:
            self.send_error(404, 'Unvalid request: %s' % self.path)

try:
    # Create a web server and define the handler to manage the
    # incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print 'Started httpserver on port ', PORT_NUMBER

    # Wait forever for incoming http requests
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()
