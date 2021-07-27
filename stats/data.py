import os
import glob
import pandas as pd


#game_files = glob.glob(os.path.join(os.getcwd(), 'games', '*.EVE'))
game_files = glob.glob(os.path.join(os.path.abspath(os.path.dirname(__file__)), '*.EVE'))
game_files.sort()

for game_file in game_files:
    game_frame = pd.read_csv(game_file, names=['type', 'multi2', 'multi3', 'multi4', 'multi5', 'multi6', 'rvrnt'])
    print(game_frame)

if __name__ == "__main__":
    pass
    # os.getcwd() gets the absolute path from the file is executed/

    # print(os.getcwd(), '')
    # print(os.path.join(os.getcwd(), ''))
    # print(os.path.abspath(os.path.dirname(__file__)))
    # print(os.path.dirname(__file__))

    #print(game_files)
