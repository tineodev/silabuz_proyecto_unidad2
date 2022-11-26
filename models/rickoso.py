import datetime

class Rickoso:

    def __init__(self, name, status, species, image, location, origin, episode):
        self.name = name
        self.status = status
        self.species = species
        self.image = image
        self.location = location,
        self.origin = origin,
        self.episode = episode


    def to_json(self):
        return {
          "name": self.name,
          "status" : self.status,
          "species": self.species,
          "image": self.image,
          "location": self.location,
          "origin": self.origin,
          "episode": self.episode,
        }
        