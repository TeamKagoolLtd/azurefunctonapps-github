from kdp_functions import *

def main(req: func.HttpRequest, context) -> func.HttpResponse:
    
    try:
        completion_call = CompletionCall(req, context)
        completion_call()

        return func.HttpResponse(f"Request received - Run ID {context.invocation_id}", status_code = 200)

    except Exception as ex:
        return func.HttpResponse(f"Request received - Run ID {context.invocation_id} - but failed with error: {repr(ex)}", status_code = 400)
