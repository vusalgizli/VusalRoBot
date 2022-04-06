import asyncio
import random
from SiestaRobot.events import register
from SiestaRobot import bot
import os
from SiestaRobot.cmdhelp import CmdHelp

@register(pattern="^/olc ?(.*)", outgoing=True)
async def sevgi(event):
    me = await bot.get_me()
    await event.edit(f'`{random.choice(["❤️", "🧡," "💛", "💚", "💙", "💜", "🖤"])} Eşq faizi hesablanır...`')

    if event.is_reply:
        reply = await event.get_reply_message()
        reply_user = await event.client.get_entity(reply.from_id)
        text = event.pattern_match.group(1)

        if text == '':
            firstUser_id = me.id
            if me.username:
                firstUser = f'@{me.username}'
            else:
                firstUser = f'[{me.first_name}](tg://user?id={me.id})'
        else:
            if '?id' in text:
                firstUser_id = text.split('?id=')[1]
            else:
                firstUser_id = text
            firstUser = text

        if reply_user.username:
            secondUser_id = reply_user.id
            secondUser = f'@{reply_user.username}'
        else:
            secondUser_id = reply_user.id
            secondUser = f'[{reply_user.first_name}](tg://user?id={reply_user.id})'
    else:
        return await event.edit('`Zəhmət olmasa bir istifadəçiyə cavab verin`')

    for i in range(0,10):
        await event.edit(f'`{random.choice(["❤️", "🧡" "💛", "💚", "💙", "💜", "🖤"])} Eşq faizi hesablanır... %{random.randint(0, 100)}`')
        await asyncio.sleep(0.3)
        
    if os.path.exists(f'{firstUser_id}-{secondUser_id}.txt'):
        yuzde = open(f'{firstUser_id}-{secondUser_id}.txt', 'r').read()
        await event.edit(f'{firstUser} `ile` {secondUser} `arasındaki sevgi hesablandı!`\n**Nəticə:** `%{yuzde}`')
    else:
        yuzde = random.randint(0, 100)
        open(f'{firstUser_id}-{secondUser_id}.txt', 'a+').write(str(yuzde))
        await event.edit(f'{firstUser} `ile` {secondUser} `arasındaki eşq hesaplandı!`\n**Nəticə:** `%{yuzde}`')

Help = CmdHelp('esqolc')
Help.add_command('olc', None, '<birinci istifadəçi/cavab> <ikinci istifadəçi/siz>', 'Cavab verdiğiniz vəya nickini verdiğiniz kullanıcı ile sizin və ya ikinci istifadəçinin arasındaki sevgini ölçün')
Help.add_info('`@Tagiyeff_018 tərıfindən düzəldilmişdir`')
Help.add()