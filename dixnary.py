import requests


word = input("\t\tWELCOME !!\nType the word >>> ")
w = word.lower()
api_url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{w}"

response = requests.get(api_url)
response.encoding = 'utf-8'
content = response.json()

try:
    repo = content[0]['meanings']
    print(f"\nDefinitions for {word} ---->>>>\n")

    for r in range(len(repo)):

        part_of_speech = repo[r]['partOfSpeech']
        word_meanings = repo[r]['definitions']
        print(f"PART OF SPEECH : {part_of_speech}\n")

        for wm in word_meanings:
            try:
                definition = wm['definition']
                example = wm['example']
                synonyms = wm['synonyms']
                antonyms = wm['antonyms']

                print(f"MEANING : {definition}")
                print(f"EXAMPLE : {example}\n")

                if len(synonyms) > 0:
                    print(f"SYNONYMS : {synonyms}\n")

                if len(antonyms) > 0:
                    print(f"ANTONYMS : {antonyms}\n")

            except KeyError:
                pass


except KeyError:
    print("!! Please check the spellings.")