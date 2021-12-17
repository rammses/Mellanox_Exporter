from os import walk, path
def get_log_files(_path):
    for root, dirs, files in walk(_path, topdown=False):
        for name in files:
            if name[-4:] == '.log':
                print(root +"/"+ name)






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    path = '/home/rammses/Belgeler/mellanox'

    dirs = get_log_files(_path=path)
    print(dirs)
