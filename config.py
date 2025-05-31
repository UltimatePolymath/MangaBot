env_vars = {
  # Get From my.telegram.org
  "API_HASH": "8f80142dfef1a696bee7f6ab4f6ece34",
  # Get From my.telegram.org
  "API_ID": "28213805",
  #Get For @BotFather
  "BOT_TOKEN": "7630269993:AAGIjOM9N3U9LkVB-u61aKZA072mtkfCN28",
  # Get For tembo.io
  "DATABASE_URL_PRIMARY": "",
  # Logs Channel Username Without @
  "CACHE_CHANNEL": "drunkCache0",
  # Force Subs Channel username without @
  "CHANNEL": "drunkCache0",
  # {chap_num}: Chapter Number
  # {chap_name} : Manga Name
  # Ex : Chapter {chap_num} {chap_name} @Manhwa_Arena
  "FNAME": "",
  # Put Thumb Link 
  "THUMB": ""
}

dbname = env_vars.get('DATABASE_URL_PRIMARY') or env_vars.get('DATABASE_URL') or 'sqlite:///test.db'

if dbname.startswith('postgres://'):
    dbname = dbname.replace('postgres://', 'postgresql://', 1)
    
