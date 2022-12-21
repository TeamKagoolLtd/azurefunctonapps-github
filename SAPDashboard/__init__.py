from kdp_functions import *

def main(req: func.HttpRequest, context) -> func.HttpResponse:
    try:
        sap = SAPDashboard(req, context)
        return func.HttpResponse(sap())
    except Exception as ex:
        return func.HttpResponse(f"Request received but failed to process! - Run ID: {context.invocation_id} - {repr(ex)}", status_code=400)
