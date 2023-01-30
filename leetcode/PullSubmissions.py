import requests,json


url = "https://leetcode.com/graphql/"
query = {
    "query": "\n    query recentAcSubmissions($username: String!, $limit: Int!) {\n  recentAcSubmissionList(username: $username, limit: $limit) {\n    id\n    title\n    titleSlug\n    timestamp\n  }\n}\n    ",
    "variables": {
        "username": "kujohar999",
        "limit":100
        }
        }

response = requests.post(url,json = query)
print(response.json())


# with open("sample.json", "w") as outfile:
#     json.dump(response.json(), outfile)