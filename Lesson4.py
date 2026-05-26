import requests
import json
#Task 1 (Get API data): Create a function that sends a GET request to a simple API endpoint
# and returns the data
#(https://www.ndosiautomation.co.za/APIDEV/groups).

def api_request(url):
    response = requests.get(url)
    print(response.json())
api_request('https://www.ndosiautomation.co.za/APIDEV/groups')

#Task 2 (Save Data to a File): Create a function that takes
# the API response and saves it into a JSON file.


def api_file_data(url):
    json_response = requests.get(url)
    with open('data.json', 'w') as file:
        file.write(json_response.text)

api_file_data('https://www.ndosiautomation.co.za/APIDEV/groups')

#Task 3 (Read and Search Data): Create a function that reads the saved file,
# ask the user for a group name to search for,
# and checks whether that group exists in the data.
# If the group is not found, then display an error message.
# If the group is found, display a success message with the group Id.

import json

def search_group():
    with open('data.json', 'r') as file:
        response = json.load(file)

    groups = response["data"]

    group_name = input("Enter group name to search: ")

    found = False

    for group in groups:
        if group["Name"] == group_name:
            print(f"Success! Group found: {group['Name']}")
            print(f"Group ID: {group['Id']}")
            found = True
            break
    if not found:
        print("Error: Group not found")

# function call
search_group()