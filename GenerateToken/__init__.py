from kdp_functions import *

def main(req: func.HttpRequest, context) -> func.HttpResponse:

    generate_token = GenerateToken(req, context)
    return generate_token()