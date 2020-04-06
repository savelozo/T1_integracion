import requests

BASE_URL = "https://integracion-rick-morty-api.herokuapp.com/api/"

def direct_request(url):

    response = requests.get(url).json()
    return response

class episodes_requests:

    def __init__(self):

        self.episodes_url = BASE_URL + 'episode/'

    def all_episodes(self):

        episodes = requests.get(self.episodes_url).json()
        list_episodes = episodes['results']

        previous_page = episodes
        for page in range(1, episodes['info']['pages']):
            new_page = requests.get(previous_page['info']['next']).json()
            list_episodes += new_page['results']
            previous_page = new_page

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

    def all_characters(self):

        characters = requests.get(self.characters_url).json()
        list_characters = characters['results']

        previous_page = characters
        for page in range(1, characters['info']['pages']):
            new_page = requests.get(previous_page['info']['next']).json()
            list_characters += new_page['results']
            previous_page = new_page

        return list_characters

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

    def all_locations(self):

        locations = requests.get(self.locations_url).json()
        list_locations = locations['results']

        previous_page = locations
        for page in range(1, locations['info']['pages']):
            new_page = requests.get(previous_page['info']['next']).json()
            list_locations += new_page['results']
            previous_page = new_page

        return list_locations

    def get_locations(self, list_ids):

        ids = str()
        for id in list_ids:
            if id == list_ids[-1]:
                ids += "{}".format(id)
            else:
                ids += "{},".format(id)

        locations = requests.get(self.locations_url + ids).json()
        return locations
