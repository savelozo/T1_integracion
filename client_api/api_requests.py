import requests

BASE_URL = 'https://rickandmortyapi.com/api/'

def direct_request(url):

    response = requests.get(url).json()
    return response

class episodes_requests:

    def __init__(self):

        self.episodes_url = BASE_URL + 'episode/'

    def all_episodes(self):

        episodes = requests.get(self.episodes_url).json()
        list_episodes = episodes['results']

        for page in range(1, episodes['info']['pages']):
            new_page = requests.get(episodes['info']['next']).json()
            list_episodes += new_page['results']

        return list_episodes

    def get_episodes(self, list_ids):

        ids = str()
        for id in list_ids:
            if id == list_ids[-1]:
                ids += "{}".format(id)
            else:
                ids += "{},".format(id)

        episode = requests.get(self.episodes_url + ids).json()
        return episode


class characters_requests:

    def __init__(self):

        self.characters_url = BASE_URL + 'character/'

    def get_characters(self, list_ids):

        ids = str()
        for id in list_ids:
            if id == list_ids[-1]:
                ids += "{}".format(id)
            else:
                ids += "{},".format(id)

        characters = requests.get(self.characters_url + ids).json()
        return characters

class locations_requests:

    def __init__(self):

        self.locations_url = BASE_URL + 'location/'

    def get_locations(self, list_ids):

        ids = str()
        for id in list_ids:
            if id == list_ids[-1]:
                ids += "{}".format(id)
            else:
                ids += "{},".format(id)

        locations = requests.get(self.locations_url + ids).json()
        return locations
