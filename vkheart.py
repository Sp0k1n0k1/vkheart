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

vk_session = vk_api.VkApi(token="64df32ac68e510172d3f86c94424a2e871587aee07642974e2319840c7135d7886b59fab6fb71e533e562")
vk = vk_session.get_api()

vk.messages.edit(peer_id="666572848", message="𝓑𝔂 𝓐𝓵𝓮𝔁 𝓥𝓸𝓵𝓴𝓸𝓿 | https://vk.com/sp0ki_n0ki", message_id=424626)
time.sleep(1)
vk.messages.edit(peer_id="666572848", message="""
	☁☁☁☁☁☁☁☁☁
	☁☁💗💗☁💗💗☁☁
	☁💗💗💗💗💗💗💗☁
	☁💗💗💗💗💗💗💗☁
	☁💗💗💗💗💗💗💗☁
	☁☁💗💗💗💗💗☁☁
	☁☁☁💗💗💗☁☁☁
	☁☁☁☁💗☁☁☁☁
	☁☁☁☁☁☁☁☁☁""", message_id=424626)
time.sleep(1)
vk.messages.edit(peer_id="666572848", message="""
	🖤🖤🖤🖤🖤🖤🖤🖤🖤🖤🖤 
	🖤🖤❤❤🖤🖤🖤❤❤🖤🖤 
	🖤❤❤❤❤❤❤❤❤❤🖤 
	🖤❤❤❤❤❤❤❤❤❤🖤 
	🖤❤❤❤❤❤❤❤❤❤🖤 
	🖤🖤❤❤❤❤❤❤❤🖤🖤 
	🖤🖤🖤❤❤❤❤❤🖤🖤🖤 
	🖤🖤🖤🖤❤❤❤🖤🖤🖤🖤 
	🖤🖤🖤🖤🖤❤🖤🖤🖤🖤🖤 
	🖤🖤🖤🖤🖤🖤🖤🖤🖤🖤🖤""", message_id=424626)
time.sleep(1)
vk.messages.edit(peer_id="666572848", message="""
	💙💙💙💙💙💙💙💙💙💙💙 
	💙💙💜💜💙💙💙💜💜💙💙 
	💙💜💜💜💜💜💜💜💜💜💙 
	💙💜💜💜💜💜💜💜💜💜💙 
	💙💜💜💜💜💜💜💜💜💜💙 
	💙💙💜💜💜💜💜💜💜💙💙 
	💙💙💙💜💜💜💜💜💙💙💙 
	💙💙💙💙💜💜💜💙💙💙💙 
	💙💙💙💙💙💜💙💙💙💙💙 
	💙💙💙💙💙💙💙💙💙💙💙""", message_id=424626)
time.sleep(1)
vk.messages.edit(peer_id="666572848", message="I", message_id=424626)
time.sleep(1)
vk.messages.edit(peer_id="666572848", message="LOVE", message_id=424626)
time.sleep(1)
vk.messages.edit(peer_id="666572848", message="YOU❤️", message_id=424626)
time.sleep(1)
vk.messages.edit(peer_id="666572848", message="I LOVE YOU❤️", message_id=424626)