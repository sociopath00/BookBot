import requests
import json

res = requests.post("http://localhost:5005/webhooks/rest/webhook",
                    data=json.dumps({"sender": "user1", "message": "tell me books written by shashi tharoor"}))


print(res.text)