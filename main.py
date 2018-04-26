# -*- coding: utf-8 -*-
# !/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from os import curdir, sep
import cgi
from urlparse import urlparse, parse_qs
from JsonHandler import get_users_query, update_user, get_user, get_courses_for_school, get_all_schools
from Config import KEY_LIST


PORT_NUMBER = 80


# This class will handles any incoming request from
# the browser
class myHandler(BaseHTTPRequestHandler):
    # Handler for the GET requests
    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        for key in query_components.keys():
            if key.lower() not in KEY_LIST:
                self.send_error(404, 'Unvalid request: %s' % self.path)
                # self.wfile.writelines([key, "    ",query_components.get(key)])
                # self.wfile.write(self.path)
                return
        try:
            query_head = self.path.split('/')[1:-1]
            if query_head[0].lower() is "users":
                results = get_users_query(query_components)
            elif query_head[0].lower() is "update":
                results = update_user(query_components)
            elif query_head[0].lower() is "profile":
                results = get_user(query_components["id"])
            elif query_head[0].lower() is "courses":
                results = get_courses_for_school(query_components["school"])
            elif query_head[0].lower() is "schools":
                results = get_all_schools()
        except Exception as e:
            self.send_error(404, 'Unvalid request: %s' % self.path)
            return


        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(results)


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
