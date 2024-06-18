import webbrowser

def open_fb_urls(usernames):
    base_url = "https://www.facebook.com/"
    for username in usernames:
        url = f"{base_url}{username}"
        webbrowser.open(url)

if __name__ == "__main__":
    # List of usernames
    usernames = [
        "victoriawalks",
        "malingroad",
        "eyewatchboroondara",
        "HARTHartwell",
        "UnionRoadSurreyHills",
    ]
    
    open_fb_urls(usernames)