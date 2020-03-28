import requests
import json

res = requests.post("http://localhost:6000/chatbot",
                    data=json.dumps({"sender": "user1", "message": "tell me books written by shashi tharoor"}))


print(res.text)