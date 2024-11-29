import requests
import json

github_repo = "https://github.com/aashnadogra/DPS_AI_deploy"
email = "aashna.x.dogra@gmail.com"
deployed_endpoint = "https://dps-310184006355.asia-south1.run.app"
notes = "Thankyou for this opportunity! I learnt so much about deployment with this challenge and am learning so much more, it was so much fun! I really hope to be a part of DPS and work on more interesting problems and solutions and learn more and more from the beautiful community there :) "  # This is optional

payload = {
    "github": github_repo,
    "email": email,
    "url": deployed_endpoint,
    "notes": notes
}

headers = {
    "Content-Type": "application/json"
}

# POST request
url = "https://dps-challenge.netlify.app/.netlify/functions/api/challenge"
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Check if the request was successful
if response.status_code == 200:
    print("Congratulations! Achieved Mission 3")
else:
    print("Failed to complete Mission 3. Status code:", response.status_code)