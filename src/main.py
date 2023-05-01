from cyber_city.game import Game, read_objects_from_excel

read_objects_from_excel("./game_data.xlsx")

game = Game()
print(game.data_str)
