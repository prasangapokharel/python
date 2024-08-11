import requests
import json

# GitHub repository information
repo_owner = "prasangapokharel"
repo_name = "Calendar_Module.py"
file_path = r""
branch_name = "main"

# GitHub personal access token
access_token = ""
headers = {
    "Authorization": f"token {access_token}",
}
# tyo ni milxa herera yesari nai banaunu parxa arko tool

# Get the SHA of the latest commit on the branch
url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/git/refs/heads/{branch_name}"
response = requests.get(url, headers=headers)

if response.status_code == 200:
    response_data = json.loads(response.text)
    try:
        latest_commit_sha = response_data["object"]["sha"]
    except KeyError as e:
        print(f"Error: {e}")
        print("Failed to retrieve the latest commit. Response content:")
        print(response.text)
        exit()
else:
    print(f"Failed to retrieve the latest commit. Status code: {response.status_code}")
    print(response.text)
    exit()

# Upload a new file to the repository
file_content = open(file_path, "r").read()
file_name = file_path.split("\\")[-1]

upload_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/git/blobs"
data = {
    "content": file_content,
    "encoding": "utf-8",
}
response = requests.post(upload_url, headers=headers, data=json.dumps(data))
blob_sha = json.loads(response.text)["sha"]

# Create a new tree with the uploaded file
tree_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/git/trees"
data = {
    "base_tree": latest_commit_sha,
    "tree": [{"path": file_name, "mode": "100644", "type": "blob", "sha": blob_sha}],
}
response = requests.post(tree_url, headers=headers, data=json.dumps(data))
new_tree_sha = json.loads(response.text)["sha"]

# Create a new commit with the updated tree
commit_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/git/commits"
data = {
    "message": f"Upload {file_name}",
    "parents": [latest_commit_sha],
    "tree": new_tree_sha,
}
response = requests.post(commit_url, headers=headers, data=json.dumps(data))
new_commit_sha = json.loads(response.text)["sha"]

# Update the branch reference to point to the new commit
ref_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/git/refs/heads/{branch_name}"
data = {
    "sha": new_commit_sha,
}
response = requests.patch(ref_url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    print(f"File '{file_name}' uploaded to '{repo_owner}/{repo_name}' on branch '{branch_name}'.")
else:
    print("File upload failed.")
