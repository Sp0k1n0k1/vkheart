#Heart Project
By Volkov Alexey | https://vk.com/sp0ki_n0ki
0. Добываем access_token (https://vkhost.github.io)
0.1 Вписываем в access_token=токен который ты добыл
1. https://dev.vk.com/method/messages.send 1. Вводим наш токен (AccessToken) 2. Вводим в peer_id айди собеседника (УДАЛИТЕ ЧУЖОЙ АЙДИ) 3. Нажимаем выполнить
2. Копируем респонс числа (В результате там будет)
3. CTRL-H Находим id и заменяем на айди собеседника, а messageid заменяем на число из результата response (Респонс)
4. Запускаем
