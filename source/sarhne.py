import random
from pyrogram import Client, filters
from source.info import (joinch)
from pyrogram import enums
from source.Data import (get_userbot)

sarhne = ["هل تعرضت لغدر في حياتك؟" ,
 " هل أنت مُسامح أم لا تستطيع أن تُسامح؟" , 
"هل تعرضت للخيانة في يومٍ ما؟" , 
 "ما هو القرار الذي اتخذتهُ ولم تندم عليه؟" ,  
"ما هي الشخصية المُميزة في حياتك؟" , 
 "من هو الشخص الذي تُفكر به دائمًا؟" , 
"ما هو الشخص الذي لا تستطيع أن ترفض له أي طلب؟" , 
 "هل ترى نفسك مُتناقضًا؟" ,  
"ما هو الموقف الذي تعرضت فيه إلى الاحراج الشديد؟" , 
 "هل تُتقن عملك أم تشعر بالممل؟" ,  
"هل أنت شخص عُدواني؟" , 
 "هل حاربت من أجل شخص ما؟" , 
"ما هي الكلمة التي تُربكك؟", 
 " من هو الشخص الذي تُصبح أمامه ضعيفًا؟" , 
"هل تحب المُشاركة الاجتماعية أم أنت شخص مُنطوي؟" , 
 "هل تنازلت عن مبدأك في الحياة من قبل؟" ,  
"اختصر حياتك في كلمة واحدة؟" , 
 "ما هو أسوأ خبر سمعته بحياتك؟" , 
"ما الشيء الذي يجعلك تشعر بالخوف؟" , 
 "من هو الشخص الذي لا تندم عليه إذا تركك وخرج من حياتك؟" , 
"هل انت ممن يحب التملك؟" , 
 "هل تشعر بالرضا عن نفسك؟" , 
"ما الذي يجعلك تُصاب بالغضب الشديد؟" , 
 "هل أنت شخص صريح أم مُنافق؟", 
"هل تحب جميع أخواتك بنفس المقدار أم تستثنى أحدهم في قلبك؟" , 
"هل كنت سبب في تدمير حياة أحد الأشخاص المُقربين إليك؟" , 
"من هو الشخص الذي تستطيع أن تحكي له أي مشكلة بدون خجل او تردد؟" , 
"إذا عرفت أن صديقك المُفضل يحب أختك فماذا تفعل؟" , 
"هل الملابس تُسبب لك انطباعات مُختلفة عن الأشخاص؟" , 
"ما هو الشيء الذي يُلفت انتباهك؟" , 
"ما هو رأيك في حظك؟" , 
"هل تعلقت بشخص معين لدرجة كنت لا تتخيلها؟" , 
"هل قمت بتهديد شخص قام بفعل شيء مُحرج؟" , 
"هل تشعر بالسعادة في حياتك؟" , 
"من هو الشخص الذي رحل عن الحياة وعندما تتذكره تشعر بالألم؟" , 
"من هو الشخص الذي خذلك؟" , 
"إذا قمت بتصنيف نفسك فهل تختار أنك إنسان سلبي أم إيجابي؟" , 
"متى آخر مرة قلت كلمك بحبك؟" , 
"هل تشعر بالراحة عند سماع القرآن الكريم؟" , 
"إذا تعرضت لموقف جعلك مُتهم في ارتكاب جريمة سرقة ، وأنت لم تقم بفعلها فما هو تبريرك لتُخلص نفسك من هذه الجريمة؟" , 
"هل أنت مُتعلم تعليم عالي أم تعليم مُتوسط؟" , 
"ما هو الإقرار الذي تقره أمام نفسك وأمام الجميع؟" , 
"ما رأيك ! هل يُمكن أن تتحول الصداقة إلى حب حقيقي؟" , 
"هل تعرضت للظلم من قبل؟" , 
"هل تستطيع أن تعيش بدون أصدقاء؟" , 
"ما هو الموقف الذي جعلك تكذب؟" , 
"من هو أغلى شخص في حياتك؟" , 
"هل تناولت أحد أنواع المواد الكحولية أو المُخدرات من قبل؟" , 
"إذا أصبحت رئيسًا للجمهورية فما هو أول قرار سوف تتخذه لتصليح حال البلاد؟" , 
"هل ندمت على حب شخص؟" , 
"هل ضحكت من قبل وانت في عذاء للمُتوفي؟" , 
"ما هو أصعب موقف تعرضت له في حياتك؟" , 
"من هو الشخص الذي تهرب منه؟" , 
"هل تشعر بأنك بخيل ولا تستطيع أن تُنفق ما لديك؟" , 
"هل شعرت بأنك تتمنى أن تموت؟" , 
"إذا أحببت صديقتك ، فهل تستطيع أن تُخبرها عن هذا الحب؟"]

sarhneto = ["مش ناوي تبطل الكدب دا", 
"ايوه كمل كدب كمل",
"الكلام دا ميه ميه ي معلم",
"عايز اقولك خف كدب عشان هتخش النار",
"خخخش هتجيبك",
"الكدب حرام ياخي اتقي الله ",
"احلف ؟",
"انت راجل مظبوط علفكره",
"حصل حصل مصدقك ",
"انا مفهمتش انت قولت اي بس انت صح",
"كلامك عشره علي عشره ❤️",
"تعرف تسكت وتبطل هري؟"]


@Client.on_message(filters.command(["صراحة", "اسئلة", "اسئله", "صراحه"], ""))
async def bott1(client: Client, message):
   try:
    if not message.chat.type == enums.ChatType.PRIVATE:
       if await joinch(message):
            return
    bar = random.choice(sarhne)
    barto = random.choice(sarhneto)
    ask = await client.ask(message.chat.id, f"**{bar}**", filters=filters.user(message.from_user.id), reply_to_message_id=message.id, timeout=100)
    await ask.reply_text(f"**{barto}**")
   except:
       pass
   
@Client.on_message(filters.command("تحديث صراحه", ""))
async def tiillllli(client, message):
 if message.from_user.username in ["L_HLN"]:
   await client.send_sticker(message.chat.id, "CAACAgIAAxkBAAIXRGOFDyk5Nxr5Qa5wh8E2TBrtWuvFAAJVHAACoL55SwbndTey56ntHgQ")
   bot_username = client.me.username
   user = await get_userbot(bot_username)
   async for msg in user.get_chat_history("sarhne_elnqyb"):
       if not msg.text in sarhne:
         sarhne.append(msg.text)
   if message.from_user.username == "L_HLN":
     await message.reply_text(f"**تم تنفيذ الامر بواسطة المطور كينج .**")
   else:
     await message.reply_text(f"**تم تحديث صراحه .**")