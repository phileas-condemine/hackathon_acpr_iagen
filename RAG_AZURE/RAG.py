import os
import openai
import dotenv
import ipdb

dotenv.load_dotenv()

os.environ["AOAIKey"] = "OPENAI_API_KEY"
os.environ["AOAIEndpoint"] = "https://francecentral-openai.openai.azure.com"
os.environ["AOAIDeploymentId"] = "gpt-35-turbo"

os.environ["SearchEndpoint"] = "https://ai-search-acpr-hackathon.search.windows.net"
os.environ["SearchKey"] = "SEARCH_API_KEY"
os.environ['SearchIndex'] = "YOURINDEXNAME"

endpoint = os.environ.get("AOAIEndpoint")
api_key = os.environ.get("AOAIKey")
deployment = os.environ.get("AOAIDeploymentId")

client = openai.AzureOpenAI(
    base_url=f"{endpoint}/openai/deployments/{deployment}/extensions",
    api_key=api_key,
    api_version="2023-08-01-preview"
)

#ipdb.set_trace()

completion = client.chat.completions.create(
    model=deployment,
    messages=[
        {
            "role": "user",
            "content": "resume moi les recommandations de Tracfin",
        },
    ],
    extra_body={
        "dataSources": [
            {
                "type": "AzureCognitiveSearch",
                "parameters": {
                    "endpoint": os.environ["SearchEndpoint"],
                    "key": os.environ["SearchKey"],
                    "indexName": os.environ["SearchIndex"],
                    "semanticConfiguration": "default",
                    "queryType": "vectorSemanticHybrid",
                    "fieldsMapping": {},
                    "inScope": True,
                    "roleInformation": "You are an AI assistant that helps people find information.",
                    "strictness": 3,
                    "topNDocuments": 5,
                    "embeddingDeploymentName": "ada-002"
                }
            }
        ]
    }
)

print(completion.model_dump_json(indent=2))