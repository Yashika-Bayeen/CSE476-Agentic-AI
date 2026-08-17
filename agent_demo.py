import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

load_dotenv()

# Extract base resource URL from PROJECT_ENDPOINT
# e.g. https://yashikabayeen2024-1022-resource.services.ai.azure.com
project_endpoint = os.getenv("PROJECT_ENDPOINT", "")
base_endpoint = project_endpoint.split("/api/projects")[0]

model = os.getenv("MODEL_DEPLOYMENT_NAME", "gpt-chat-latest")

print(f"Endpoint : {base_endpoint}")
print(f"Model    : {model}")
print()

# Use DefaultAzureCredential (az login) — no API key required
token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default",
)

client = AzureOpenAI(
    azure_endpoint=base_endpoint,
    azure_ad_token_provider=token_provider,
    api_version="2024-10-21",
)

response = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "system", "content": "You are a friendly teaching assistant. Explain answers simply."},
        {"role": "user",   "content": "Describe a line with slope 2 and y-intercept 5. Give the equation and explain what it means."},
    ],
)

print("Assistant:", response.choices[0].message.content)