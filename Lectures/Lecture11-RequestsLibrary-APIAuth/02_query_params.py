import requests

postID = int(input("Enter post ID: "))

response = requests.get(
    "https://jsonplaceholder.typicode.com/comments",
    params={"postId": postID}
    )

print(response.status_code)
print(response.json())