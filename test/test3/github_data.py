import requests
import pandas as pd

def issues(repo):
    url = "https://api.github.com/repos/{repo}/issues".format(
        repo=repo)
    response = requests.get(url)
    data = response.json()
    issues_df = pd.DataFrame(response.json(), columns=["number", "title", "user_name"])
    # print(issues_df)
    return issues_df


issues("numpy/numpy")