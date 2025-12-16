# downloader.py
import requests

def download_latest(repo, output_file):
    """
    Télécharge le premier .exe trouvé dans la dernière release d'un repo GitHub.
    
    repo: "user/repo"  (ex: "yo-le-zz/Explorateur_distant")
    output_file: chemin local où sauvegarder le .exe téléchargé
    """
    api_url = f"https://api.github.com/repos/{repo}/releases/latest"

    # Récupère la dernière release
    r = requests.get(api_url, timeout=15)
    if r.status_code != 200:
        raise RuntimeError(f"Impossible de récupérer la dernière release : {r.status_code}")

    data = r.json()

    # Cherche le premier asset .exe
    download_url = None
    for asset in data.get("assets", []):
        if asset["name"].lower().endswith(".exe"):
            download_url = asset["browser_download_url"]
            break

    if not download_url:
        raise RuntimeError("Aucun fichier .exe trouvé dans la dernière release")

    # Télécharge le fichier
    with requests.get(download_url, stream=True, timeout=30) as r:
        r.raise_for_status()
        with open(output_file, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

    print(f"Téléchargement terminé : {output_file}")

