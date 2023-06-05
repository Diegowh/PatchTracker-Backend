from .version_fetcher import VersionFetcher
from .scraper import Scraper


def all_episodes_data():
    '''Returns a list with all episodes and patch data'''
    episodes = VersionFetcher().episodes()
    
    for episode in episodes:
        for version in episode['versions']:
            scraper = Scraper(version['patch_endpoint'])
            version['content'] = style_html(scraper.patch_html.strip())
            # version['content'] = "<h1>HTML PLACEHOLDER</h1>"
        
    return episodes

def style_html(content):
    return f"""<!DOCTYPE html>
    <html>
    <head>
    <style>
    body {{
        font-family: -apple-system, sans-serif;
        font-size: 35px;
        line-height: 1.6;
        padding: 20px;
        border: 2px solid #000000;
    }}
    </style>
    </head>
    <body>
    {content}
    </body>
    </html>
    """
    
    