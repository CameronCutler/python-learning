import requests

# response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
# print(f"Status Code: {response.status_code}")  # 200 = success
# print(f"Content Type: {response.headers['Content-Type']}")
# print()

# post = response.json()
# print(f"Post Title: {post['title']}")
# print(f"Post Body: {post['body'][:80]}...")
# print(f"Author (userId): {post['userId']}")
# print()


# response = requests.get(
#     "https://jsonplaceholder.typicode.com/posts",
#     params={"userId": 1}
# )

# posts = response.json()
# for post in posts:
#     print(f"Post Title: {post['title']}")
#     print(f"Post Body: {post['body'][:80]}...")
#     print(f"Author (userId): {post['userId']}")
#     print()


new_post = {
    "title": "My New Post",
    "body": "This is the body of my new post.",
    "userId": 1
}
response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=new_post
)
created_post = response.json()
print(f"Created Post ID: {created_post['id']}")
print(f"Created Post Title: {created_post['title']}")
print(f"Created Post Body: {created_post['body'][:80]}...")
print(f"Author (userId): {created_post['userId']}")