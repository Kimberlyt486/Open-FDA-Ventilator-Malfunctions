import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

def get_data():
    api_key = os.getenv('api_key')
    base_url = "https://api.fda.gov/device/event.json"
    search_query = 'device.generic_name:%22ventilator%22+AND+event_type:%22Malfunction%22'
    url = f"{base_url}?api_key={api_key}&search={search_query}&limit=1000"
   
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        
        df = pd.json_normalize(data['results'])
        return df
    else:
        return None

df_vents = get_data()

# if df_vents is not None:
    
# else:
#     print("Failed to retrieve data.")