#By Volkov Alexey | https://vk.com/sp0ki_n0ki
#Heart Project
# Инструкция
#0. Добываем access_token (https://vkhost.github.io)
#0.1 Вписываем в access_token=токен который ты добыл
#1. https://dev.vk.com/method/messages.send 1. Вводим наш токен (AccessToken) 2. Вводим в peer_id айди собеседника (УДАЛИТЕ ЧУЖОЙ АЙДИ) 3. Нажимаем выполнить
#2. Копируем респонс числа (В результате там будет)
#3. CTRL-H Находим id и заменяем на айди собеседника, а messageid заменяем на число из результата response (Респонс)
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
