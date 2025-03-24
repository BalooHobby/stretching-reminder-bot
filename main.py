import logging
import random
import asyncio
from datetime import datetime, time, timedelta
from telegram import Bot

TOKEN = "7381747261:AAH01BrS_afRqk8K3clxMuL5__Cc9IqAR0w"
CHAT_ID = "<raskorhubbot>"

bot = Bot(token=TOKEN)

motivations = [
    "Твоє тіло — твоя зброя. Не ігноруй його.",
    "15 хвилин — і ти став гнучкішим за більшість. Вперед!",
    "Не важко — вийти. Важко — не вийти. Рухайся.",
    "Зроби це для себе, не для дисципліни, а з любові.",
    "Ти вже воїн. Ставай ще й мудрим тілом.",
    "Розтяжка — як медитація в русі. Тобі це потрібно.",
    "Нехай ці 15 хвилин стануть твоїм вечірнім ритуалом сили."
]

async def send_motivation():
    while True:
        now = datetime.now()
        target_time = datetime.combine(now.date(), time(20, 0))
        if now > target_time:
            target_time += timedelta(days=1)
        wait_seconds = (target_time - now).total_seconds()
        await asyncio.sleep(wait_seconds)
        
        motivation = random.choice(motivations)
        try:
            await bot.send_message(chat_id=CHAT_ID, text=f"🧘‍♂️ Час на розтяжку!\n\n{motivation}")
            logging.info("Message sent.")
        except Exception as e:
            logging.error(f"Error sending message: {e}")
        await asyncio.sleep(60)  # затримка, щоб не повторити одразу

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(send_motivation())
