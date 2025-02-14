import os

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from gcp_config import TOPIC, GMAIL


SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
SERVICE_ACCOUNT_FILE = os.path.abspath('credentials.json')

def get_gmail_event():
    flow = InstalledAppFlow.from_client_secrets_file(
        SERVICE_ACCOUNT_FILE, SCOPES
    )
    credentials = flow.run_local_server(port=0)

    service = build('gmail', 'v1', credentials=credentials)

    request = {
        "topicName": "projects/affable-doodad-450908-f0/topics/email",
        "labelIds": ["INBOX"],
        "labelFilterAction": "include"
    }

    return service.users().watch(userId="me", body=request).execute()
    
