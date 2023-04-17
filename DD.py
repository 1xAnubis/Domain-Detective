import requests
import argparse
import sys
import os.path
from tqdm import tqdm
from termcolor import colored
import pyfiglet


def validate_domain_name(domain_name):
    if ' ' in domain_name or not domain_name:
        return False
    return True

def check_status_code(domain):
    try:
        response = requests.get(f"https://{domain}")
        if response.ok:
            status_color = "green"
        else:
            status_color = "yellow"
        print(colored(f"{domain} -- Status code : {response.status_code}", status_color))
    except requests.exceptions.RequestException as e:
        print(colored(f"{domain} -- Error: {e}", "red"))
        print(colored("Please check the domain name and try again.", "red"))


def check_multiple_domains(file_path, output_path=None):
    try:
        with open(file_path, 'r') as f:
            domains = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(colored(f"Error: Could not find the file '{file_path}'", "red"))
        return
    for domain in tqdm(domains, desc="Checking domains"):
        try:
            response = requests.get(f"https://{domain}")
            if response.ok:
                status_color = "green"
            else:
                status_color = "yellow"
            status_msg = colored(f"{domain} -- Status code : {response.status_code}", status_color)
            if output_path:
                print(status_msg, file=open(output_path, 'a'))
            else:
                print(status_msg)
        except requests.exceptions.RequestException as e:
            error_msg = colored(f"{domain} -- Error: {e}", "red")
            if output_path:
                print(error_msg, file=open(output_path, 'a'))
            else:
                print(error_msg)
            print(colored("Please check the domain name and try again.", "red"))
    sys.exit()


def main():
    welcome = pyfiglet.figlet_format("Domain Detective")
    print(colored(welcome, "green"))

    parser = argparse.ArgumentParser(description="Domain Detective: A tool for checking the HTTP status codes of domains")
    parser.add_argument("--domain", help="Domain name to check")
    parser.add_argument("--file", help="Path to file with domains")
    parser.add_argument("--output", help="Custom output file path")
    args = parser.parse_args()

    if not args.domain and not args.file:
        print(colored("Please provide either a domain or a file with domains to check.", "red"))
        sys.exit()

    if args.domain:
        if not validate_domain_name(args.domain):
            print(colored("Invalid domain name, please try again.", "red"))
            sys.exit()
        check_status_code(args.domain)

    if args.file:
        if not os.path.isfile(args.file):
            print(colored("Invalid file path, please try again.", "red"))
            sys.exit()

        if args.output:
            output_file = open(args.output, "w")
            sys.stdout = output_file

        check_multiple_domains(args.file, args.output)

        if args.output:
            output_file.close()


if __name__ == '__main__':
    main()
