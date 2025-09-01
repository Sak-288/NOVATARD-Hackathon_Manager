# Importing OS (to retrieve env variables) && pyairtable (a community-built python library to use the Airtable API)
import os
from pyairtable import Api

# Getting necessary info from the API
api = Api(os.environ['AIRTABLE_TEST_API_KEY'])
BASE_ID = "app5RiAfXsKWSZ67p"
TABLE_ID = "tblt7GgXQ6gCYCV2l"

# Declaring the Participants Spreadsheet
daydream_table = api.table(BASE_ID, TABLE_ID)