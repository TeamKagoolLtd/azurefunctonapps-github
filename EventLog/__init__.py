from kdp_functions import *

def main(req: func.HttpRequest, context) -> func.HttpResponse:

    event_log = EventLog(req, context)
    event_log()

    return func.HttpResponse(f"Request received and processed successfully! - Run ID: {context.invocation_id}", status_code=200)
