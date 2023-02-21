import requests
import json
import datetime


url = "https://leetcode.com/graphql/"

GraphQLQuery = """
query recentAcSubmissions($username: String!, $limit: Int!) {
	recentAcSubmissionList(username: $username, limit: $limit) {
		id
		title
		titleSlug
		timestamp
		statusDisplay
		lang
		url
		runtime
		memory
	}
}
"""
variables = {
    "username": "kujohar999",
    "limit": 100
}

response = requests.post(
    url, json={'query': GraphQLQuery, 'variables': variables})
# print(response.json())
# print(response.cookies)


D = datetime.datetime.now()
with open("../LeetCodeData-" +
          D.strftime("%Y-%m-%d") +
          ".json", "w") as outfile:
    json.dump(response.json(), outfile)
