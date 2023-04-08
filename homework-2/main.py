# Подключается модуль Channel из src.channel
from src.channel import Channel

if __name__ == '__main__':
    # Если скрипт запущен как основной, создается экземпляр класса Channel с идентификатором канала YouTube
    vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')

    # Выводятся значения атрибутов экземпляра vdud
    print(vdud.title)  # вДудь Название канала
    print(vdud.video_count)  # 163 (может уже больше) Количество видео
    print(vdud.url)  # https://www.youtube.com/channel/UCMCgOm8GZkHp8zJ6l7_hIuA

    # Если изменить channel_id на 'Новое название', вызывает ошибку AttributeError, т.к channel_id НЕ МЕНЯЕМ только для чтения (@property).
    vdud.channel_id = 'Новое название'
    # AttributeError: property 'channel_id' of 'Channel' object has no setter

    # можем получить объект для работы с API вне класса с помощью метода get_servce()
    print(Channel.get_service())
    # <googleapiclient.discovery.Resource object at 0x000002B1E54F9750>

    # создаем файл 'vdud.json' в данными по каналу, используя метод to_json(). Файл будет содержать словарь атрибутов экземпляра vdud, в формат JSON.
    vdud.to_json('vdud.json')
