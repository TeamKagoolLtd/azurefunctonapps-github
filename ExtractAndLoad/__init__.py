from kdp_functions import *

def main(req: func.HttpRequest, context) -> func.HttpResponse:
    try:
        extract_and_load = ExtractAndLoad(req, context)
        extract_and_load()

    except Exception as ex:
        return func.HttpResponse(f"Request received and processed successfully! - Run ID: {context.invocation_id} - {repr(ex)}", status_code=400)
    
    return func.HttpResponse(f"Request received and processed successfully! - Run ID: {context.invocation_id}", status_code=200)