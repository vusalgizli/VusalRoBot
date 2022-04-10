import json
import requests
import html
import random
import time

from SiestaRobot import dispatcher
from SiestaRobot.modules.disable import DisableAbleCommandHandler
from SiestaRobot.modules.helper_funcs.chat_status import (is_user_admin)
from telegram.ext import CallbackContext, CommandHandler, Filters, run_async, CallbackQueryHandler
from telegram import ParseMode, Update, InlineKeyboardMarkup, InlineKeyboardButton, replymarkup, ChatPermissions
from telegram.error import BadRequest

def anime_quote():
    url = "https://animechan.vercel.app/api/random"
    # since text attribute returns dictionary like string
    response = requests.get(url)
    try:
        dic = json.loads(response.text)
    except Exception:
        pass
    quote = dic["quote"]
    character = dic["character"]
    anime = dic["anime"]
    return quote, character, anime
def quotes(update: Update, context: CallbackContext):
    message = update.effective_message
    quote, character, anime = anime_quote()
    msg = f"<i>❝{quote}❞</i>\n\n<b>{character} from {anime}</b>"
    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton(
            text="Change🔁",
            callback_data="change_quote")]])
    message.reply_text(
        msg,
        reply_markup=keyboard,
        parse_mode=ParseMode.HTML,
    )
def change_quote(update: Update, context: CallbackContext):
    query = update.callback_query
    chat = update.effective_chat
    message = update.effective_message
    quote, character, anime = anime_quote()
    msg = f"<i>❝{quote}❞</i>\n\n<b>{character} from {anime}</b>"
    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton(
            text="Change🔁",
            callback_data="quote_change")]])
    message.edit_text(msg, reply_markup=keyboard,
                      parse_mode=ParseMode.HTML)
    
def animequotes(update: Update, context: CallbackContext):
    message = update.effective_message
    name = message.reply_to_message.from_user.first_name if message.reply_to_message else message.from_user.first_name
    reply_photo = message.reply_to_message.reply_photo if message.reply_to_message else message.reply_photo
    reply_photo(
        random.choice(QUOTES_IMG))
