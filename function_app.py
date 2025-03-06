import azure.functions as func
import logging
import scrapeFile as scf


app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


@app.route(route="ProgramInventory")
def ProgramInventory(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    scf.getFile()
    data = scf.readFile('downloads/search_results.csv')



    
    if not data:
        return func.HttpResponse("No file detected.",
            status_code=500
    )
    else:
        return func.HttpResponse(
            f"{data}",
             status_code=200
        )

        # "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response."