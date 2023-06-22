import os

# Prompt the user to add their API key
api_key = input("Enter your API key: ")
os.environ["FASTLY_API_KEY"] = api_key

# Prompt the user for service ID
serv_id = input("Enter the service ID: ")

# Get the current working directory and remove the last directory
current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)

command = f"{parent_dir}/terraformify service vcl {serv_id}"
print(command)
os.system(command)

