import azure.functions as func
import logging
import scrapeFile as scf
import json


app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


@app.route(route="ProgramInventory")
def ProgramInventory(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    scf.getFile()
    data = scf.readFile('downloads/search_results.csv')
    #print("\n".join(str(d) for d in data))
    json_output = json.dumps(data, default=lambda x: x.__dict__, indent=4)
    #print(json_output)
    
    if not data:
        return func.HttpResponse("No file detected.",
            status_code=500
    )
    else:
        return func.HttpResponse(
            f"{json_output}",
             status_code=200

        )
