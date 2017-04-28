import requests
import json
import click


class Application:
    def __init__(self, applicationId, applicationName, applicationDescription, applicationCreatedDate, businessCriticalityTypeId, emailList, applicationTypeId, applicationType, attributes):
        self.applicationId = applicationId
        self.applicationName = applicationName
        self.applicationDescription = applicationDescription
        self.applicationCreatedDate = applicationCreatedDate
        self.businessCriticalityTypeId = businessCriticalityTypeId
        self.emailList = emailList
        self.applicationTypeId = applicationTypeId
        self.applicationType = applicationType
        self.attributes = attributes


secret = "fTRPbXN0Sv'b4j)9NxmcoYj3a8ZW/x"
apiKey = "acdd0eb9-076f-4938-8377-72087ed54c65"
token_url = "https://www.hpfod.com/oauth/token/"


def getToken():
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    params = {"grant_type": "client_credentials", "scope": "https://hpfod.com/tenant",
              "client_id": apiKey, "client_secret": secret}

    r = requests.post(token_url, headers=headers, data=params)
    # json.loads turns the json response into a dictionary
    data = json.loads(r.text)
    return data['access_token']


def listApplications():
    headerValue = "Bearer " + getToken()
    listapp_url = "https://api.hpfod.com/api/v3/applications/"
    headers = {"Content-Type": "application/x-www-form-urlencoded",
               "Authorization": headerValue}
    params = {"fields": "applicationID,applicationName"}

    r = requests.get(listapp_url, headers=headers, data=params)
    data = json.loads(r.text)
    results = []
    for item in data['items']:
        app = Application(item['applicationId'], item['applicationName'], item['applicationDescription'], item['applicationCreatedDate'], item['businessCriticalityTypeId'], item['emailList'], item['applicationTypeId'], item['applicationType'], item['attributes'])
        results.append(app)
    return results
