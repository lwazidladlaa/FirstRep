import requests

def lookup_word_details(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)

    if response.status_code != 200:
        # handle error
        print("Error:", response.json()["title"])
        return

    data = response.json()

    # extract audio url
    audio_url = data[0]["phonetics"][0].get("audio", "")

    # extract first definition
    definition = data[0]["meanings"][0]["definitions"][0]["definition"]

    # extract first synonym, if available
    synonym = ""
    try:
        synonym = data[0]["meanings"][0]["definitions"][0]["synonyms"][0]
    except (IndexError, KeyError):
        pass

    return audio_url, definition, synonym
