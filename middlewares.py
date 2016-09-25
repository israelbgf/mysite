class CORSMiddleware:

    def process_response(self, request, response, resource):
        response.append_header('Access-Control-Allow-Origin', '*')
