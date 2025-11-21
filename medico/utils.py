import requests

def geocode_address(address):
    api_key = "5ab90ada2cf84cd5b389a4c6b94315fb"  #  clé API OpenCage
    url = "https://api.opencagedata.com/geocode/v1/json"
    params = {
        "q": address,
        "key": api_key,
        "limit": 1,
        "no_annotations": 1
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        if data["results"]:
            lat = data["results"][0]["geometry"]["lat"]
            lon = data["results"][0]["geometry"]["lng"]
            return float(lat), float(lon)
        else:
            print(f"Aucun résultat trouvé pour '{address}'")
            return None, None
    except requests.exceptions.RequestException as e:
        print(f"Erreur réseau pour l'adresse '{address}': {e}")
        return None, None
