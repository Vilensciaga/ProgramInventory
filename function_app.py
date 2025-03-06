import azure.functions as func
import logging
import scrapeFile as scf


app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


@app.route(route="ProgramInventory")
def ProgramInventory(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    scf.getFile()
    data = scf.readFile('downloads/search_results.csv')



    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
            f"{data[0]}",
             status_code=200
        )

        # "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response."