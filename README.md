# LoaderVK
The application will search for videos posted on VK to upload videos.

Installing dependencies
First, install the necessary libraries:
pip install vk_api requests

Explanation of the code
Authorization: The auth_vk function uses the vk_api library to authorize the user in VK.
Video search: The search_videos function searches for videos for a given query using the video.search method from the VK API.
Getting a link to a video: The get_video_url function gets a link to a video using the video.get method.
Video download: The download_video function downloads the video by URL and saves it to disk.
Main function: In main, all of the above functions are called, and the process of searching and downloading videos is controlled.

Setting
up login parameters: Login from your VK account.
password: The password for your VK account.
app_id: The ID of your VK application.
search_query: A request to search for a video.
download_folder: Folder for saving downloaded videos.
