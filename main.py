import os
from VKProcess import *
# Основная функция
def main(login, password, app_id, search_query, download_folder='videos'):
    # Авторизация в VK
    vk = auth_vk(login, password, app_id)
    if vk is None:
        return

    # Поиск видео
    videos = search_videos(vk, search_query)

    # Создание папки для загрузки видео
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    # Загрузка каждого видео
    for video in videos:
        owner_id = video['owner_id']
        video_id = video['id']
        title = video['title']
        video_url = get_video_url(vk, owner_id, video_id)
        if video_url:
            save_path = os.path.join(download_folder, f"{title}_{video_id}.mp4")
            download_video(video_url, save_path)
        else:
            print(f"Не удалось получить ссылку на видео {title} ({video_id})")

if __name__ == "__main__":
    # Замените на ваши учетные данные и параметры
    login = 'your_login'
    password = 'your_password'
    app_id = 'your_app_id'
    search_query = 'your_search_query'

    main(login, password, app_id, search_query)