QUOTES_IMG = (
"https://telegra.ph/file/2af840d4b544283a5681c.jpg","https://telegra.ph/file/40da2e2c8d6845715690b.jpg","https://telegra.ph/file/35a83006ef07392cbbb02.jpg","https://telegra.ph/file/65ded72e902612fa0ecf8.jpg","https://telegra.ph/file/3164eec3577752b00c4a0.jpg","https://telegra.ph/file/de584d0f2c35ce934791c.jpg","https://telegra.ph/file/72986ec12b28c1161c0fe.jpg","https://telegra.ph/file/6e57ddb285f4a7107ef17.jpg","https://telegra.ph/file/e6613983e32c1fdbec6bc.jpg","https://telegra.ph/file/7cebaa2f536f4c9e3a04d.jpg","https://telegra.ph/file/f96d408f674dc98e11996.jpg","https://telegra.ph/file/ccd88451c6b35a41fb919.jpg","https://telegra.ph/file/18f9b0e76cb4b06e9f042.jpg","https://telegra.ph/file/f5c7fb6345ae08b0756c5.jpg","https://telegra.ph/file/25cc40e24d057db5b3510.jpg","https://telegra.ph/file/774c4807415a36d08201c.jpg","https://telegra.ph/file/06615db52698e2b5be527.jpg","https://telegra.ph/file/f602d74490ea334faa996.jpg","https://telegra.ph/file/cc7eba292d8c59426f136.jpg","https://telegra.ph/file/08fa5f7a9a913e602caae.jpg","https://telegra.ph/file/b82768ea54c1b88b761a0.jpg","https://telegra.ph/file/92902e39f863a14bf346a.jpg","https://telegra.ph/file/a09dd5667c6a156a81473.jpg","https://telegra.ph/file/d1295679bc981fd572999.jpg","https://telegra.ph/file/3d70f093b375f96fb40e5.jpg","https://telegra.ph/file/44a86e022a5f524b7174e.jpg","https://telegra.ph/file/76f8b855a22fcdc94720f.jpg","https://telegra.ph/file/5e1ef87d38881c355c694.jpg","https://telegra.ph/file/ec264472ea91541809564.jpg","https://telegra.ph/file/d20622ef559808af97eda.jpg","https://telegra.ph/file/3e7d0bbe7c7d883f752ad.jpg","https://telegra.ph/file/18b6fd691975990da488c.jpg","https://telegra.ph/file/207c46659ec65c5a9a781.jpg","https://telegra.ph/file/40918d64616279ffe3c44.jpg","https://telegra.ph/file/c2b7d80c27ef714de1a9c.jpg","https://telegra.ph/file/bd57dfc0ed53878e71c20.jpg","https://telegra.ph/file/5a6526f7da3854ecc1f15.jpg","https://telegra.ph/file/6418c9e1cb94e5640a55f.jpg","https://telegra.ph/file/1ca2b73228de65600002b.jpg","https://telegra.ph/file/66901b5512df7f6aee500.jpg","https://telegra.ph/file/55b3ae6bf7315d8aaf063.jpg","https://telegra.ph/file/720344bd1304cb85188dc.jpg","https://telegra.ph/file/ab3637e7fcb7f534a43de.jpg","https://telegra.ph/file/d92001692cad50bd020de.jpg","https://telegra.ph/file/037f8d901bcb525dded7d.jpg","https://telegra.ph/file/d3c894daa4d5d62f6006e.jpg","https://telegra.ph/file/86a3caa1f1888d09f9526.jpg","https://telegra.ph/file/578523944035c477c862f.jpg","https://telegra.ph/file/e063803deb43a02a9e353.jpg","https://telegra.ph/file/e4fd43daf77aa7c7e016b.jpg","https://telegra.ph/file/23692be820f2d86761fa2.jpg","https://telegra.ph/file/6125b4338311683b49383.jpg","https://telegra.ph/file/b047c7556e004689d81bc.jpg","https://telegra.ph/file/14826fff6f3f5266d37e9.jpg","https://telegra.ph/file/4c3b09585def5f473a426.jpg","https://telegra.ph/file/88718fc6e67e765cc2824.jpg","https://telegra.ph/file/c91546ba8ebdc5a9ee588.jpg","https://telegra.ph/file/f7e6c732fadd2d63afb11.jpg","https://telegra.ph/file/35bb823ab612c8925f7b4.jpg","https://telegra.ph/file/6cb29cdb77d62a7e81aca.jpg","https://telegra.ph/file/8bc6d95bd3de52a384d0d.jpg","https://telegra.ph/file/9f33742aab0d34d4dc357.jpg","https://telegra.ph/file/980b9a55fa1dc9f2288ac.jpg","https://telegra.ph/file/0f2b48fdd48e0bc419aff.jpg","https://telegra.ph/file/0ba309ed00aae83fb7e2d.jpg","https://telegra.ph/file/e57143440028a7c141440.jpg","https://telegra.ph/file/6c33a5a8dab4a0c4822b9.jpg","https://telegra.ph/file/666a68af2fc6ee5a429a3.jpg","https://telegra.ph/file/eee582a22fc42ed9f2286.jpg","https://telegra.ph/file/eee582a22fc42ed9f2286.jpg","https://telegra.ph/file/9066e1cedb8640e712fe8.jpg","https://telegra.ph/file/0909711f4071ab5bd6252.jpg","https://telegra.ph/file/6c2338b9c8ff62403757f.jpg","https://telegra.ph/file/a4e40d9fcb7f203d6a1ea.jpg","https://telegra.ph/file/7ee1ded692e90ec2f54e3.jpg","https://telegra.ph/file/cfd7e3b6bf3bd99e25f83.jpg","https://telegra.ph/file/7dba92c97c636e64e6561.jpg","https://telegra.ph/file/73c501102cf8c4788de9e.jpg","https://telegra.ph/file/217d3eeba0a805f35f37.jpg","https://telegra.ph/file/2a766819e0c7d6e97c1d2.jpg","https://telegra.ph/file/2cc909aff5d1e2367d0e8.jpg","https://telegra.ph/file/13fed9487f9e28f21b5b3.jpg","https://telegra.ph/file/952d66c246a6203fee602.jpg","https://telegra.ph/file/0c4658ea3174529727d9f.jpg","https://telegra.ph/file/f58e631665de14f5f58e8.jpg","https://telegra.ph/file/45a0d298852ffbee0974b.jpg","https://telegra.ph/file/c704b13ed84f55bd0dccb.jpg","https://telegra.ph/file/a39215d5e52147ab4261a.jpg","https://telegra.ph/file/fd7ef0e5773ab824936fd.jpg","https://telegra.ph/file/5b8c841fd10a423bea884.jpg","https://telegra.ph/file/19fd9f074bbc5be9d783f.jpg","https://telegra.ph/file/69f48f26de9b21b1c3fd1.jpg","https://telegra.ph/file/0d13fabfab12ee1fdc15b.jpg","https://telegra.ph/file/db1224404049c03139189.jpg","https://telegra.ph/file/73fcc5487a6abedbdb1c1.jpg","https://telegra.ph/file/34566f2222ce2ea8db41c.jpg","https://telegra.ph/file/c34a52b1b73f94f4fe2cd.jpg","https://telegra.ph/file/347265b3a372b5c133245.jpg","https://telegra.ph/file/11d45d99903d197ee4f1c.jpg","https://telegra.ph/file/8c6965aefc0c32f218d31.jpg","https://telegra.ph/file/cf2db4ae9bba24b0d4b4d.jpg","https://telegra.ph/file/4d8b2dd35c02e354305dd.jpg","https://telegra.ph/file/1249999649307f0db0ebb.jpg","https://telegra.ph/file/52361bb267d1cbb2569b4.jpg","https://telegra.ph/file/413544c4784c52a772355.jpg","https://telegra.ph/file/9c0c8e033ae1105131acf.jpg","https://telegra.ph/file/18d1a2d17fee22592c1c7.jpg","https://telegra.ph/file/dbd1c1015577dc6ddf075.jpg","https://telegra.ph/file/e9f34c716ac3ddd4b6d92.jpg","https://telegra.ph/file/727aaf87f3d210384e385.jpg","https://telegra.ph/file/a0490f7e22e70dfd2dca5.jpg","https://telegra.ph/file/5fbdb6b18b7438a0b5847.jpg","https://telegra.ph/file/b0799aa20a3728201d8d3.jpg","https://telegra.ph/file/f26df3b8b819b891ba1a4.jpg","https://telegra.ph/file/5ac106f75597dd044bc0b.jpg","https://telegra.ph/file/aa2ae5b4f866c17ed265f.jpg","https://telegra.ph/file/8728850c57f749ffb5fd8.jpg","https://telegra.ph/file/0599e692bcbc514928054.jpg","https://telegra.ph/file/a18e1053f9e5d9850bb52.jpg","https://telegra.ph/file/0d2e10583eb677a89a4ad.jpg""https://telegra.ph/file/53610699438ff6d0cc117.jpg",
"https://telegra.ph/file/ec46abdc7605a349b2deb.jpg",
"https://telegra.ph/file/ea45e7275bfbe7503846b.jpg",
"https://telegra.ph/file/9063eba2a2d11f6dae51b.jpg",
"https://telegra.ph/file/645ba1d6dcd35723e2b82.jpg", 
"https://telegra.ph/file/a7c0c07099851760ce02a.jpg", 
"https://telegra.ph/file/f3bb315ae7937754708ed.jpg", 
"https://telegra.ph/file/96cc43cb2b5329e1eeb19.jpg",
"https://telegra.ph/file/fd67bbf11fa69ea5ef4de.jpg",
"https://telegra.ph/file/730f5fbe1cc155f90edec.jpg",
"https://telegra.ph/file/0cbbd5b53251176244182.jpg",
"https://telegra.ph/file/15571355a71d4bfb6443e.jpg",
"https://telegra.ph/file/717fbf732213c7fe814bb.jpg",
"https://telegra.ph/file/7cc18f54cfffe9433eb69.jpg", 
"https://telegra.ph/file/315df87699e505f7074fa.jpg",
"https://telegra.ph/file/16219318e2171b2968cd3.jpg",
"https://telegra.ph/file/b130887f731b1491e6238.jpg",
"https://telegra.ph/file/599352d566a144fcb87c7.jpg",
"https://telegra.ph/file/7bbec8230bb9c3a1de654.jpg", 
"https://telegra.ph/file/4139e46f8830c4e73df02.jpg",
"https://telegra.ph/file/1a9108e1c34938f9f2bbc.jpg",
"https://telegra.ph/file/b9f148779cd7d1ee61eb1.jpg",
"https://telegra.ph/file/8bf0c8252a38cdce49084.jpg",
"https://telegra.ph/file/9118586d29f1040e2e24b.jpg",
"https://telegra.ph/file/5bff5e812559325c01cde.jpg",
"https://telegra.ph/file/89d178753ae531a8577da.jpg",
"https://telegra.ph/file/f79b78eaca1d5e3098f54.jpg", 
"https://telegra.ph/file/ea45e7275bfbe7503846b.jpg"
"https://telegra.ph/file/38b68d82bbd4a4c7b147f.jpg",
"https://telegra.ph/file/b214e5dee631fa86554cc.jpg",
"https://telegra.ph/file/794a1554479a36ee532ce.jpg", 
"https://telegra.ph/file/acdeed95d27eb5523e7e0.jpg",
"https://telegra.ph/file/bb6ac47b368b4de9c70ec.jpg",
"https://telegra.ph/file/6fea1669b87a31ff2cae3.jpg",
"https://telegra.ph/file/3c53c803dde9aa95e7f04.jpg",
"https://telegra.ph/file/10823b36ecb6188e50575.jpg",
"https://telegra.ph/file/c2a1e358d3bd1227c0d6d.jpg",
"https://telegra.ph/file/24e9bd5c19ea6409fa8c3.jpg",
"https://telegra.ph/file/2fc1c163d97b870798a44.jpg",
"https://telegra.ph/file/74a7aff327fa1129b9bb0.jpg",
"https://telegra.ph/file/9f0c53170227b6f6dcc89.jpg",
"https://telegra.ph/file/ae945a5d0f82727ebce65.jpg",
"https://telegra.ph/file/8f39349083f6875617b92.jpg",
"https://telegra.ph/file/1de4c5721872f9878d956.jpg",
"https://telegra.ph/file/ed69f36c2532bef276fe7.jpg",
"https://telegra.ph/file/7bc1f707719ea09ded836.jpg",
"https://telegra.ph/file/61efc2922cf35c720db8a.jpg", 
"https://telegra.ph/file/32bb982ae3338ed5e830a.jpg",
"https://telegra.ph/file/7c5ff7ea311ca177c1049.jpg", 
"https://telegra.ph/file/595eeaf32909bc89921c0.jpg",
"https://telegra.ph/file/3ea969ead828699151cc6.jpg",
"https://telegra.ph/file/8bfd743656c4f6d1f0d8d.jpg",
"https://telegra.ph/file/cd498e367a4d64e25240a.jpg",
"https://telegra.ph/file/ee3172ab45fff6a14f6c9.jpg",
"https://telegra.ph/file/1e92576712be4204e12ad.jpg",
"https://telegra.ph/file/b197b266f1eace0601453.jpg",
"https://telegra.ph/file/2b847c10b90f1bcb22aac.jpg","https://telegra.ph/file/cb3caa3afb4e0649ce334.png",  
"https://telegra.ph/file/51445aed91c15f8524c7f.png",  
"https://telegra.ph/file/ebffa1e1e1e9f1daa5305.png",  
"https://telegra.ph/file/6f7acc862f6c127f3ef81.png",  
"https://telegra.ph/file/a8c99d5a0e0dcda0eb862.png",  
"https://telegra.ph/file/050c35ca0553b5e93ecfb.png",  
"https://telegra.ph/file/561d266d7744cfe7b9750.png",  
"https://telegra.ph/file/e9c7194e870f7cfb23ffb.png",  
"https://telegra.ph/file/17eb047bcc0858ec2f257.png",  
"https://telegra.ph/file/6400fd26de81a2f24856d.png",  
"https://telegra.ph/file/b6e312ba10250a16d38c8.png",  
"https://telegra.ph/file/65c30845828b0b72f145b.png",  
"https://telegra.ph/file/2f62e95f8a90de5377e3e.png",  
"https://telegra.ph/file/21245e36dee080b9b0626.png",  
"https://telegra.ph/file/8009afc70971269d2f6f3.png",  
"https://telegra.ph/file/e4035427c6d9b10669023.png",  
"https://telegra.ph/file/50a520ceccce2f075d752.png",  
"https://telegra.ph/file/195423459077f11d8eae7.png",  
"https://telegra.ph/file/8bbe67f9b33d289be4ec6.png",  
"https://telegra.ph/file/3f7615281f841701a642f.png",  
"https://telegra.ph/file/42b5ff6e1df0c65250904.png",  
"https://telegra.ph/file/0ab5ff1254397be9e51e5.png",  
"https://telegra.ph/file/be8e335c441bb8b2cbaa6.png",  
"https://telegra.ph/file/6c31e04ba0846cf157853.png",  
"https://telegra.ph/file/70d29917dee443306e81f.png",  
"https://telegra.ph/file/20360545d42c1b8db24f2.png",  
"https://telegra.ph/file/8b49945713223f6d98d05.png",  
"https://telegra.ph/file/04e1b6becd25ba66ccc4f.png",  
"https://telegra.ph/file/5cdce5dddc5c9f92836f3.png",  
"https://telegra.ph/file/7f791eb4f5a4189f3038c.png",  
"https://telegra.ph/file/3acdf6fef8f858c31d95e.png",  
"https://telegra.ph/file/ee20780a5ddeb464c9142.png",  
"https://telegra.ph/file/1c006aaa5d597888bf2d9.png",  
"https://telegra.ph/file/e3c1cce917fee9e2143eb.png",  
"https://telegra.ph/file/9b4522623b8d8729b160f.png",  
"https://telegra.ph/file/ad2215a73765f04bc1c47.png",  
"https://telegra.ph/file/494aec3b4d464fa8ddcd7.png",  
"https://telegra.ph/file/c1726cfcb8ca8a604b1eb.png",  
"https://telegra.ph/file/fa5b117b5f174b6df6f92.png",  
"https://telegra.ph/file/248802c89b438050f4f86.png",  
"https://telegra.ph/file/2f5207602fa8d060d9b76.png",  
"https://telegra.ph/file/8380956a8237c64e63794.png",  
"https://telegra.ph/file/695ab7cf8f9ec2e552cea.png",  
"https://telegra.ph/file/9d54db5a4db865f8cd9e1.png",  
"https://telegra.ph/file/b4696a6f998decfd51cce.png",  
"https://telegra.ph/file/fa572ad7b28d28082ba73.png",  
"https://telegra.ph/file/7c977ab1cb9507f0d0eed.png",  
"https://telegra.ph/file/189cd85e52428df904fd5.png",  
"https://telegra.ph/file/2dd73ec7cc10247bce4c4.png",  
"https://telegra.ph/file/c9154931a18d0059508b7.png","https://telegra.ph/file/fb75df92b167fa5922044.jpg", "https://telegra.ph/file/b0c27d612817b95e64ac4.jpg", "https://telegra.ph/file/d5cec16f9bd0b8556513d.jpg", ",https://telegra.ph/file/8a7b7cc67271489047b77.jpg", "https://telegra.ph/file/1329fd553ceafa3f3ed78.jpg", "https://telegra.ph/file/13dede9b621a70b524bc6.jpg", "https://telegra.ph/file/31b15c8dd5e1e3e1a29fb.jpg", "https://telegra.ph/file/1fec7d342d6b9ab7bafd5.jpg", 
 "https://telegra.ph/file/6178fd02efb5cedcdc0ac.jpg", 
 "https://telegra.ph/file/03b7c531418d180143ce3.jpg", 
 "https://telegra.ph/file/1abb21148686da66e04a2.jpg", 
 "https://telegra.ph/file/16cc8028696383a2fcf9d.jpg", 
 "https://telegra.ph/file/93b0ea47e8b662a86d7c6.jpg", 
 "https://telegra.ph/file/f7135478f049794671752.jpg", 
 "https://telegra.ph/file/9a26ff55f947b25631176.jpg", 
 "https://telegra.ph/file/58215607ccea9f3865dc6.jpg", 
 "https://telegra.ph/file/7c4195ecb7d0cc134039c.jpg", 
 "https://telegra.ph/file/242b231eb2e7010179b2b.jpg", 
 "https://telegra.ph/file/88cd7e8bb8a1dcbd6a7de.jpg", 
 "https://telegra.ph/file/658b499b0f51e7e98af1b.jpg", 
 "https://telegra.ph/file/49c8caf5cd58fa2a327f0.jpg", 
 "https://telegra.ph/file/db23bd3f1838fe5639c1a.jpg", 
 "https://telegra.ph/file/dcfe2dab246b21e078acc.jpg", 
 "https://telegra.ph/file/521fbf4157f6506a9782a.jpg", 
 ",https://telegra.ph/file/ebe16af533a3deecd4b3f.jpg", 
 "https://telegra.ph/file/e3ab56715c101c14904e4.jpg", 
 ",https://telegra.ph/file/e106da1946759c520cb2a.jpg", 
 "https://telegra.ph/file/c43d6d3c2e0a88e64d3e2.jpg", 
 "https://telegra.ph/file/3165e51ef801ff729f06d.jpg", 
 "https://telegra.ph/file/f7f90407da9be2cdfe143.jpg", 
 "https://telegra.ph/file/6645a4aa102fce89fd95b.jpg", 
 "https://telegra.ph/file/78aa400cacc861ff6ba82.jpg", 
 "https://telegra.ph/file/d7ddb5dfff3bd9e5488e2.jpg", 
 "https://telegra.ph/file/0947b3da41e2f5989bd3e.jpg", 
 "https://telegra.ph/file/8b8216cee1ce98792ddc4.jpg", 
 "https://telegra.ph/file/174111d45f6921121e399.jpg", 
 "https://telegra.ph/file/17b41de0d23f7df737312.jpg", 
 "https://telegra.ph/file/f8c34a82907796f9b5a48.jpg", 
 "https://telegra.ph/file/379e1658cb8201768d492.jpg", 
 "https://telegra.ph/file/31917d2b14a87c1d23e1c.jpg", 
 "https://telegra.ph/file/e29b87a7b8d2f6578ab0f.jpg", 
 "https://telegra.ph/file/88d3026cfeb0b41b00daa.jpg", 
 "https://telegra.ph/file/c6f16d880711b3218ec21.jpg", 
 "https://telegra.ph/file/3e077b5ce177087f69cb7.jpg", 
 "https://telegra.ph/file/16b8ec33805b8f3c84db3.jpg", 
 "https://telegra.ph/file/f624e7c074d85b8611b7e.jpg", 
 "https://telegra.ph/file/f3291c8870d960d773fb3.jpg", 
 "https://telegra.ph/file/d3d05ddae859928300e23.jpg", 
 "https://telegra.ph/file/385d9e081228b972fe81a.jpg", 
 "https://telegra.ph/file/868dbe6d2ec455665bb39.jpg", 
 "https://telegra.ph/file/fbb47c83ac1ca5c831f3d.jpg", 
 "https://telegra.ph/file/4da81da0f41d33834e8ec.jpg", 
 "https://telegra.ph/file/892090b577132d22bb40c.jpg", 
 "https://telegra.ph/file/1cb2dd1b36d7a3334cd09.jpg", 
 "https://telegra.ph/file/962102e5062dd8eb68a68.jpg", 
 "https://telegra.ph/file/90ff5cc6216110b16b4ba.jpg", 
 "https://telegra.ph/file/e95ccdc6118f0f45175bb.jpg", 
 "https://telegra.ph/file/d82a6265d4081be1cc8d8.jpg", 
 "https://telegra.ph/file/a6fa184f845f95078017b.jpg", 
 "https://telegra.ph/file/6d31caec6cea4a4ffdcca.jpg", 
 "https://telegra.ph/file/0d36f01088e0f151deb0a.jpg", 
 "https://telegra.ph/file/e5bf04a45b8d999ad779b.jpg", 
 "https://telegra.ph/file/aa6b1bf285a12128d1370.jpg", 
 "https://telegra.ph/file/7109f62d27f31e2b295bc.jpg", 
 "https://telegra.ph/file/40a9ee54a2b095ae10706.jpg", 
 "https://telegra.ph/file/296bf8523fa1e814e01cf.jpg", 
 "https://telegra.ph/file/5be3988117dbbfe2f8ea8.jpg", 
 "https://telegra.ph/file/2c596c563e4b487710463.jpg", 
 "https://telegra.ph/file/d8c11b0bd464a9f4b6194.jpg", 
 "https://telegra.ph/file/3b29a73f5adde44707932.jpg","https://telegra.ph/file/0fc137357ed0f7e99cb7c.jpg", 
 "https://telegra.ph/file/265fb8794dec12d4d81a3.jpg", 
 "https://telegra.ph/file/b53523807e2a6519ee4f0.jpg", 
 "https://telegra.ph/file/05db815dbaf30f727c632.jpg", 
 "https://telegra.ph/file/997213bc32b417786666e.jpg", 
 "https://telegra.ph/file/630e257937db024b58975.jpg","https://telegra.ph/file/7bbb105ffb584b7f5caa8.jpg","https://telegra.ph/file/d57e4b5a3d6fb25d41c74.jpg","https://telegra.ph/file/ee29a1d074e91a329ffcc.jpg","https://telegra.ph/file/478b4d7e9dd79f8c71908.jpg","https://telegra.ph/file/6ede03509e15396995781.jpg","https://telegra.ph/file/0502afceab3a913472e06.jpg","https://telegra.ph/file/51da8fb5a5fc5ff7156f1.jpg","https://telegra.ph/file/3ef0df5a5b98561e2477b.jpg","https://telegra.ph/file/18abcfe5dc2982d4cbc25.jpg","https://telegra.ph/file/d81d7db37be3bd04de236.jpg","https://telegra.ph/file/19c1a975d6ceefbcd2d8b.jpg","https://telegra.ph/file/af1fc294259d1872eb312.jpg","https://telegra.ph/file/2eb1a3fdd1e7295884adf.jpg","https://telegra.ph/file/5e908ab94b6ecb68604b0.jpg","https://telegra.ph/file/2a29ea08d02155a37c8d6.jpg","https://telegra.ph/file/6fbf54b394e173673c1f8.jpg","https://telegra.ph/file/61312944167a23ed66740.jpg","https://telegra.ph/file/f50897b2c6660d1874d4f.jpg","https://telegra.ph/file/bc26c6ae9bcb63d5db979.jpg","https://telegra.ph/file/76527fe0c56c87b251499.jpg","https://telegra.ph/file/9a88121b88e86bea86e7c.jpg","https://telegra.ph/file/22b7778f3f3706ff3f8a8.jpg","https://telegra.ph/file/7441cef10b380ec9df923.jpg","https://telegra.ph/file/28012f6ba8d40a542f1e1.jpg","https://telegra.ph/file/a87ff7e2bfd2c7ddbde65.jpg","https://telegra.ph/file/a4858c442aa61fc5ec8a4.jpg","https://telegra.ph/file/e41475cf7613af1ca6a99.jpg","https://telegra.ph/file/be3f8f71f25e6a9fce623.jpg","https://telegra.ph/file/12bc5eb6b74624acd94f9.jpg","https://telegra.ph/file/4a1c263182c69c1bd6740.jpg","https://telegra.ph/file/4f35c6148799571f46de5.jpg","https://telegra.ph/file/95f3435abf993a503d0c0.jpg","https://telegra.ph/file/806f5a508d4b67baa1162.jpg","https://telegra.ph/file/91ef26ecb253115578143.jpg","https://telegra.ph/file/f3f7868005e15da1e6aff.jpg","https://telegra.ph/file/e370b6d528e0025ba86eb.jpg","https://telegra.ph/file/3ba0ce1b502711263c15f.jpg","https://telegra.ph/file/77fcec37b366781665c68.jpg","https://telegra.ph/file/67097cd8d9af4df7f10c8.jpg","https://telegra.ph/file/269f5a591305af5b18268.jpg","https://telegra.ph/file/8cb76160a63f7aca11b77.jpg","https://telegra.ph/file/5a8b7e59006f8e8f6e183.jpg","https://telegra.ph/file/5a7e9c4670f7015c9ddc2.jpg","https://telegra.ph/file/cdc9257c1a4c359f9a65f.jpg","https://telegra.ph/file/1633e0f910bc1dc75d554.jpg","https://telegra.ph/file/9bbd4a5579805a67b4e44.jpg","https://telegra.ph/file/3cf65a942e4df002d491c.jpg","https://telegra.ph/file/3370614e62146a2ee67b6.jpg","https://telegra.ph/file/103401f7ff1e470fc574e.jpg","https://telegra.ph/file/7cc7a8f0efad15cce469d.jpg","https://telegra.ph/file/6a28b8969692b3bae320d.jpg","https://telegra.ph/file/738b231556c83534384a0.jpg","https://telegra.ph/file/158f0cc9f949d75a070a6.jpg","https://telegra.ph/file/f9636f445b262a953a8cf.jpg","https://telegra.ph/file/ba144c3b438fd8cf61fad.jpg","https://telegra.ph/file/9e0bb3846ced1b6061f5e.jpg","https://telegra.ph/file/679b63537f795f5715393.jpg","https://telegra.ph/file/5871ab5b28955a47ce241.jpg","https://telegra.ph/file/b6eb820ead45498a1f9e8.jpg","https://telegra.ph/file/bfdff3dd6bedbf0abd840.jpg","https://telegra.ph/file/9d4ea08fe12506f95e441.jpg","https://telegra.ph/file/c017600294af5a2650c0c.jpg","https://telegra.ph/file/25e7bcdbaa6b850a3527f.jpg","https://telegra.ph/file/d5d11117f7556cffacde8.jpg","https://telegra.ph/file/665b2f327003372c2a21b.jpg","https://telegra.ph/file/7fb89d9a20f8c443e031c.jpg","https://telegra.ph/file/3546fcc187562cb80cd38.jpg","https://telegra.ph/file/a8b2afee9f4276f7e165e.jpg","https://telegra.ph/file/aff0e31cc81048947ab0a.jpg","https://telegra.ph/file/73df79e314fae47c43592.jpg","https://telegra.ph/file/719c73f9f5fac9f152adb.jpg","https://telegra.ph/file/236348b78107d7dfcbd70.jpg","https://telegra.ph/file/48f1060c2ebb4c5e8c6c4.jpg","https://telegra.ph/file/ebc6ccb101c7a487ba3a1.jpg","https://telegra.ph/file/56a014dd99c1e0b9b47a0.jpg","https://telegra.ph/file/327e45a0ad7c07d5712d8.jpg","https://telegra.ph/file/a24768cf792b65a32974d.jpg","https://telegra.ph/file/046afc9635a374fbac886.jpg","https://telegra.ph/file/c2cb934a04663eb24caa3.jpg","https://telegra.ph/file/4a4a69d12db9d82f54e3c.jpg","https://telegra.ph/file/5fb1facdc6bb84791c770.jpg","https://telegra.ph/file/97a53270e6faeda43cea6.jpg","https://telegra.ph/file/7343b7b628c05b32bedcb.jpg","https://telegra.ph/file/0695bb8c78b14d34f42f3.jpg","https://telegra.ph/file/a277e1268677055527e05.jpg","https://telegra.ph/file/064331f9a29d25450b86b.jpg","https://telegra.ph/file/94a5e2d09be9dbcebad18.jpg","https://telegra.ph/file/760666351a27db319a04d.jpg","https://telegra.ph/file/91c23d72e45ca86c9d6a5.jpg","https://telegra.ph/file/830b35ac2ad9d28cf61ad.jpg","https://telegra.ph/file/2c956954e0beb4971d34d.jpg","https://telegra.ph/file/ca363c0aa71cfdb3a1b1d.jpg","https://telegra.ph/file/b3d0ef085098cd7b0f121.jpg","https://telegra.ph/file/cf0cd1ee085c50531dbbc.jpg","https://telegra.ph/file/0b7fc3ff3f8f5778266bf.jpg","https://telegra.ph/file/93f238e3adb4e1910d2d6.jpg","https://telegra.ph/file/20d3c362c5f5106221b61.jpg","https://telegra.ph/file/d1f54f00809da79a7a66a.jpg","https://telegra.ph/file/a6084dac7b9f09d39999c.jpg","https://telegra.ph/file/63dcb98ee31c5552134d5.jpg","https://telegra.ph/file/5728405d59688276e25d8.jpg","https://telegra.ph/file/898178bb3dcaabf45d17a.jpg","https://telegra.ph/file/6a8bb123a09f491c823bd.jpg","https://telegra.ph/file/2282e0660e9aacefa68e6.jpg","https://telegra.ph/file/b0af6dbbca7a3693f359d.jpg","https://telegra.ph/file/1d405f3125b9c4a127b0d.jpg","https://telegra.ph/file/fd69a713ee3db13b27c92.jpg","https://telegra.ph/file/f26655f880db685f044b0.jpg","https://telegra.ph/file/f3006456ca350da767ac2.jpg","https://telegra.ph/file/568ff17eaf96fbefd4e2a.jpg","https://telegra.ph/file/80c052d33194afcb121f4.jpg","https://telegra.ph/file/780da73fe667b90f1c459.jpg","https://telegra.ph/file/c0c3af3d2bad0e9a71480.jpg","https://telegra.ph/file/61f6db708665892de2745.jpg","https://telegra.ph/file/9b2b7062edf5db0c374c5.jpg","https://telegra.ph/file/e507548729ab693f283b5.jpg","https://telegra.ph/file/bbc7ad47a237ab1e0fbf9.jpg","https://telegra.ph/file/6d6c5fea1b85c85ac0c2b.jpg","https://telegra.ph/file/d6dac8eea84a023faa36e.jpg","https://telegra.ph/file/aa07509542cc1bd4a0d0c.jpg","https://telegra.ph/file/4bf47e621e4580f91e344.jpg","https://telegra.ph/file/82a2fa2ca0a3de6d856c7.jpg","https://telegra.ph/file/008a8d9c0f81c0db00cb0.jpg","https://telegra.ph/file/c3509962edbe7872cb482.jpg","https://telegra.ph/file/273f2401cbc69c59ce833.jpg","https://telegra.ph/file/9d57b1dd968f83b4c179b.jpg","https://telegra.ph/file/5167198fc09f5d7b66cef.jpg","https://telegra.ph/file/68e5927c2e37917b9c2e2.jpg","https://telegra.ph/file/ffe3a353a5e3bd511f246.jpg","https://telegra.ph/file/230ed1ba5e575511ced1c.jpg","https://telegra.ph/file/b36223ed2f94b73427c11.jpg","https://telegra.ph/file/7264f312503480d421398.jpg","https://telegra.ph/file/f42e09b1e2e19d2163c1c.jpg","https://telegra.ph/file/fba6177af6f6a8aeba9eb.jpg","https://telegra.ph/file/bb4da75695e9ca90aa1cd.jpg","https://telegra.ph/file/65365adb339139759eb99.jpg","https://telegra.ph/file/331fcb39e12eed757c01f.jpg","https://telegra.ph/file/4fc346b7b5891fe92bf19.jpg","https://telegra.ph/file/aaab848e9d3575869a3f5.jpg","https://telegra.ph/file/e3ab9346a63603a78df64.jpg","https://telegra.ph/file/7f16dfd1ab39de71d28fd.jpg","https://telegra.ph/file/109d80fdd791943aa4baa.jpg","https://telegra.ph/file/ca96588f6ffeabfd9aee1.jpg","https://telegra.ph/file/86fc6a6506020c1d88ff9.jpg","https://telegra.ph/file/a4d0c244ac13eb106615a.jpg","https://telegra.ph/file/d2bc8efb69adc153d8d32.jpg"
      
      )    

ANIMEQUOTES_HANDLER = DisableAbleCommandHandler("animequotes", animequotes, run_async=True)
QUOTES_HANDLER = DisableAbleCommandHandler("quote", quotes, run_async=True)

CHANGE_QUOTE = CallbackQueryHandler(
    change_quote, pattern=r"change_.*")
QUOTE_CHANGE = CallbackQueryHandler(
    change_quote, pattern=r"quote_.*")
dispatcher.add_handler(CHANGE_QUOTE)
dispatcher.add_handler(QUOTE_CHANGE)
dispatcher.add_handler(ANIMEQUOTES_HANDLER)
dispatcher.add_handler(QUOTES_HANDLER)

__command_list__ = [

    "animequotes",
    "quote"

]

__handlers__ = [

    ANIMEQUOTES_HANDLER,
    QUOTES_HANDLER

]
