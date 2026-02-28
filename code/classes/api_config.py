class APIConfig:
    def __init__(self,api_key,model="mistral-large-2512",max_tokens="256000"):
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens
        self.base_url = "https://api.mistral.ai/v1"

# Check Different Configurations
small_config = APIConfig(api_key="small_api_key",model="mistral-small-2506",max_tokens="128000")

medium_config = APIConfig(api_key="medium_api_key",model="mistral-medium-2508",max_tokens="128000")

large_config = APIConfig(api_key="large_api_key")

#Accessing the configuration

print("---Small Model----")
print(small_config.api_key)
print(small_config.model)
print(small_config.max_tokens)
print(small_config.base_url)

print("\n ---Medium Model----")
print(medium_config.api_key)
print(medium_config.model)
print(medium_config.max_tokens)
print(medium_config.base_url)

print("\n ---Large Model----")
print(large_config.api_key)
print(large_config.model)
print(large_config.max_tokens)
print(large_config.base_url)

print("\n after changing the large model info..")
large_config.model = "ministral-8b-2512"
print(large_config.model)



