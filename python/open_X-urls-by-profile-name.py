import webbrowser

def open_x_urls(usernames):
    base_url = "https://x.com/"
    for username in usernames:
        url = f"{base_url}{username}"
        webbrowser.open(url)

if __name__ == "__main__":
    # List of usernames
    usernames = [
        "StreetsYarra",
        "BristolCycling",
        "yarrabike",
        "UserBicycle",
        "katie_cardigan",
        "MelbourneWay",
        "liveable_melb",
        "bikemelbourne",
    ]
    
    open_x_urls(usernames)