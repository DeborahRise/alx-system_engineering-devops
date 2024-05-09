#!/usr/bin/python3

import requests

# Set up your Datadog API credentials
api_key = 'dbc811071720dbeea47bc3aedebf1e5d'
app_key = '55dffcb7584574176ad4fff51ec23068e4fc5eb2'

# Make the API request to list dashboards
url = 'https://api.datadoghq.com/api/v1/dashboard'
headers = {'DD-API-KEY': api_key, 'DD-APPLICATION-KEY': app_key}
response = requests.get(url, headers=headers)

# Parse the response to find the dashboard ID
dashboards = response.json()['dashboards']
for dashboard in dashboards:
    print(f"Dashboard Name: {dashboard['title']}, ID: {dashboard['id']}")
