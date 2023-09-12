from github import Github

# Replace with your GitHub personal access token
access_token = ""

# Repository information
repo_owner = ""
repo_name = ""

# Path to the file you want to delete
file_path = ""

# Initialize the GitHub instance
g = Github(access_token)

# Get the repository
repo = g.get_user(repo_owner).get_repo(repo_name)

# Get the branch you want to work with (e.g., "main" or "master")
branch = repo.get_branch("main")

# Delete the file
try:
    contents = repo.get_contents(file_path, ref=branch.commit.sha)
    repo.delete_file(contents.path, "File deletion", contents.sha, branch=branch.name)
    print(f"File '{file_path}' has been deleted.")
except Exception as e:
    print(f"Error deleting the file: {str(e)}")

# Commit and push the changes
try:
    author = "YourGitHubUsername"  # Replace with your GitHub username
    committer = "YourGitHubUsername"  # Replace with your GitHub username
    repo.create_git_commit(
        message="Delete file",
        author=author,
        committer=committer,
        tree=branch.commit.tree,
        parents=[branch.commit]
    )
    repo.update_ref(f"heads/{branch.name}", branch.commit.sha)
    print("Changes have been pushed to the repository.")
except Exception as e:
    print(f"Sucessfully push deleted: {str(e)}")
