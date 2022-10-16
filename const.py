TOKEN = '5714857134:AAEZPyFYcRsilmtk7DJKi7vSAXb3WpAXb9A'

URL = 'https://api.telegram.org/bot{token}/{method}'

UPDATE_METH = 'getUpdates'
SEND_METH = 'sendMessage'

MY_ID = 796802141

UPDATE_ID_FILE_PATH = 'update_id'

with open(UPDATE_ID_FILE_PATH) as file:
    data = file.readline()
    if data:
        data = int(data)
    UPDATE_ID = data


WEATHER_TOKEN = '944eaddf8469431995de036d11d5f102'

WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={token}&units=metric&lang=ua'
