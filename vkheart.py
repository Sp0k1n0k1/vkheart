#By Volkov Alexey | https://vk.com/sp0ki_n0ki
#Heart Project
#0. Добываем access_token
#0.1 Вписываем в token= Твой токен
#1. https://dev.vk.com/method/messages.send веддите  напишите айди собеседника, удалите из строки peer_id ВСЕ а в message введите что хотите!
#2. Копируем респонс числа
#3. Заменяем в 0,коде message_id=число из респонс
#4. Запускаем

import vk_api
import time

vk_session = vk_api.VkApi(token="token")
vk = vk_session.get_api()

vk.messages.edit(peer_id="id", message="𝓑𝔂 𝓐𝓵𝓮𝔁 𝓥𝓸𝓵𝓴𝓸𝓿 | https://vk.com/sp0ki_n0ki", message_id=messageid)
time.sleep(1)
vk.messages.edit(peer_id="id", message="""
	☁☁☁☁☁☁☁☁☁
	☁☁💗💗☁💗💗☁☁
	☁💗💗💗💗💗💗💗☁
	☁💗💗💗💗💗💗💗☁
	☁💗💗💗💗💗💗💗☁
	☁☁💗💗💗💗💗☁☁
	☁☁☁💗💗💗☁☁☁
	☁☁☁☁💗☁☁☁☁
	☁☁☁☁☁☁☁☁☁""", message_id=messageid)
time.sleep(1)
vk.messages.edit(peer_id="id", message="""
	🖤🖤🖤🖤🖤🖤🖤🖤🖤🖤🖤 
	🖤🖤❤❤🖤🖤🖤❤❤🖤🖤 
	🖤❤❤❤❤❤❤❤❤❤🖤 
	🖤❤❤❤❤❤❤❤❤❤🖤 
	🖤❤❤❤❤❤❤❤❤❤🖤 
	🖤🖤❤❤❤❤❤❤❤🖤🖤 
	🖤🖤🖤❤❤❤❤❤🖤🖤🖤 
	🖤🖤🖤🖤❤❤❤🖤🖤🖤🖤 
	🖤🖤🖤🖤🖤❤🖤🖤🖤🖤🖤 
	🖤🖤🖤🖤🖤🖤🖤🖤🖤🖤🖤""", message_id=messageid)
time.sleep(1)
vk.messages.edit(peer_id="id", message="""
	💙💙💙💙💙💙💙💙💙💙💙 
	💙💙💜💜💙💙💙💜💜💙💙 
	💙💜💜💜💜💜💜💜💜💜💙 
	💙💜💜💜💜💜💜💜💜💜💙 
	💙💜💜💜💜💜💜💜💜💜💙 
	💙💙💜💜💜💜💜💜💜💙💙 
	💙💙💙💜💜💜💜💜💙💙💙 
	💙💙💙💙💜💜💜💙💙💙💙 
	💙💙💙💙💙💜💙💙💙💙💙 
	💙💙💙💙💙💙💙💙💙💙💙""", message_id=messageid)
time.sleep(1)
vk.messages.edit(peer_id="id", message="I", message_id=messageid)
time.sleep(1)
vk.messages.edit(peer_id="id", message="LOVE", message_id=messageid)
time.sleep(1)
vk.messages.edit(peer_id="id", message="YOU❤️", message_id=messageid)
time.sleep(1)
vk.messages.edit(peer_id="id", message="I LOVE YOU❤️", message_id=messageid)