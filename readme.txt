Fastly Configuration Export Tool

This python script exports Fastly VCL configurations and outputs them into Terraform. If there are also compute configurations in use at Fastly, then it would be best to discuss that configuration in a discovery call. 

You will need to have Go and Python installed. 
You can install Go here: https://go.dev/doc/install. 
Python here: https://docs.brew.sh/Homebrew-and-Python

This script is a wrapper for the binary: https://github.com/hrmsk66/terraformify and  recommended by Fastly support. It is a third party public tool and not supported by Fastly.
 
The tool requires read permissions to access your Fastly resource and you'll be prompted to add your Fastly API key and service id. 
You can create API tokens here: https://manage.fastly.com/account/tokens

You'll find the service "ID" on the Service Configuration page in your Fastly console. You'll find it next to the name of your service. 

To use, navigate to the fastly-export folder and run: $ python fe.py

Please select "Y" when prompted to download.

The export files will appear in the fastly-export folder. Please compress this folder and copy it your google drive folder (ensure permissions are set to "anyone with link") and send us a link via 
email.

Feel free to reach out with any questions. 
