import json
from http.server import HTTPServer,BaseHTTPRequestHandler
from backend.parser.sql_parser import parse_sql

class LuxRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/schema":

            with open("data/test.sql","r") as file:
                sql_text = file.read()

            schema = parse_sql(sql_text)
            respomse_json = json.dumps(schema)

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            self.wfile.write(respomse_json.encode("utf-8"))

        else:
            self.send_response(404)
            self.end_headers()

def run_server(port=8000):
    server = HTTPServer(("localhost",port), LuxRequestHandler)
    print(f"Server live at http://localhost:{port}/api/schema")
    server.serve_forever()

if __name__ == "__main__":
    run_server()