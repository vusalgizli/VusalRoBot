import time
from typing import List

from telegram import Update
from telegram.ext import run_async, CallbackContext

from SiestaRobot import dispatcher
from SiestaRobot.modules.disable import DisableAbleCommandHandler
from SiestaRobot.modules.helper_funcs.chat_status import user_admin




        await brend.edit("`Sana neden inanayım?! 🧐`")

        time.sleep(0.9)

        await brend.edit("`Yalan mı doğru mu öğrenelim`")
        time.sleep(1)
        await brend.edit("`Araştırılıyor...🔎`")
        time.sleep(0.5)
        await brend.edit("`Yalan🤥`")
        time.sleep(0.1)
        await brend.edit("`Doğru👍`")
        time.sleep(0.1)
        await brend.edit("`Yalan🤥`")
        time.sleep(0.1)
        await brend.edit("`Doğru👍`")
        time.sleep(0.1)
        await brend.edit("`Yalan🤥`")
        time.sleep(0.1)
        await brend.edit("`Doğru👍`")
        time.sleep(0.1)
        await brend.edit("`Yalan🤥`")
        time.sleep(0.1)
        await brend.edit("`Doğru👍`")
        time.sleep(0.4)
        await brend.edit(f'`{random.choice(["Yalan söylüyorsun❌", "Doğru söylüyorsun✅"])}\n\n%{random.randint(0, 100)}`')
        time.sleep(0.9)