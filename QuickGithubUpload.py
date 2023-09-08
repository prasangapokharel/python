import requests
import json

# GitHub repository information
repo_owner = "replace with your owner name"  # Replace with your GitHub username or organization name
repo_name = "your repository name"  # Replace with the name of your repository
file_path = r"C:\Users\godsu\Desktop\Python\auto yt open.py"  # Replace with the path to the file you want to upload
branch_name = "main"  # Replace with the name of the branch you want to use

# GitHub personal access token
access_token = "your github acess token"  # Replace with your personal access token
headers = {
    "Authorization": f"token {access_token}",
}

# Get the SHA of the latest commit on the branch
url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/git/refs/heads/{branch_name}"
response = requests.get(url, headers=headers)
latest_commit_sha = json.loads(response.text)["object"]["sha"]

# Upload a new file to the repository
file_content = open(file_path, "rb").read()
file_name = file_path.split("\\")[-1]  # Use double backslashes to split Windows paths

upload_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/git/blobs"
data = {
    "content": file_content.decode("utf-8"),
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
