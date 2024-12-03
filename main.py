import os
import requests
import zipfile
from io import BytesIO
from tqdm import tqdm

def download_repos():
    github_username = input("Entrez le nom d'utilisateur GitHub : ").strip()
    output_directory = os.path.join(os.getcwd(), "GithubRepos")
    os.makedirs(output_directory, exist_ok=True)
    token = input("Entrez le token GitHub (laisser vide si non nécessaire) : ").strip() or None
    headers = {"Authorization": f"token {token}"} if token else {}
    repos_url = f"https://api.github.com/users/{github_username}/repos"
    response = requests.get(repos_url, headers=headers)
    if response.status_code != 200:
        print("Erreur lors de la récupération des repositories :", response.json())
        return
    repos = response.json()
    for repo in tqdm(repos, desc="Téléchargement des repositories"):
        repo_name = repo["name"]
        zip_url = f"https://github.com/{github_username}/{repo_name}/archive/refs/heads/main.zip"
        repo_dir = os.path.join(output_directory, repo_name)
        os.makedirs(repo_dir, exist_ok=True)
        zip_response = requests.get(zip_url, headers=headers, stream=True)
        if zip_response.status_code == 200:
            with zipfile.ZipFile(BytesIO(zip_response.content)) as zip_file:
                zip_file.extractall(repo_dir)

download_repos()
