PATCH_V = "6.08"
BASE_URL = "https://playvalorant.com/"
english = "en-us"
spanish = "es-es"
LANGUAGE = english
PATCH_ENDPOINT = "/news/game-updates/valorant-patch-notes-"

def url_generator(patch_version: str):
    """Generate a URL for the patch notes of a specific version of Valorant

    Args:
        patch_version (str): The version of the patch, formatted as 'X.Y'.

    Returns:
        str: A URL that leads to the patch notes for the specified version.
    """
    modified_ver = patch_version.replace(".", "-")
    url = f"{BASE_URL}{LANGUAGE}{PATCH_ENDPOINT}{modified_ver}"
    
    return url