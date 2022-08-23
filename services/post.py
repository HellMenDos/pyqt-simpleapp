import requests

def get_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    return [data['title'] for index, data in enumerate(response.json())]

def get_posts_by_title(str):
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    posts = [data['title'] for index, data in enumerate(response.json()) if str in data['title']]
    return posts

if __name__ == '__main__':
    print(get_posts())
    print(get_posts_by_title('sequi'))