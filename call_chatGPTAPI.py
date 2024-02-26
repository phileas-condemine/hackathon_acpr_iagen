import os
from openai import AzureOpenAI

# Ne pas toucher aux deux lignes suivantes.
os.environ["AZURE_OPENAI_KEY"] = "OPENAI_API_KEY"
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://francecentral-openai.openai.azure.com"

# Le modèle à utiliser pour vos requêtes. Modèle recommandé : "gpt-35-turbo". Autres modèles disponibles : "gpt-35-turbo-16k", "gpt-4", "gpt-4-32k".
# Ces modèles alternatifs ne sont à utiliser que de façon parcimonieuse.
os.environ["AZURE_OPENAI_DeploymentId"] = "gpt-35-turbo"
client = AzureOpenAI(
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
  api_key=os.getenv("AZURE_OPENAI_KEY"),  
  api_version="2023-05-15"
)

response = client.chat.completions.create(
    model=os.getenv("AZURE_OPENAI_DeploymentId"), # model = "deployment_name".
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
        {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
        {"role": "user", "content": "Do other Azure AI services support this too?"}
    ]
)

print(response.choices[0].message.content)
