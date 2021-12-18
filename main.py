from os import walk, path
import graypy
import logging

def get_log_files(_path):
    list_of_log_files=[]
    for root, dirs, files in walk(_path, topdown=False):
        for name in files:
            if name[-4:] == '.log':
                # print(root +"/"+ name)
                list_of_log_files.append(root +"/"+ name)
    return list_of_log_files

# Press the green button in the gutter to run the script.
def get_contents_of_file(file):
    with open(file,'r') as file:
        lines=file.readlines()

    return lines




if __name__ == '__main__':

    # Setup handler and loggers
    my_logger = logging.getLogger('test_logger')
    my_logger.setLevel(logging.DEBUG)
    handler = graypy.GELFTCPHandler('172.21.21.134', 12201)

    my_logger.addHandler(handler)

    path = '/home/rammses/Belgeler/mellanox'
    test_file = '/home/rammses/Belgeler/mellanox/cl_support_LSW-GY-H3-RBG30-TYC-P1-N39_20211206_122928/var/log/switchd.log'

    logfiles = get_log_files(_path=path)
    print(logfiles)
    for file in logfiles:
        print(file)
        for item in get_contents_of_file(test_file):
            # print(item.strip('\n'))
            my_logger.debug(item.strip('\n'))





    # loop thru dirs

    # send logs