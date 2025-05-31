import asyncio as aio
from threading import Thread
from flask import Flask
from bot import *

# Flask App Setup
app = Flask(__name__)

@app.route('/')
def health_check():
    return "Manga Bot is running", 200

async def async_main():
    db = DB()
    await db.connect()

def run_flask():
    app.run(host='0.0.0.0', port=7860, use_reloader=False)

if __name__ == '__main__':
    # Start Flask in a daemon thread (for health checks/API)
    flask_thread = Thread(target=run_flask, daemon=True)
    flask_thread.start()

    # Main async loop
    loop = aio.get_event_loop_policy().get_event_loop()
    loop.run_until_complete(async_main())
    
    # Background tasks
    loop.create_task(manga_updater())
    for i in range(100):  # 100 chapter workers
        loop.create_task(chapter_creation(i + 1))
    
    bot.run()
