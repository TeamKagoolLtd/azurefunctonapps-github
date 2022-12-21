from kdp_functions import *

def main(req: func.HttpRequest, context) -> func.HttpResponse:

    get_mdata = GetMData(req, context)
    return get_mdata()
