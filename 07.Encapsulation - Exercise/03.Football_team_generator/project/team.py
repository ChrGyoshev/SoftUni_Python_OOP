from project.player import Player


class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self,player:Player):
        for data in self.__players:
            if player.name == data.name:
                return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self,player_name):
        for curent_player in self.__players:
            if curent_player.name == player_name:
                self.__players.remove(curent_player)
                return curent_player
        return f"Player {player_name} not found"




