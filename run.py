"""
Скрипт запуска бота и веб-сервера одновременно.
"""

import asyncio
import multiprocessing
import os
import sys


def run_web():
    """Запуск Flask-сервера."""
    from web import app

    port = int(os.getenv("WEB_PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=False)


def run_bot():
    """Запуск Telegram-бота."""
    from bot import main

    asyncio.run(main())


if __name__ == "__main__":
    web_process = multiprocessing.Process(target=run_web)
    web_process.start()

    try:
        run_bot()
    except KeyboardInterrupt:
        print("Остановка...")
    finally:
        web_process.terminate()
        web_process.join()
