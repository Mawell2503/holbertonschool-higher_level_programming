import requests
import csv

URL = "https://jsonplaceholder.typicode.com/posts"

#  Part 1 
def fetch_and_print_posts():
    #  "go to this URL, ask for he data of the server and store it in response"
    response = requests.get(URL)

    #  "show me what the server request said"
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()

        for post in data:
            print(post["title"])

#  Part 2
def fetch_and_save_posts():
    response = requests.get(URL)

    if response.status_code == 200:
        data  = response.json () 

        posts_list = []
        for post in data:
             posts_list.append({
                 "id": post["id"],
                 "title": post["title"],
                 "body": post["body"]
             })

        with open("posts.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            
            writer.writeheader()
            writer.writerows(posts_list)