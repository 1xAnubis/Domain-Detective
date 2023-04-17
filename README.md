# Domain-Detective
Domain Detective is a command-line tool that allows you to check the HTTP status code of a single domain or multiple domains. It uses the Python requests library to send HTTP requests to domains, and the tqdm library to display a progress bar for the checking process.

### The tool can be used in two ways:

- By providing a single domain name as a command-line argument using the "--domain" option. In this case, the tool will check the status code of the provided domain and display the result in the terminal.
- By providing a file path containing a list of domain names to be checked using the "--file" option. In this case, the tool will read the list of domains from the file and check the status code for each domain. If the "--output" option is specified, the tool will save the results to a file at the specified path.

 ----
## Install requirements 
    pip install -r requirements.txt
 ----
 
 ----
## Usage 
    $ python DD.py --domain google.com

    $ python DD.py --file <file_path> --output <output_file

    $ python DD.py --help
 ----
## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mhmmdashraf/)

