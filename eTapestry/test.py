import zeep
import os

databaseId = os.environ['ETAPESTRY_DATABASE_ID']
apiKey = os.environ['ETAPESTRY_API_KEY']

client = zeep.Client(wsdl='https://sna.etapestry.com/v3messaging/service?WSDL')
print(client.service.apiKeyLogin(databaseId, apiKey))