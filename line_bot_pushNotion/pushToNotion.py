import requests
from requests.exceptions import RequestException, ConnectionError, HTTPError, Timeout
import os
from dotenv import load_dotenv

def pushToNotion(message):
    url = "https://api.notion.com/v1/pages"
    API_KEY = os.environ['API_KEY_NOTION']
    database_id = os.environ['database_id']

    payload = {
        "parent": {"database_id": database_id},
        "properties": {
            "Name":{
                "title":[
                    {
                        "text":{
                            "content" : message
                        }
                    }
                ]
            }
        },
        "children": [
            {
                "object" : "block",
                "type"  : "paragraph",
                "paragraph":{
                    "rich_text":[
                        {
                            "text" :{
                                "content":"これはテストです"
                            }
                        }
                    ]
                }
            }
        ]
        
    }

    headers = {
        "Accept": "application/json",
        "Notion-Version": "2022-02-22",
        "Content-Type": "application/json",
        "Authorization": "Bearer " + API_KEY
    }


    try:
        response = requests.request("POST", url, json=payload, headers=headers)
        print(response.text)
        return "success"
    except ConnectionError as CE:
        print("Connection Error:", CE)
    except HTTPError as HE:
        print("HTTP Error:",HE)
    except Timeout as TO:
        print("Timeout Error:", TO)
    except RequestException as RE:
        print("Error:", RE)
