class CORSMiddleware:

    def process_response(self, request, response, resource):
        response.append_header('Access-Control-Allow-Origin', '*')
        response.append_header('Access-Control-Allow-Headers', 'Content-Type')
        response.append_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
