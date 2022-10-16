TOKEN = ''

URL = ''

UPDATE_METH = 'getUpdates'
SEND_METH = 'sendMessage'

MY_ID =

UPDATE_ID_FILE_PATH = 'update_id'

with open(UPDATE_ID_FILE_PATH) as file:
    data = file.readline()
    if data:
        data = int(data)
    UPDATE_ID = data


WEATHER_TOKEN = ''

WEATHER_URL = ''
