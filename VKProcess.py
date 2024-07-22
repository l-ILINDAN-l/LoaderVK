import vk_api
import requests

# Функция для авторизации в VK
def auth_vk(login, password, app_id, api_version='5.131'):
    vk_session = vk_api.VkApi(login, password, app_id=app_id, api_version=api_version)
    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return None
    vk = vk_session.get_api()
    return vk

# Функция для поиска видео по ключевому слову
def search_videos(vk, query, count=10):
    try:
        response = vk.video.search(q=query, count=count)
        videos = response['items']
        return videos
    except vk_api.ApiError as e:
        print(f"Ошибка при поиске видео: {e}")
        return []

# Функция для получения ссылки на видео
def get_video_url(vk, owner_id, video_id):
    try:
        response = vk.video.get(videos=f"{owner_id}_{video_id}")
        if response['items']:
            video = response['items'][0]
            return video.get('player')
    except vk_api.ApiError as e:
        print(f"Ошибка при получении ссылки на видео: {e}")
    return None

# Функция для загрузки видео
def download_video(video_url, save_path):
    try:
        response = requests.get(video_url, stream=True)
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=1024):
                    file.write(chunk)
            print(f"Видео сохранено по пути: {save_path}")
        else:
            print(f"Ошибка загрузки видео: {response.status_code}")
    except requests.RequestException as e:
        print(f"Ошибка при загрузке видео: {e}")