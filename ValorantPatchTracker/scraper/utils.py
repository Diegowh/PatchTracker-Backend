PATCH_V = "3.08"
BASE_URL = "https://valorant.fandom.com/wiki/Patch_Notes/"

def url_generator(patch_version: str):
    """
    Generate a URL for the patch notes of a specific version of Valorant
    """
    return f"{BASE_URL}{patch_version}"