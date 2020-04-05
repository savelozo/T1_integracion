from django.shortcuts import render
from .api_requests import episodes_requests, characters_requests, locations_requests, direct_request

def index(request):

    episodes = episodes_requests().all_episodes()

    return render(request, 'index.html', {'episodes': episodes})

def episodes(request, id):

    episode = episodes_requests().get_episodes([id])
    url_characters = episode['characters']
    characters_ids = list()

    for url in url_characters:
        character_id = url.split('/')[-1]
        characters_ids.append(character_id)

    characters = characters_requests().get_characters(characters_ids)

    if isinstance(characters, dict):
        characters = [characters]

    return render(request, 'episodes.html', {'episode': episode, 'characters': characters})

def characters(request, id):

    characters = characters_requests().get_characters([id])

    if isinstance(characters, dict):
        characters = [characters]

    episodes_ids = list()

    for character in characters:

        for url in character['episode']:
            episode_id = url.split('/')[-1]
            episodes_ids.append(episode_id)

    episodes = episodes_requests().get_episodes(episodes_ids)

    if isinstance(episodes, dict):
        episodes = [episodes]

    if characters[0]['origin']['url'] != '':
        origin = direct_request(characters[0]['origin']['url'])
    else:
        origin = 'unknown'

    if characters[0]['location']['url'] != '':
        location = direct_request(characters[0]['location']['url'])
    else:
        location = 'unknown'

    return render(request, 'characters.html', {'characters': characters, 'episodes': episodes, 'origin': origin, 'location': location})

def locations(request, id):

    location = locations_requests().get_locations([id])
    residents = location['residents']

    residents_ids = list()

    for url_resident in residents:
        resident_id = url_resident.split('/')[-1]
        residents_ids.append(resident_id)

    characters = characters_requests().get_characters(residents_ids)

    if isinstance(characters, dict):
        characters = [characters]

    return render(request, 'locations.html', {'location': location, 'characters': characters})
