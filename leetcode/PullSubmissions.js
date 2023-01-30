var request = require('request');

siteURL = "https://leetcode.com/graphql/"
query = {
    "query": "\n    query recentAcSubmissions($username: String!, $limit: Int!) {\n  recentAcSubmissionList(username: $username, limit: $limit) {\n    id\n    title\n    titleSlug\n    timestamp\n  }\n}\n    ",
    "variables": {
        "username": "kujohar999",
        "limit": 15
    }
}

request.post(
    siteURL,
    { json: query },
    function (error, response, body) {
        if (!error && response.statusCode == 200) {
            console.log(response.toJSON().body);
        }
    }
);