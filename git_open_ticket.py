#!/usr/bin/env python3
import subprocess
import re
from os.path import join, dirname
import os
import sys
from dotenv import load_dotenv


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


def print_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print("Exception - {}".format(e))
            sys.exit(1)
    return wrapper


@print_error
def fetch_branch_name():
    branch_name = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], stdout=subprocess.PIPE).stdout
    if branch_name:
        return str(branch_name.rstrip(), 'utf-8')
    return ""


@print_error
def extract_ticket_number(branch_name):
    matches = re.findall('((?:GB|gb)-\\d{4})', branch_name)
    if matches:
        return matches[0]
    else:
        return ""


if __name__ == '__main__':
    ticket_number = extract_ticket_number(fetch_branch_name())
    if ticket_number:
        subprocess.run(["python3", "-m", "webbrowser", "-t", "%s/browse/%s"%(os.getenv('JIRA_URL'), ticket_number)])
    else:
        print("Are you sure this is a JIRA related branch?")



