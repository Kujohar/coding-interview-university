import requests
import json


url = "https://leetcode.com/graphql/"

GraphQLQuery = """
query recentAcSubmissions($username: String!, $limit: Int!) {
	recentAcSubmissionList(username: $username, limit: $limit) {
		id
		title
		titleSlug
		timestamp
	}
}
"""
variables = {
    "username": "kujohar999",
    "limit": 100
}

response = requests.post(
    url, json={'query': GraphQLQuery, 'variables': variables})
print(response.json())

# with open("sample.json", "w") as outfile:
#     json.dump(response.json(), outfile)
