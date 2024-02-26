import os
import openai
import dotenv
import ipdb

os.environ["AOAIKey"] = "OPENAI_API_KEY_VISION"
os.environ["AOAIEndpoint"] = "https://gptshared-vision.openai.azure.com/"
os.environ["AOAIDeploymentId"] = "gpt-4-vision"


endpoint = os.environ.get("AOAIEndpoint")
api_key = os.environ.get("AOAIKey")
deployment = os.environ.get("AOAIDeploymentId")

client = openai.AzureOpenAI(
    base_url=f"{endpoint}/openai/deployments/{deployment}/extensions",
    api_key=api_key,
    api_version="2023-12-01-preview"
)


response = client.chat.completions.create(
    model=deployment,
    messages=[
        { "role": "system", "content": "You are a helpful assistant." },
        { "role": "user", "content": [  
            { 
                "type": "text", 
                "text": "Describe this picture:" 
            },
            { 
                "type": "image_url",
                "image_url": {
                    "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
                }
            }
        ]}
    ],
    max_tokens=2000 
)

print(response)
print(response.choices[0].message.content)