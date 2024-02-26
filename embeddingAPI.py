import os
from openai import AzureOpenAI

# Ne pas toucher aux deux lignes suivantes
os.environ["AZURE_OPENAI_KEY"] = "OPENAI_API_KEY"
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://francecentral-openai.openai.azure.com"

# Le modèle d'embedding à utiliser tel que déployé sur Azure
os.environ["AZURE_OPENAI_DeploymentId"] = "ada-002" #"text-embedding-ada-002"
client = AzureOpenAI(
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
  api_key=os.getenv("AZURE_OPENAI_KEY"),  
  api_version="2023-05-15"
)

response = client.embeddings.create(
    model=os.getenv("AZURE_OPENAI_DeploymentId"), # model = "deployment_name".
    input="Your text string goes here"
)

print(response.data[0].embedding)
