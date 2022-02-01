import os
# Table Name
TABLE_PATTERN = "pattern"

# Fetch the service account key JSON file contents
CRED_FIREBAE = 'firebase-adminsdk.json'
# Initialize the app with a service account, granting admin privileges
DATABASE_URL = os.getenv('DATABASE_URL')
