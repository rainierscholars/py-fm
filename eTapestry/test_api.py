# Tests connection to eTapestry API

import zeep
import os

databaseId = os.environ['ETAPESTRY_DATABASE_ID']
apiKey = os.environ['ETAPESTRY_API_KEY']

client = zeep.Client(wsdl='https://sna.etapestry.com/v3messaging/service?WSDL')

# apiKeyLogin may return a URL or an empty string. If successful no error should be printed. 
# See https://www.blackbaudhq.com/files/etapestry/api3/methods/apiKeyLogin.html for more information.
print(client.service.apiKeyLogin(databaseId, apiKey))