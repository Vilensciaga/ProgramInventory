from playwright.sync_api import sync_playwright
from Models.InstitutionData import InstitutionData 

url = "https://prod.flbog.net:4445/pls/apex/f?p=136:2:15603079343155:::::"


def getFile():
   with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)  # Use headless mode for Azure
    page = browser.new_page()
    page.goto(url)
    print(page.title())

    # Wait for the download and intercept it
    with page.expect_download() as download_info:
        page.click("div.t-Report-links a:first-of-type")

    # Get the downloaded file
    download = download_info.value
    print(f"Downloading: {download.suggested_filename}")

    # Save the file to a specific location
    download.save_as(f"downloads/{download.suggested_filename}")
    browser.close() 



def readFile(path):
    institutionData = []

    with open(path, 'r') as file:
        next(file)
        for line in file:
            data = line.strip().split(',')
            Institution = data[0] if data[0] else "Unknown"
            DegreeLevel = data[1] if data[1] else "Unknown" 
            CIP = data[2] if data[2] else "Unknown" 
            PSE = data[3] if data[3] else "Unknown" 
            SpecializedAdmissions = data[4] if data[4] else "Unknown"
            CreditHours = data[5] if data[5] else "Unknown" 
            Implemented = data[6] if data[6] else "Unknown" 
            Suspended = data[7] if data[7] else "Unknown" 
            Terminated = data[8] if data[8] else "Unknown"

            if(Institution == 'UNF'):
                currentData = InstitutionData(Institution, DegreeLevel, CIP, PSE, SpecializedAdmissions, CreditHours, Implemented, Suspended, Terminated)
                institutionData.append(currentData)

    return institutionData