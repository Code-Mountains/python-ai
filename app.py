import os
from googleapiclient.discovery import build

def get_youtube_service(api_key):
    return build('youtube', 'v3', developerKey=api_key)

def search_tutorials(query):
    youtube = get_youtube_service(os.environ.get('YOUTUBE_API_KEY'))

    request = youtube.search().list(
        part="snippet",
        maxResults=10,
        q=query,
        type="video",
        videoCategoryId="27"  # Category for Education
    )
    response = request.execute()

    tutorials = []
    for item in response['items']:
        title = item['snippet']['title']
        video_url = f"https://www.youtube.com/watch?v={item['id']['videoId']}"
        tutorials.append((title, video_url))

    return tutorials

def main():
    user_query = input("Type your question to find tutorials: ")
    tutorials = search_tutorials(user_query)
    
    if tutorials:
        print("Here are some tutorials that might help:")
        for title, url in tutorials:
            print(f"{title}\n{url}\n")
    else:
        print("No tutorials found for your query.")

if __name__ == "__main__":
    main()
